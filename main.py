# bouncing dvd logo

import sys
import random
import time

try:
    import bext
except ImportError:
    print('This program requires the bext module: https://pypi.org/project/Bext/')
    sys.exit()

# set up constants
WIDTH, HEIGHT = bext.size()
# reduce width by 1 for Windows
WIDTH =-1
NUMBER_OF_LOGOS = 5
PAUSE_AMOUNT = 0.2
COLORS = ['red', 'green', 'yellow', 'blue', 'magenta', 'cyan', 'white']
UP_RIGHT = 'ur'
UP_LEFT = 'ul'
DOWN_RIGHT = 'dr'
DOWN_LEFT = 'dl'
DIRECTIONS = (UP_RIGHT, UP_LEFT, DOWN_RIGHT, DOWN_LEFT)

# key names for logo dicitonaries
COLOR = 'color'
X = 'x'
Y = 'y'
DIR = 'direction'


def main():
    bext.clear()

    # generate logos
    logos = []
    for i in range(NUMBER_OF_LOGOS):
        logos.append({COLOR: random.choice(COLORS),
                      X: random.randint(1, WIDTH - 4),
                      Y: random.randint(1, HEIGHT - 4),
                      DIR: random.choice(DIRECTIONS)})
        if logos[-1][X] % 2 == 1:
            # make sure X is even to hit the corners
            logos[-1][X] -= 1
    # count how many times logo hits the corner
    cornerBounces = 0
    while True:
        for logo in logos:
            # erase logo's current location
            bext.goto(logo[X], logo[Y])
            print('  ', end='')

            originalDirection = logo[DIR]

            # See if the logo bounces off the corners:
            if logo[X] == 0 and logo[Y] == 0:
                logo[DIR] = DOWN_RIGHT
                cornerBounces += 1
            elif logo[X] == 0 and logo[Y] == HEIGHT - 1:
                logo[DIR] = UP_RIGHT
                cornerBounces += 1
            elif logo[X] == WIDTH - 3 and logo[Y] == 0:
                logo[DIR] = DOWN_LEFT
                cornerBounces += 1
            elif logo[X] == WIDTH - 3 and logo[Y] == HEIGHT - 1:
                logo[DIR] = UP_LEFT
                cornerBounces += 1
            # see if logo bounces off left edge
            elif logo[X] == 0 and logo[DIR] == UP_LEFT:
                logo[DIR] = UP_RIGHT
            elif logo[X] == 0 and logo[DIR] == DOWN_LEFT:
                logo[DIR] = DOWN_RIGHT
            # see if logo bounces off right edge
            elif logo[X] == WIDTH - 3 and logo[DIR] == UP_RIGHT:
                logo[DIR] = UP_LEFT
            elif logo[X] == WIDTH - 3 and logo[DIR] == DOWN_RIGHT:
                logo[DIR] = DOWN_LEFT
            # see if logo bounces off top edge
            elif logo[Y] == HEIGHT - 1 and logo[DIR] == UP_LEFT:
                logo[DIR] = DOWN_LEFT
            elif logo[Y] == 0 and logo[DIR] == UP_RIGHT:
                logo[DIR] = DOWN_RIGHT
            # see if logo bounces off bottom edge
            elif logo[Y] == HEIGHT -1 and logo[DIR] == DOWN_LEFT:
                logo[DIR] = UP_LEFT
            elif logo[Y] == HEIGHT -1 and logo[DIR] == DOWN_RIGHT:
                logo[DIR] = UP_RIGHT

            if logo[DIR] != originalDirection:
                # change color when logo bounces
                logo[COLOR] = random.choice(COLORS)

            # move logo (x moves by 2 because the terminal characters are twice as tall as they are wide)
            if logo[DIR] == UP_RIGHT:
                logo[X] += 2
                logo[Y] -= 1
            elif logo[DIR] == UP_LEFT:
                logo[X] += 2
                logo[Y] -= 1
            elif logo[DIR] == DOWN_RIGHT:
                logo[X] -= 2
                logo[Y] -= 1
            elif logo[DIR] == DOWN_LEFT:
                logo[X] -= 2
                logo[Y] += 1

        # display number of corner bounces
        bext.goto(5, 0)
        bext.fg('white')
        print('Corner bounces:', cornerBounces, end ='')

        for logo in logos:
            # draw the logos at the their new location
            bext.goto(logo[X], logo[Y])
            bext.fg(logo[COLOR])
            print('DVD', end='')

        bext.goto(0,0)

        sys.stdout.flush() # required for bext programs
        time.sleep(PAUSE_AMOUNT)

# if program was run instead of imported, run the game
if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print()
        print('Bouncing DVD logo')
        sys.exit() # when CTRL+C is pressed, end the program
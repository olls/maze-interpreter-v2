import sys
import time
import re
import argparse

import funcs
import controls
import parser
import run
from colors import *


CLS = '\033[2J'
CLS_END = '\033[0J'
CLS_END_LN = '\033[0K'
REDRAW = '\033[0;0f'
HIDE_CUR = '\033[?25l'
SHOW_CUR = '\033[?25h'


class Car:
    def __init__(self, value, x, y):
        self.value = value
        self.x = x
        self.y = y
        self.direction = 'D'
        self.pause = 0


def get_args():
    parser = argparse.ArgumentParser(
        description='A Maze interpreter (http://esolangs.org/wiki/Maze)')
    parser.add_argument('file', type=open,
        help='the program to run')
    parser.add_argument('-d', '--debug', action='store_true',
        help='display the maze during interpretation.')
    parser.add_argument('-c', '--no-colors', action='store_false',
        help='shows the maze without color when in debug mode.')
    parser.add_argument('-f', '--fps', default=10, type=int,
        help='the fps of the maze when in debug mode.')

    args = parser.parse_args()
    return args


def output(maze, cars, logs, colors=True):
    out = ''

    for y, row in enumerate(maze):
        for x, cell in enumerate(row):

            # Get value of cell without car.
            value = controls.display[cell.name].format(value=cell.value)
            color = controls.colors[cell.name]

            # Should only be one car in cell, but if not print last one.
            car = [car for car in cars if car.x == x and car.y == y]
            if car:
                # Replace value of cell with value of car if there is one.
                value = car[-1].value
                color = {'bg': color['bg'], 'fg': BLACK, 'style': None}

            # Two characters wide.
            value = str(value)
            if len(value) > 2:
                value = value[:2]
            elif len(value) < 2:
                value = ('0' * (2 - len(value))) + value

            out += colorStr(value, **color) if colors else value
        out += CLS_END_LN + '\n'
    out += (CLS_END_LN + '\n').join(logs[-10:])

    print(REDRAW + out + CLS_END)


def main():
    logs = []
    args = get_args()

    maze, functions = parser.parse_file(args.file)
    args.file.close()

    cars = run.create_cars(maze, Car)

    if args.debug:
        print(HIDE_CUR)
        print(CLS)
        output(maze, cars, logs, args.no_colors)

    try:
        while cars:
            maze, cars = run.move_cars(maze, cars)

            if args.debug:
                time.sleep(1 / args.fps)
                output(maze, cars, logs, args.no_colors)

            maze, cars, new_logs = run.car_actions(maze, cars, functions, debug=args.debug)

            if args.debug:
                logs += new_logs
            else:
                print('\n'.join(new_logs) if new_logs)

    finally:
        if args.debug: print(SHOW_CUR)


if __name__ == '__main__':
    main()

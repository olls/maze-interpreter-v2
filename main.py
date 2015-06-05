import sys
import time
import re
import argparse

import funcs
import controls
import parser
import run
from colors import *


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


def output(maze, cars, out=True, colors=True):
    if not out: return
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
        out += '\n'

    print(out)


def main():
    args = get_args()

    maze, functions = parser.parse_file(args.file)
    args.file.close()

    cars = run.create_cars(maze, Car)

    output(maze, cars, args.debug, args.no_colors)
    while cars:
        if args.debug:
            time.sleep(1 / args.fps)

        maze, cars = run.move_cars(maze, cars)
        output(maze, cars, args.debug, args.no_colors)
        maze, cars = run.car_actions(maze, cars, functions, debug=args.debug)

    print('\n' * (not args.debug), end='')


if __name__ == '__main__':
    main()

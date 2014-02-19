import sys
import time
import re
import argparse

import funcs
import controls
import parser
import run


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
    parser.add_argument('file', type=argparse.FileType('r'),
        help='the file to run')
    args = parser.parse_args()

    return args


def output(maze, cars):
    out = ''

    for y, row in enumerate(maze):
        for x, cell in enumerate(row):

            # Get value
            value = controls.display[cell.name].format(value=cell.value)
            car = [car for car in cars if car.x == x and  car.y == y]
            if car:
                if not len(car) == 1:
                    funcs.error('Multiple cars in same cell.')
                value = car[-1].value

            # Two characters wide.
            value = str(value)
            if len(value) > 2:
                value = value[:2]
            elif len(value) < 2:
                value = ('0' * (2 - len(value))) + value

            out += value
        out += '\n'

    print(out)


def main():
    args = get_args()

    maze = parser.parse_file(args.file)
    args.file.close()

    cars = run.create_cars(maze, Car)
    output(maze, cars)
    while cars:
        maze, cars = run.move_cars(maze, cars)
        maze, cars = run.car_actions(maze, cars)
        output(maze, cars)

        time.sleep(.6)

if __name__ == '__main__':
    main()

import sys
import time
import re
import argparse

import parser
import run
import out


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
    parser.add_argument('-l', '--log-length', default=10, type=int,
        help='Max length of debug log.')
    parser.add_argument('-c', '--no-colors', action='store_false',
        help='shows the maze without color when in debug mode.')
    parser.add_argument('-f', '--fps', default=10, type=int,
        help='the fps of the maze when in debug mode.')

    args = parser.parse_args()
    return args


def main():
    logs = ''
    args = get_args()

    maze, functions = parser.parse_file(args.file)
    args.file.close()

    cars = run.create_cars(maze, Car)

    if args.debug: out.init()

    try:
        while cars:

            if args.debug:
                out.output(maze, cars, logs, args.no_colors)

            maze, cars = run.move_cars(maze, cars)
            maze, cars, new_logs = run.car_actions(maze, cars, functions, debug=args.debug)

            if args.debug:
                if new_logs:
                    logs = out.log_lines(logs + new_logs, args.log_length)
                time.sleep(1 / args.fps)

            else:
                print(new_logs, end='')

    finally:
        if args.debug: out.end()


if __name__ == '__main__':
    main()

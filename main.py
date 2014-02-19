import re
import argparse
import parse_input as pi


def get_args():
    parser = argparse.ArgumentParser(
        description='A Maze interpreter (http://esolangs.org/wiki/Maze)')
    parser.add_argument('file', type=argparse.FileType('r'), help='the file to run')
    args = parser.parse_args()

    return args


def main():
    args = get_args()

    maze = pi.parse_file(args.file)

    print(maze)


if __name__ == '__main__':
    main()

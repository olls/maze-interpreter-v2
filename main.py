import re
import argparse
import parse_maze as pi


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
    print('\n'.join(''.join(char+(' '*(10-len(char))) for char in line) for line in maze))


if __name__ == '__main__':
    main()

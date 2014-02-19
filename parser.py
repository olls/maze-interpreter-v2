import re

import funcs
import controls


class Cell:
    def __init__(self, name, value):
        self.name = name
        self.value = value


def get_cell(line):
    """
        Returns the line minus the first cell it finds, and the cell.
    """

    # Search for matches for each control.
    matches = []
    for name, pattern in controls.regexes.items():
        match = re.search(pattern, line)
        if match:
            matches.append((name, match))

    if not matches:
        return False, None

    # Use control match closest to the beginning of the line, remove everything
    #    to the end of the match from the line.
    match = min(matches, key=lambda k: k[1].start())
    line = line[match[1].end():]

    value = match[1].group()

    return line, Cell(match[0], value)


def parse_file(file_):

    game = file_.read().splitlines()

    cells = []
    for line in game:

        if '//' in line:
            line = line[:line.index('//')]

        cells.append([])
        while line:
            line, cell = get_cell(line)

            if cell:
                cells[-1].append(cell)

    return cells


def main():

    with open('test.mz', 'r') as f:
        print(parse_file(f))


if __name__ == '__main__':
    main()

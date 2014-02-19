import re


CONTROLS = {
    'wall': r'##|``',
    'path': r'\.\.',
    'splitter': r'<>',
    'pause': r'[0-9]{2}',
    'start': r'\^\^',
    'hole': r'\(\)',
    'out': r'>>',
    'in': r'<<',
    'one-use': r'--',
    'direction': r'%[LRUDlrud]',
    'signal': r'\*\*',
    'function': r'[A-Za-z]{2}'
}


def get_cell(line):

    # Search for matches for each control.
    matches = []
    for name, pattern in CONTROLS.items():
        match = re.search(pattern, line)
        if match:
            matches.append((name, match))

    if not matches:
        return False, None

    # Use control match closest to the beginning of the line, remove everything
    #    to the end of the match from the line.
    match = min(matches, key=lambda k: k[1].start())
    line = line[match[1].end():]

    return line, match[0]


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

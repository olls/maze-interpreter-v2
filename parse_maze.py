import re


CONTROLS = {
    'wall': r'\#\#',
    'path': r'\.\.',
    'splitter': r'\<\>',
    'pause': r'[0-9]{2}',
    'start': r'\^\^',
    'hole': r'\(\)',
    'out': r'\>\>',
    'in': r'\<\<',
    'one-use': r'\-\-',
    'direction': r'%[LRUDlrud]',
    'signal': r'\*\*',
    'function': r'[A-z]{2}'
}


def get_cell(line):
    for name, pattern in CONTROLS.items():
        match = re.match(' *(' + pattern + ')', line)
        if match:
            result = match.group()
            while result.startswith(' '):
                result = result[1:]
                line = line[1:]
            line = line[2:]
            return line, result

    return False, None


def parse_file(file_):

    game = file_.read().splitlines()

    cells = []
    for line in game:
        cells.append([])

        while line:
            line, cell = get_cell(line)
            cells[-1].append(cell)

    return cells

def main():
    with open('test.mz', 'r') as f:
        print(parse_file(f))


if __name__ == '__main__':
    main()

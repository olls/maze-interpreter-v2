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


def get_function(line):
    match = re.search(r'[A-Za-z]{2}', line.split('->')[0])
    if not match:
        funcs.error('Invalid function, invalid name.')
    name = match.group()

    match = re.search(r'[A-Za-z]{2} *-> *', line)
    if not match:
        funcs.error('Invalid function.')
    function = line[match.end():]

    if function.lower().startswith('if'):
        # Conditional

        match = re.search(r'([<>]=?)|==|\*\*', function)
        if not match:
            funcs.error('Invalid function, invalid condition.')
        condition = match.group()

        if not condition == '**':
            match = re.search(r'[0-9]+', function)
            try:
                number = int(match.group())
            except (ValueError, AttributeError):
                funcs.error('Invalid function, invalid value for condition.')


        # Then keyword and statement.
        match = re.search(r' *[Tt][Hh][Ee][Nn] *', function)
        if not match:
            funcs.error('Invalid function, no THEN keyword.')
        then_keywd = match.group()
        function = function[match.end():]

        match = re.search(controls.regexes['direction'], function)
        if not match:
            funcs.error('Invalid function, no THEN statement.')
        then = match.group()


        # Else keyword and statement.
        match = re.search(r' *[Ee][Ll][Ss][Ee] *', function)
        if not match:
            funcs.error('Invalid function, no ELSE keyword.')
        function = function[match.end():]

        match = re.search(controls.regexes['direction'], function)
        else_ = match.group()
        if not else_:
            funcs.error('Invalid function, no THEN condition.')


        if condition == '**':
            function = lambda value, signal: then if signal else else_
        else:

            if condition == '<=':
                function = lambda value: then if int(value) <= number else else_
            elif condition == '==':
                function = lambda value: then if int(value) == number else else_
            elif condition == '>=':
                function = lambda value: then if int(value) >= number else else_
            elif condition == '>':
                function = lambda value: then if int(value) > number else else_
            elif condition == '<':
                function = lambda value: then if int(value) < number else else_

    else:
        # Assignment
        print(function)

        match = re.search(r'[-+*/]?=', function)
        if not match:
            funcs.error('Invalid function, invalid operator.')
        operator = match.group()

        match = re.search(r'[0-9]+', function)
        try:
            number = int(match.group())
        except (ValueError, AttributeError):
            funcs.error('Invalid function, invalid value for operator.')

        if operator == '=':
            function = lambda value: number
        elif operator == '-=':
            function = lambda value: int(value) - number
        elif operator == '+=':
            function = lambda value: int(value) + number
        elif operator == '*=':
            function = lambda value: int(value) * number
        elif operator == '/=':
            function = lambda value: int(value) / number

    return {name: function}


def parse_file(file_):

    game = file_.read().splitlines()

    cells = []
    functions = {}
    for line in game:

        if '//' in line:
            line = line[:line.index('//')]

        if '->' not in line:
            # Maze

            cells.append([])
            while line:
                line, cell = get_cell(line)

                if cell:
                    cells[-1].append(cell)

        else:
            # Function
            function = get_function(line)
            functions.update(function)

    return cells, functions


def main():

    with open('test.mz', 'r') as f:
        print(parse_file(f))


if __name__ == '__main__':
    main()

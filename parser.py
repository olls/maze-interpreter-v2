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
    """
        Parses and returns a function on the given line.
    """

    # Get function name from before the function assignment operator.
    match = re.search(controls.regexes['function'], line.split('->')[0])
    if not match:
        funcs.error('Invalid function, invalid name.')
    name = match.group()

    # Make sure the function has an function assignment operator.
    match = re.search(controls.regexes['function'] + r' *-> *', line)
    if not match:
        funcs.error('Invalid function.')
    function = line[match.end():]

    # Function type: conditional or assignment.
    if function.lower().startswith('if'): # Conditional

        # Get Condition
        match = re.search(r'([<>]=?)|==|(\*(?=[\*A-Za-z0-9]))', function)
        if not match:
            funcs.error('Invalid function, invalid condition.')
        condition = match.group()

        # Get condition value
        if condition == '*':
            match = re.search(controls.regexes['signal'], function)
            try:
                number = match.group()
            except (ValueError, AttributeError):
                funcs.error('Invalid function, invalid value for signal.')
        else:
            match = re.search(r'(-?[0-9]+)|((?<=")[^"]*(?=")|(?<=\')[^\']*(?=\'))', function)
            if match.group(1):
                number = int(match.group(1))
                string = None
            elif isinstance(match.group(2),str) and condition == '==':
                number = None
                string = str(match.group(2))
            else:
                funcs.error('Invalid function, invalid value for condition.')

        # Get 'then' keyword and statement.
        match = re.search(r' *then *', function.lower())
        if not match:
            funcs.error('Invalid function, no THEN keyword.')
        then_keywd = match.group()
        function = function[match.end():]

        match = re.search(controls.regexes['direction'], function)
        if not match:
            funcs.error('Invalid function, no THEN statement.')
        then = match.group()

        # Get 'else' keyword and statement.
        match = re.search(r' *else *', function.lower())
        if not match:
            else_ = None
        else:
            function = function[match.end():]

            match = re.search(controls.regexes['direction'], function)
            else_ = match.group()
            if not else_:
                funcs.error('Invalid function, no ELSE statement.')

        # Create lambda representing the function.
        if condition == '*':
            if number == '*':
                function = lambda value, signal: then if signal else else_
            else:
                function = lambda value, signal: then if '*' in signal or number in signal else else_

        elif condition == '<=':
            function = lambda value: then if int(value) <= number else else_
        elif condition == '==':
            if isinstance(string,str):
                function = lambda value: then if funcs.escape(value) == string else else_
            else:
                function = lambda value: then if int(value) == number else else_
        elif condition == '>=':
            function = lambda value: then if int(value) >= number else else_
        elif condition == '>':
            function = lambda value: then if int(value) > number else else_
        elif condition == '<':
            function = lambda value: then if int(value) < number else else_

    else: # Assignment

        # Make sure it has an assignment operator.
        match = re.search(r'[-+*/]?=', function)
        if not match:
            funcs.error('Invalid function, invalid operator.')
        operator = match.group()

        # Create lambdas representing the assignment.
        if operator == '=':
            # Find a string or an int
            quotes = r'(?<=")[^"]*(?=")|(?<=\')[^\']*(?=\')'
            str_match = re.search(quotes, function)
            int_match = re.search(r'-?[0-9]+', function)
            if not str_match and not int_match:
                funcs.error('Invalid function, invalid assignment value.')

            assign = (str_match or int_match).group()

            # Fix new lines in string assignment
            assign = '\n'.join(assign.split('\\n'))

            function = lambda value: assign

        else:
            # Find an int
            match = re.search(r'-?[0-9]+', function)
            try:
                number = int(match.group())
            except (ValueError, AttributeError):
                funcs.error('Invalid function, invalid value for operator.')

            if operator == '-=':
                function = lambda value: int(int(value) - number)
            elif operator == '+=':
                function = lambda value: int(int(value) + number)
            elif operator == '*=':
                function = lambda value: int(int(value) * number)
            elif operator == '/=':
                function = lambda value: int(int(value) / number)

    return {name: function}


def parse_file(file_):
    game = file_.read().splitlines()

    cells = []
    functions = {}
    for line in game:

        if '//' in line:
            # Remove any comment
            line = line[:line.index('//')]
        if '->' not in line:
            # A part of the maze, not a function
            cells.append([])
            while line:
                # Keep taking a cell off the beginning of the line, until it's empty.
                line, cell = get_cell(line)

                if cell:
                    cells[-1].append(cell)

            if not cells[-1]:
                cells = cells[:-1]
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

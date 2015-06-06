import controls
import funcs
from colors import *


escape_codes = {
  'CLS': '\033[2J',
  'CLS_END': '\033[0J',
  'CLS_END_LN': '\033[0K',
  'REDRAW': '\033[0;0f',
  'HIDE_CUR': '\033[?25l',
  'SHOW_CUR': '\033[?25h'
}


def log_lines(logs, n):
    return ('\n' + escape_codes['CLS_END_LN']).join(line for line in logs.split('\n')[-n:])


def output(maze, cars, logs, colors=True):
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
                color = {
                    'bg': color['bg'],
                    'fg': WHITE if color['bg'] == BLACK else BLACK,
                    'style': None
                }

            # Two characters wide.
            value = funcs.escape(value)
            if len(value) > 2:
                value = value[:2]
            elif len(value) < 2:
                value = ('0' * (2 - len(value))) + value

            out += colorStr(value, **color) if colors else value
        out += escape_codes['CLS_END_LN'] + '\n'
    out += logs

    print(escape_codes['REDRAW'] + out + escape_codes['CLS_END'])


def init(simple_out):
    global escape_codes
    for i in escape_codes:
      escape_codes[i] = '' if simple_out else escape_codes[i]

    print(escape_codes['HIDE_CUR'] + escape_codes['CLS'])


def end():
    print(escape_codes['SHOW_CUR'])

import controls
import funcs
from colors import *


CLS = '\033[2J'
CLS_END = '\033[0J'
CLS_END_LN = '\033[0K'
REDRAW = '\033[0;0f'
HIDE_CUR = '\033[?25l'
SHOW_CUR = '\033[?25h'


def log_lines(logs, n):
    return ('\n' + CLS_END_LN).join(line for line in logs.split('\n')[-n:])


def output(maze, cars, logs, colors=True, scale=1):
    out = ''

    for y, row in enumerate(maze):
        next_row = ''
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

            next_row += (colorStr(value, **color) if colors else value) * scale

        out += (next_row + CLS_END_LN + '\n') * scale
    out += logs

    print(REDRAW + out + CLS_END)


def init():
    print(HIDE_CUR + CLS)

def end():
    print(SHOW_CUR)

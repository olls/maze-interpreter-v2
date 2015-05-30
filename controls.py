from colors import *


regexes = {
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
    'function': r'[A-Za-z][A-Za-z0-9]'
}


display = {
    'wall': '##',
    'path': '  ',
    'splitter': '<>',
    'pause': '{value}',
    'start': '^^',
    'hole': '()',
    'out': '>>',
    'in': '<<',
    'one-use': '--',
    'direction': '{value}',
    'signal': '**',
    'function': '{value}'
}


colors = {
    'wall':         {'fg': WHITE,    'bg': BLACK,   'style': CLEAR},
    'path':         {'fg': WHITE,    'bg': WHITE,   'style': CLEAR},
    'splitter':     {'fg': WHITE,    'bg': GREEN,   'style': None},
    'pause':        {'fg': WHITE,    'bg': YELLOW,  'style': None},
    'start':        {'fg': WHITE,    'bg': GREEN,   'style': None},
    'hole':         {'fg': WHITE,    'bg': RED,     'style': None},
    'out':          {'fg': WHITE,    'bg': BLUE,    'style': None},
    'in':           {'fg': WHITE,    'bg': BLUE,    'style': None},
    'one-use':      {'fg': WHITE,    'bg': MAGENTA, 'style': None},
    'direction':    {'fg': WHITE,    'bg': CYAN,    'style': None},
    'signal':       {'fg': BLACK,    'bg': WHITE,   'style': None},
    'function':     {'fg': WHITE,    'bg': BLACK,   'style': None}
}
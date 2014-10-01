

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
    'function': r'[A-Za-z]{2}'
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

import sys


def error(message):
    while message.startswith(' '):
        message = message[1:]

    if message.lower().startswith('error'):
        message = message[5:]

    while message.startswith(' '):
        message = message[1:]

    if message.lower().startswith(':'):
        message = message[1:]

    while message.startswith(' '):
        message = message[1:]

    sys.exit(('Error: ' if not message.lower().startswith('error') else '') +
        message)

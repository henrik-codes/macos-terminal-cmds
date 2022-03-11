# -*- coding: utf-8 -*-

from argparse import ArgumentParser
from ..util.entrypoint import entrypoint
from ..lib import terminal_bounds_get, terminal_bounds_set, \
    AppleScriptWrapperError, MacOSTerminalException


def split(name, delim, split_type, splits=2):
    def _int_split(value):
        values = value.split(delim)

        if len(values) != splits:
            raise ValueError('Invalid value')

        return tuple(map(split_type, values))

    _int_split.__name__ = name
    return _int_split


position_type = split('position', ',', int)
size_type = split('size', 'x', int)


@entrypoint
def main(args=None):
    parser = ArgumentParser()
    parser.add_argument('position', type=position_type, help='Position (e.g. 0,0)', nargs='?')
    parser.add_argument('size', type=size_type, help='Height x Width (e.g. 800x600)')

    namespace = parser.parse_args(args)

    old_bounds = terminal_bounds_get()

    if namespace.position:
        x, y = namespace.position
    else:
        x, y = old_bounds.x, old_bounds.y

    w, h = namespace.size

    terminal_bounds_set(x, y, w, h)

# -*- coding: utf-8 -*-

from argparse import ArgumentParser
from ..util.entrypoint import entrypoint
from ..lib import terminal_profile_set, AppleScriptWrapperError, MacOSTerminalException


@entrypoint
def main(args=None):
    parser = ArgumentParser()
    parser.add_argument('theme', nargs='*')

    namespace = parser.parse_args(args)

    if namespace.theme:
        theme = ' '.join(namespace.theme)
    else:
        theme = 'Solid Colors'

    terminal_profile_set(theme)

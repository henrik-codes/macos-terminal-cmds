# -*- coding: utf-8 -*-

from argparse import ArgumentParser
from ..util.entrypoint import entrypoint
from ..lib import terminal_custom_title_set, AppleScriptWrapperError, MacOSTerminalException


@entrypoint
def main(args=None):
    parser = ArgumentParser()
    parser.add_argument('title', nargs='+')

    namespace = parser.parse_args(args)

    title = ' '.join(namespace.title)

    terminal_custom_title_set(title)

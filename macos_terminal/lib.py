# -*- coding: utf-8 -*-

from .util.wrapper import run
from collections import namedtuple


class MacOSTerminalException(Exception):
    pass


class AppleScriptWrapperError(MacOSTerminalException):
    pass


MacOSTerminalBounds = namedtuple('MacOSTerminalBounds', [
    'x',
    'y',
    'width',
    'height',
])


def terminal_profile_get():
    return run(
        'terminal-profile-get',
        on_error=AppleScriptWrapperError('Failed to get theme'))


def terminal_profile_set(name):
    run('terminal-profile-set', name,
        on_error=AppleScriptWrapperError('Failed to set theme'))


def terminal_custom_title_get():
    return run(
        'terminal-custom-title-get',
        on_error=AppleScriptWrapperError('Failed to get title'))


def terminal_custom_title_set(name):
    run('terminal-custom-title-set', name,
        on_error=AppleScriptWrapperError('Failed to set title'))


def terminal_bounds_get():
    output = run(
        'terminal-bounds-get',
        on_error=AppleScriptWrapperError('Failed to get bounds'))

    return MacOSTerminalBounds(*map(int, output.split(', ')))


def terminal_bounds_set(x, y, width, height):
    """ Set the coordinate and size of the active terminal

        NOTE: Result may not be exactly as set if the window is unable to move
              to requested location. This happens at least if setting the
              y-coordinate to 0, which will be translated to something like 34.
    """
    run('terminal-bounds-set', *map(str, (x, y, width, height)),
        on_error=AppleScriptWrapperError('Failed to set bounds'))

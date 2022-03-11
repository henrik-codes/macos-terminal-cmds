# -*- coding: utf-8 -*-

import unittest
import macos_terminal


class TestLib(unittest.TestCase):

    def test_theme(self):
        original_theme = macos_terminal.terminal_profile_get()

        try:
            macos_terminal.terminal_profile_set('Homebrew')
            self.assertEqual('Homebrew', macos_terminal.terminal_profile_get())

            macos_terminal.terminal_profile_set('Red Sands')
            self.assertEqual('Red Sands', macos_terminal.terminal_profile_get())

        finally:
            macos_terminal.terminal_profile_set(original_theme)
            self.assertEqual(original_theme, macos_terminal.terminal_profile_get())

    def test_title(self):
        original_title = macos_terminal.terminal_custom_title_get()

        try:
            macos_terminal.terminal_custom_title_set('Hello world')
            self.assertEqual('Hello world', macos_terminal.terminal_custom_title_get())

            macos_terminal.terminal_custom_title_set('¡Ay, caramba!')
            self.assertEqual('¡Ay, caramba!', macos_terminal.terminal_custom_title_get())

            macos_terminal.terminal_custom_title_set('🤯')
            self.assertEqual('🤯', macos_terminal.terminal_custom_title_get())
        finally:
            macos_terminal.terminal_custom_title_set(original_title)
            self.assertEqual(original_title, macos_terminal.terminal_custom_title_get())

    def test_size(self):
        original_bounds = macos_terminal.terminal_bounds_get()

        try:
            macos_terminal.terminal_bounds_set(50, 100, 800, 600)
            self.assertEqual(
                macos_terminal.MacOSTerminalBounds(x=50, y=100, width=800, height=600),
                macos_terminal.terminal_bounds_get())

            macos_terminal.terminal_bounds_set(0, 50, 500, 300)
            self.assertEqual(
                macos_terminal.MacOSTerminalBounds(x=0, y=50, width=500, height=300),
                macos_terminal.terminal_bounds_get())

        finally:
            macos_terminal.terminal_bounds_set(*original_bounds)
            self.assertEqual(original_bounds, macos_terminal.terminal_bounds_get())

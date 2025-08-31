__all__ = ['show_window', 'hide_window']

import win32con
import win32gui


def show_window(in_title: str, actually_hide_it_instead=False):
    program_hwnd = None

    def win_enum_handler(hwnd, ctx) -> [None, int]:
        title = win32gui.GetWindowText(hwnd)
        if in_title in title:
            nonlocal program_hwnd
            program_hwnd = hwnd
            action = win32con.SW_SHOW
            if actually_hide_it_instead:
                action = win32con.SW_HIDE
            win32gui.ShowWindow(hwnd, action)

    win32gui.EnumWindows(win_enum_handler, None)
    return program_hwnd


def hide_window(in_title: str, actually_show_it_instead=False):
    return show_window(in_title, actually_hide_it_instead=not actually_show_it_instead)
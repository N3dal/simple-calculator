#!/usr/bin/python3
# -----------------------------------------------------------------
# simple calculator using python/tkinter.
#
#
#
# Author:N84.
#
# Create Date:Sat May 21 10:33:22 2022.
# ///
# ///
# ///
# -----------------------------------------------------------------

from os import system
from os import name as OS_NAME
import tkinter


def clear():
    """wipe the terminal screen"""

    if OS_NAME == "posix":
        # *nix machines.
        system("clear")

    else:
        # windows machines.
        system("cls")


def start_app(root: tkinter.Tk):
    """"""
    # note: add any thing you want to do,
    # with the startup.
    root.mainloop()


def main_window():
    """main window for the calculator."""


def main():
    main_window()


if __name__ == "__main__":
    main()

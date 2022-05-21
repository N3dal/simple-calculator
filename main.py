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


# set the program defaults.
WIN_WIDTH = 344
WIN_HEIGHT = 454
WIN_TITLE = "Calculator"
WIN_BG = "black"
WIDGETS_FONT = "Calibre"

BTN_STYLE = {
    "font": ("calibre", 14, "bold"),
    "width": 5,
    "height": 2,
    "borderwidth": 0,
    "highlightbackground": "black",
    "highlightthickness": 0,
    "bg": "gray22",
    "fg": "white",
    "activebackground": "gray28",
    "activeforeground": "white"

}

LABEL_STYLE = {
    "borderwidth": 0,
    "highlightbackground": "black",
    "highlightthickness": 0,
    "bg": "black",
    "fg": "white",

}


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

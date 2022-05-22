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


clear()


def start_app(root: tkinter.Tk):
    """"""
    # note: add any thing you want to do,
    # with the startup.
    root.mainloop()


def main_window():
    """main window for the calculator."""

    root = tkinter.Tk()

    root.title(WIN_TITLE)

    # set the background.
    root.configure(bg=WIN_BG)

    # make the window un-resizable.
    root.resizable(False, False)

    # set the size of our window and also the start position.
    root.geometry(f"{WIN_WIDTH}x{WIN_HEIGHT}")

    # create calculator screen variables.
    # and those are input, and output(result).
    input_var = tkinter.StringVar()
    result_var = tkinter.StringVar()

    # make sure to initialize those vars.
    input_var.set("")
    result_var.set("")

    start_app(root)


def print_symbol_to_screen(symbol: str, screen_var: tkinter.StringVar):
    """print user input to the calculator screen."""

    # first we have to get what is on the screen.
    # and we can do that by getting what is inside,
    # the screen_var.
    temp_var = screen_var.get()

    screen_var.set(temp_var + str(symbol))


def eql_btn_command(screen_var: tkinter.StringVar, result_var: tkinter.StringVar):
    """calculate the user input and set it,
    to the result var."""

    # get the user input.
    user_input = screen_var.get()

    # Guard-Condition.
    if "÷0" in user_input:
        # make sure the user is not divide on zero.
        result_var.set("Error")
        return None

    # now replace all special vars with normal ones.
    user_input = user_input.replace("÷", "/").replace("x", "*")

    # now calculate the result,
    # and make sure to convert-it to string.
    result = str(eval(user_input))

    # now make sure to remove useless zero's.
    if result.endswith(".0"):
        # now remove the last two digits including '.' and '0'.
        result = result[:-2]

    # now set the result to the result_screen_var.
    result_var.set(result)


def clear_screen_btn_command(screen_var: tkinter.StringVar, result_var: tkinter.StringVar):
    """wipe the result screen and the input screen."""

    screen_var.set("")
    result_var.set("")


def clear_last_digit_btn_command(screen_var: tkinter.StringVar, result_var: tkinter.StringVar):
    """remove the last digit from the user input."""

    temp_screen_var = screen_var.get()

    new_screen_var = temp_screen_var[:-1]

    screen_var.set(new_screen_var)


def main():
    main_window()


if __name__ == "__main__":
    main()

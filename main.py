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
CLEAR_BTN_STYLE = {
    "font": ("calibre", 14, "bold"),
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


def print_symbol_to_screen(screen_var: tkinter.StringVar, symbol: str):
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

    # create the buttons.
    btn0 = tkinter.Button(
        root, text='0', command=lambda: print_symbol_to_screen(input_var, '0'), **BTN_STYLE)

    btn1 = tkinter.Button(
        root, text='1', command=lambda: print_symbol_to_screen(input_var, '1'), **BTN_STYLE)

    btn2 = tkinter.Button(
        root, text='2', command=lambda: print_symbol_to_screen(input_var, '2'), **BTN_STYLE)

    btn3 = tkinter.Button(
        root, text='3', command=lambda: print_symbol_to_screen(input_var, '3'), **BTN_STYLE)

    btn4 = tkinter.Button(
        root, text='4', command=lambda: print_symbol_to_screen(input_var, '4'), **BTN_STYLE)

    btn5 = tkinter.Button(
        root, text='5', command=lambda: print_symbol_to_screen(input_var, '5'), **BTN_STYLE)

    btn6 = tkinter.Button(
        root, text='6', command=lambda: print_symbol_to_screen(input_var, '6'), **BTN_STYLE)

    btn7 = tkinter.Button(
        root, text='7', command=lambda: print_symbol_to_screen(input_var, '7'), **BTN_STYLE)

    btn8 = tkinter.Button(
        root, text='8', command=lambda: print_symbol_to_screen(input_var, '8'), **BTN_STYLE)

    btn9 = tkinter.Button(
        root, text='9', command=lambda: print_symbol_to_screen(input_var, '9'), **BTN_STYLE)

    # place the number buttons.
    btn0.place(x=85, y=343)
    btn1.place(x=0, y=288)
    btn2.place(x=85, y=288)
    btn3.place(x=170, y=288)
    btn4.place(x=0, y=232)
    btn5.place(x=85, y=232)
    btn6.place(x=170, y=232)
    btn7.place(x=0, y=176)
    btn8.place(x=85, y=176)
    btn9.place(x=170, y=176)

    # create operations buttons.
    add_btn = tkinter.Button(
        root, text='+', command=lambda: print_symbol_to_screen(input_var, '+'), **BTN_STYLE)

    sub_btn = tkinter.Button(
        root, text='-', command=lambda: print_symbol_to_screen(input_var, '-'), **BTN_STYLE)

    mul_btn = tkinter.Button(
        root, text='x', command=lambda: print_symbol_to_screen(input_var, 'x'), **BTN_STYLE)

    div_btn = tkinter.Button(
        root, text='÷', command=lambda: print_symbol_to_screen(input_var, '÷'), **BTN_STYLE)

    dot_btn = tkinter.Button(
        root, text='.', command=lambda: print_symbol_to_screen(input_var, '.'), **BTN_STYLE)

    eql_btn = tkinter.Button(root, text="=", command=lambda: eql_btn_command(
        input_var, result_var), **BTN_STYLE)

    # place operations buttons.
    mul_btn.place(x=255, y=176)
    sub_btn.place(x=255, y=232)
    add_btn.place(x=255, y=288)
    div_btn.place(x=255, y=343)
    dot_btn.place(x=0, y=343)
    eql_btn.place(x=170, y=343)

    # create clear buttons.

    clear_screen_btn = tkinter.Button(
        root, text="AC", command=lambda: clear_screen_btn_command(input_var, result_var),
        width=13, **CLEAR_BTN_STYLE)

    clear_last_digit_btn = tkinter.Button(
        root, text='C', command=lambda: clear_last_digit_btn_command(input_var, result_var),
        width=11, **CLEAR_BTN_STYLE)

    # now place clear buttons.
    clear_screen_btn.place(x=0, y=398)
    clear_last_digit_btn.place(x=177, y=398)

    # create labels for showing the user input and result,
    # simply-out screen-labels.

    screen_label = tkinter.Label(
        root, textvariable=input_var,  font=(WIDGETS_FONT, 14, "bold"),
        width=30, height=4, anchor='nw', **LABEL_STYLE)

    result_label = tkinter.Label(
        root, textvariable=result_var,  font=(WIDGETS_FONT, 22, "bold"),
        width=17, height=2, anchor='se', **LABEL_STYLE)

    # place screen labels.
    screen_label.place(x=0, y=5)
    result_label.place(x=0, y=50)

    start_app(root)


def main():
    main_window()


if __name__ == "__main__":
    main()

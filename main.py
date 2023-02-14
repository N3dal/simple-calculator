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

# TODO:
# [1]- add click effect on calc buttons, for example:
# when you click on the number 2 the color will change to,
# darkorange, and when you release the color will back to,
# the default color for our case is gray.


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
        # for *nix machines.
        system("clear")

    elif OS_NAME == "windows":
        system("cls")

    else:
        # for all other os in the world.
        # system("your-command")
        pass


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

    return lambda: print_symbol_to_screen(screen_var, symbol)


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


def button_click_event(button: tkinter.Button):
    """
        when we click on any button;

        return None;
    """
    button.configure(background="darkorange", activebackground="darkorange")

    return None


def button_release_event(button: tkinter.Button):
    """
        release event on any button;

        return None;
    """
    button.configure(background="gray22", activebackground="gray28")

    return None


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
    btns = [tkinter.Button(
            root, text=char, command=print_symbol_to_screen(input_var, char), **BTN_STYLE) for char in "0123456789+-x÷."]

    eql_btn = tkinter.Button(root, text="=", command=lambda: eql_btn_command(
        input_var, result_var), **BTN_STYLE)

    clear_screen_btn = tkinter.Button(
        root, text="AC", command=lambda: clear_screen_btn_command(input_var, result_var),
        width=13, **CLEAR_BTN_STYLE)

    clear_last_digit_btn = tkinter.Button(
        root, text='C', command=lambda: clear_last_digit_btn_command(input_var, result_var),
        width=11, **CLEAR_BTN_STYLE)

    def bind_button_with_event(button, func):
        """"""
        return lambda e: func(button)

    for btn in btns:

        btn.bind("<Button-1>", bind_button_with_event(btn, button_click_event))
        btn.bind("<ButtonRelease-1>",
                 bind_button_with_event(btn, button_release_event))

    # place the number buttons.
    btns[0].place(x=85, y=343)
    btns[1].place(x=0, y=288)
    btns[2].place(x=85, y=288)
    btns[3].place(x=170, y=288)
    btns[4].place(x=0, y=232)
    btns[5].place(x=85, y=232)
    btns[6].place(x=170, y=232)
    btns[7].place(x=0, y=176)
    btns[8].place(x=85, y=176)
    btns[9].place(x=170, y=176)

    # place operations buttons.
    btns[12].place(x=255, y=176)
    btns[11].place(x=255, y=232)
    btns[10].place(x=255, y=288)
    btns[13].place(x=255, y=343)
    btns[14].place(x=0, y=343)
    eql_btn.place(x=170, y=343)

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

    clear_screen_btn_command(input_var, result_var)

    start_app(root)


def main():
    main_window()


if __name__ == "__main__":
    main()

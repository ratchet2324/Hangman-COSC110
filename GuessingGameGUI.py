#!/usr/bin/env python3

from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import random
import time
import platform

attempts = 10
guesses = []
word = ""


def loadfile(filename):
    # Function opens a file, then reads each line and puts it into a list to be chosen later.
    word_list = []
    game_window["state"] = "normal"
    file = open(filename)
    # Tries to open the file. If successful, prints it was able to be loaded,
    # otherwise says it cant find it and exits the program after displaying the error and waiting.
    try:
        game_window.insert("end", "Word list loaded. . .")
        for line in file.readlines():
            word_list.append(line.strip().lower())
        file.close()
    except IOError:
        messagebox.showerror("File not found!", "Oops. File not found")
        time.sleep(3)
        exit()
    game_window["state"] = "disabled"
    return word_list


def new_game(event=None):
    global attempts
    global guesses
    global word
    attempts = 10
    guesses = []
    word = ""
    attempts_var.set("Attempts \nremaining: \n" + str(attempts))
    attempts_label.grid(row=0, column=5, sticky=EW)
    game_window["state"] = "normal"
    game_window.delete(1.0, "end")
    game_window["state"] = "disabled"
    game_window["state"] = "normal"
    word = select_word()
    hints(word)
    game_window["state"] = "disabled"
    reset_buttons()
    return word

#Not working - needs to reset the buttons upon resetting the game.
def reset_buttons():
    for child in main_window.winfo_children():
        if child.winfo_class() == 'button':
            print(child)
            print("resetting")
            child["state"] = "enabled"
        else:
            print(child, "is not button")


#Not working - needs to disable the buttons upon reaching 0 attempts.
def disable_buttons():
    for child in main_window.winfo_children():
        if child.winfo_class() == 'button':
            print(child)
            print("disabling")
            child["state"] = "disabled"
        else:
            print(child, "is not button")


def about_me(event=None):
    # Displays a help box, for any errors.
    messagebox.showinfo("About Me", message="This is a variation of the game 'Hangman', created using Python 3."
                                            "\nIf you have a problem using this program, please report it to the author"
                                            ", including your system specs found below.\n"
                                            "\nThe author is Cordel Murphy."
                                            "\n\nSystem: {0} {1}".format(platform.system(), platform.release()) +
                                            "\n\nSystem Version: {0}".format(platform.version()) +
                                            "\n\nSystem Architecture: {0}".format(platform.architecture()) +
                                            "\n\nPython Version: {0}".format(platform.python_version()))


def select_word():
    # Selects the word to be used
    global word
    word_list = loadfile("words.txt")
    word = random.choice(word_list)
    game_window["state"] = "normal"
    game_window.insert("end", "\nThe word is: " + word + "\n")
    game_window["state"] = "disabled"
    return word


def change_attempts():
    # Changes the attempts upon buttons being pressed
    global attempts
    print("Attempts =", attempts)
    attempts -= 1
    print("New attempts =", attempts)
    attempts_var.set("Attempts \nremaining: \n" + str(attempts))
    attempts_label.grid(row=0, column=5, sticky=EW)
    return attempts


def hints(word):
    game_window["state"] = "normal"
    # reads in the chosen word and creates the clue from it. Once a guess is made, it checks if it is in the word
    # if it is, then it appends the hint to show the letters in the right space. At the end it prints out the current hint.
    secret_word = ""
    for letter in word:
        if letter not in guesses:
            secret_word += "_"
        else:
            secret_word += letter
    game_window.insert("end", "\nThe current hint is:\n" + secret_word + "\n")
    game_window["state"] = "disabled"
    return secret_word


def occurrences(word, letters):
    # counts how many times the letter occurs in the word
    guess = letters
    times_in_word = 0
    for letter in word:
        if guess == letter:
            times_in_word += 1
    return times_in_word


def handle_button(button, letters):
    # when the buttons are clicked, this function checks the letter selected and runs the corresponding functions and
    # disabled the button so it cannot be used again.
    global guesses
    global word
    button["state"] = "disabled"
    game_window["state"] = "normal"
    guesses.append(letters)
    print(letters)
    times_in_word = occurrences(word, letters)
    print(times_in_word)
    game_window.insert("end", "\nThe letter occurs " + str(times_in_word) + "time(s).\n")
    secret_word = hints(word)
    game_window["state"] = "disabled"
    change_attempts()
    if secret_word == word:
        game_window["state"] = "normal"
        game_window.insert("end", "Congratulations! You have correctly guesses the word!!")
        game_window["state"] = "disabled"
        play_again()
    else:
        pass


def play_again():
    # Asks the user if they would like to play again.
    ask = messagebox.askyesno("Play Again?", "Would you like to play again?")
    print(ask)
    if 'True':
        new_game()
    elif 'False':
        messagebox.showinfo("Thanks.", "Thank you for playing Hangman!!")
        exit()


# Sets commands for the buttons when clicked.
def selected_a(event=NONE):
    handle_button(letter_a, "a")


def selected_b(event=NONE):
    handle_button(letter_b, "b")


def selected_c(event=NONE):
    handle_button(letter_c, "c")


def selected_d(event=NONE):
    handle_button(letter_d, "d")


def selected_e(event=NONE):
    handle_button(letter_e, "e")


def selected_f(event=NONE):
    handle_button(letter_f, "f")


def selected_g(event=NONE):
    handle_button(letter_g, "g")


def selected_h(event=NONE):
    handle_button(letter_h, "h")


def selected_i(event=NONE):
    handle_button(letter_i, "i")


def selected_j(event=NONE):
    handle_button(letter_j, "j")


def selected_k(event=NONE):
    handle_button(letter_k, "k")


def selected_l(event=NONE):
    handle_button(letter_l, "l")


def selected_m(event=NONE):
    handle_button(letter_m, "m")


def selected_n(event=NONE):
    handle_button(letter_n, "n")


def selected_o(event=NONE):
    handle_button(letter_o, "o")


def selected_p(event=NONE):
    handle_button(letter_p, "p")


def selected_q(event=NONE):
    handle_button(letter_q, "q")


def selected_r(event=NONE):
    handle_button(letter_r, "r")


def selected_s(event=NONE):
    handle_button(letter_s, "s")


def selected_t(event=NONE):
    handle_button(letter_t, "t")


def selected_u(event=NONE):
    handle_button(letter_u, "u")


def selected_v(event=NONE):
    handle_button(letter_v, "v")


def selected_w(event=NONE):
    handle_button(letter_w, "w")


def selected_x(event=NONE):
    handle_button(letter_x, "x")


def selected_y(event=NONE):
    handle_button(letter_y, "y")


def selected_z(event=NONE):
    handle_button(letter_z, "z")


# Sets up the base
base = Tk()
base.title('Hangman')
main_window = ttk.Frame(base, padding='3 3 12 12')
attempts_var = StringVar()
attempts_var.set("Attempts \nremaining: \n" + str(attempts))

# Sets up widgets
game_window = Text(main_window, width=50, height=15)
game_scroll = ttk.Scrollbar(main_window, orient=VERTICAL, command=game_window.yview)
game_window["yscrollcommand"] = game_scroll.set
game_window["state"] = "disabled"
attempts_label = ttk.Label(main_window, textvariable=attempts_var)

# Creates buttons for letters.
letter_a = ttk.Button(main_window, text="A", command=selected_a)
letter_b = ttk.Button(main_window, text="B", command=selected_b)
letter_c = ttk.Button(main_window, text="C", command=selected_c)
letter_d = ttk.Button(main_window, text="D", command=selected_d)
letter_e = ttk.Button(main_window, text="E", command=selected_e)
letter_f = ttk.Button(main_window, text="F", command=selected_f)
letter_g = ttk.Button(main_window, text="G", command=selected_g)
letter_h = ttk.Button(main_window, text="H", command=selected_h)
letter_i = ttk.Button(main_window, text="I", command=selected_i)
letter_j = ttk.Button(main_window, text="J", command=selected_j)
letter_k = ttk.Button(main_window, text="K", command=selected_k)
letter_l = ttk.Button(main_window, text="L", command=selected_l)
letter_m = ttk.Button(main_window, text="M", command=selected_m)
letter_n = ttk.Button(main_window, text="N", command=selected_n)
letter_o = ttk.Button(main_window, text="O", command=selected_o)
letter_p = ttk.Button(main_window, text="P", command=selected_p)
letter_q = ttk.Button(main_window, text="Q", command=selected_q)
letter_r = ttk.Button(main_window, text="R", command=selected_r)
letter_s = ttk.Button(main_window, text="S", command=selected_s)
letter_t = ttk.Button(main_window, text="T", command=selected_t)
letter_u = ttk.Button(main_window, text="U", command=selected_u)
letter_v = ttk.Button(main_window, text="V", command=selected_v)
letter_w = ttk.Button(main_window, text="W", command=selected_w)
letter_x = ttk.Button(main_window, text="X", command=selected_x)
letter_y = ttk.Button(main_window, text="Y", command=selected_y)
letter_z = ttk.Button(main_window, text="Z", command=selected_z)

# Creates a menu bar
top_menu = Menu(main_window)
top_menu.config()
base.config(menu=top_menu)
File = Menu(top_menu)
File.add_command(label='New Game', command=new_game)
File.add_command(label='Exit', command=exit)
Help = Menu(top_menu)
Help.add_command(label='About Me', command=about_me)
top_menu.add_cascade(label='File', menu=File)
top_menu.add_cascade(label='Help', menu=Help)

# Sets up the grid and configures it.
main_window.grid(column=0, row=0, sticky=(N, S, W, E))
game_window.grid(row=0, column=0, columnspan=4, sticky=(N, S, W, E))
game_scroll.grid(row=0, column=4, sticky=(N, S, W))
attempts_label.grid(row=0, column=5, sticky=EW)

base.grid_columnconfigure(0, weight=1)
base.grid_rowconfigure(0, weight=1)

main_window.grid_columnconfigure(0, weight=1)
main_window.grid_columnconfigure(1, weight=1)
main_window.grid_columnconfigure(2, weight=1)
main_window.grid_columnconfigure(3, weight=1)
main_window.grid_columnconfigure(4, weight=1)
main_window.grid_rowconfigure(0, weight=1)
main_window.grid_rowconfigure(1, weight=1)
main_window.grid_rowconfigure(2, weight=1)
main_window.grid_rowconfigure(3, weight=1)
main_window.grid_rowconfigure(4, weight=1)
main_window.grid_rowconfigure(5, weight=1)
main_window.grid_rowconfigure(6, weight=1)
main_window.grid_rowconfigure(7, weight=1)
main_window.grid_rowconfigure(8, weight=1)

# Grid for letters
letter_a.grid(row=2, column=0)
letter_b.grid(row=2, column=1)
letter_c.grid(row=2, column=2)
letter_d.grid(row=2, column=3)
letter_e.grid(row=3, column=0)
letter_f.grid(row=3, column=1)
letter_g.grid(row=3, column=2)
letter_h.grid(row=3, column=3)
letter_i.grid(row=4, column=0)
letter_j.grid(row=4, column=1)
letter_k.grid(row=4, column=2)
letter_l.grid(row=4, column=3)
letter_m.grid(row=5, column=0)
letter_n.grid(row=5, column=1)
letter_o.grid(row=5, column=2)
letter_p.grid(row=5, column=3)
letter_q.grid(row=6, column=0)
letter_r.grid(row=6, column=1)
letter_s.grid(row=6, column=2)
letter_t.grid(row=6, column=3)
letter_u.grid(row=7, column=0)
letter_v.grid(row=7, column=1)
letter_w.grid(row=7, column=2)
letter_x.grid(row=7, column=3)
letter_y.grid(row=8, column=1)
letter_z.grid(row=8, column=2)

new_game()

base.bind('<Control-n>', new_game)
base.bind('<Control-q>', exit)
base.bind('<F1>', about_me)
base.mainloop()

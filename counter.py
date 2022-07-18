# Author: Tom Naccarato (tcarlnaccarato@gmail.com)
#
# counter.py (c) 2022
#
# Description:  A simple counter app to practice UI with tkinter in python.
#
# Created:  01/07/2022, 16:52:02
#
# Modified: 01/07/2022, 16:52:49
# ------------------------------------------------------------------------------
# Imported Libraries
# ------------------------------------------------------------------------------
import tkinter as tk
from tkinter import ttk
# ------------------------------------------------------------------------------
# Defining Classes and Functions
# ------------------------------------------------------------------------------


def button_clicked():
    ''' Adds to the counter when button is clicked'''
    root.click_counter += 1
    message['text'] = f"You have clicked me {root.click_counter} times!"

# ------------------------------------------------------------------------------


root = tk.Tk()

# Defines click counter
root.click_counter = 0

# Adds a title to the window
root.title("Counter App")

# Changes the size of the window
window_width = 300
window_height = 200
# Gets the screen dimensions
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
# Finds centre point of screen
center_x = int(screen_width/2 - window_width/2)
center_y = int(screen_height/2 - window_height/2)
# Sets window position to centre of screen
root.geometry(f"{window_width}x{window_height}+{center_x}+{center_y}")


# Adds a message to the window
message = ttk.Label(root)
message['text'] = "Button has not been clicked yet!"
message.pack()

# Creates a button widget
button = ttk.Button(root, text="Click Me", command=button_clicked)
button.pack()

root.mainloop()

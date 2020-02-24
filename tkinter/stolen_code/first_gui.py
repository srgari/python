#==================
# imports
# =================

import tkinter as tk
from tkinter import ttk
import numpy as np

# Create instance
win = tk.Tk()

# Add a title
win.title("Python GUI")


# Modified Button click function
def click_me():
    action.configure(text = 'Hello, ' + name.get())


# Changing our label
ttk.Label(win, text = "Enter a name:").grid(column=0,row=0)

# Adding a Text box Entry widget
name = tk.StringVar()
name_entered = ttk.Entry(win, width = 12, textvariable = name)
name_entered.grid(column=0,row=1)

# Adding a button
action = ttk.Button(win, text = "Click me!", width = 15, command = click_me)
# action.configure(state = 'disabled') # Disable the Button Widget
action.grid(column = 2, row = 1)

name_entered.focus() # Place cursor into name Entry

ttk.Label(win, text = "Choose a number:").grid(column = 1, row = 0)
number = tk.StringVar()
number_chosen = ttk.Combobox(win, width = 12, textvariable = number)
number_chosen['values'] = (1,2,4,42,100)
number_chosen.grid(column=1, row = 1)
number_chosen.current(0)



#====================
# Start GUI
#====================
win.mainloop()
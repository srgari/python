import tkinter as tk
from tkinter import ttk

w = tk.Tk()
w.title('Messy Sergio')

def click_me():
    action.configure(text = 'hello, ' + name.get() + '  ' + number_chosen.get())

# adding a textbox entry widget
name = tk.StringVar()
name_entered = ttk.Entry(w, width = 12, textvariable = name)
name_entered.pack()

# adding a button
action = ttk.Button(w, text = 'click me!', command = click_me)
action.pack()

ttk.Label(w, text = 'choose a number:').pack()

number = tk.StringVar()
number_chosen = ttk.Combobox(w, width = 12,
                            textvariable = number,
                            state = 'readonly')

number_chosen['values'] = (1,2,3,4,5,100)

number_chosen.current(0)
number_chosen.pack()

w.mainloop()


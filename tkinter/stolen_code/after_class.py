import tkinter as tk
from tkinter import ttk

class OOP():

    def click_me(self):
        self.action.configure(text = 'Hello, ' + self.name.get()\
             + ' ' + self.number_chosen.get())


    def create_widgets(self):
        # adding a textbox entry widget
        self.name = tk.StringVar()
        name_entered = ttk.Entry(self.w, width = 12, textvariable = self.name)
        name_entered.pack()

        # adding a button
        self.action = ttk.Button(self.w, text = 'click me!', command = self.click_me)
        self.action.pack()

        self.number = tk.StringVar()
        self.number_chosen = ttk.Combobox(self.w, width = 12,
                            textvariable = self.number,
                            state = 'readonly')
        self.number_chosen['values'] = (2,4,6,8,200)
        self.number_chosen.current(0)
        self.number_chosen.pack()
        
    def __init__(self):
        self.w = tk.Tk() # just add self. before w
        self.w.title('Classy Sergio')
        self.create_widgets()



        
        
    
oop = OOP()
oop.w.mainloop()

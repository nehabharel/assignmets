# -*- coding: utf-8 -*-
"""
Created on Tue Sep 24 23:06:16 2024

@author: khann
"""

import tkinter as tk

primary = [
    'option 1',
    'option 2',
    'option 3',
    'option 4'
    ]

options1 = [
    'option 1.1',
    'option 1.2',
    'option 1.3',
    'option 1.4'
    ]
options2 = [
    'option 2.1',
    'option 2.2',
    'option 2.3',
    'option 2.4'
    ]

secondary = options1


root = tk.Tk()
root.geometry('400x200')


primDD = tk.StringVar()
primDD.set(primary[0])
primOpt = tk.OptionMenu(root, primDD, *primary)


if primDD.get() == 'options 1':
    secondary = options1
elif primDD.get() == 'options 2':
    secondary = options2


secDD = tk.StringVar()
secDD.set(secondary[0])
secOpt = tk.OptionMenu(root, secDD, *secondary)


primOpt.config(width=20)
secOpt.config(width=30)
primOpt.grid(row=0, column=0, padx=1.25, pady=1.25)
secOpt.grid(row=0, column=1, padx=1.25, pady=1.25)
root.mainloop()

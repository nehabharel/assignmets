# -*- coding: utf-8 -*-
"""
Created on Tue Sep 24 18:29:47 2024

@author: khann
"""


from tkinter import *


root = Tk()


root.title("Welcome to Python class")

root.geometry('500x500')

lbl = Label(root, text = "Are you new to Python?")
lbl.grid()


def clicked():
    lbl.configure(text = "I just got selected")


btn = Button(root, text = "select" ,
             fg = "blue", command=clicked)

btn.grid(column=1, row=0)


root.mainloop()

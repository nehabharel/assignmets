# -*- coding: utf-8 -*-
"""
Created on Thu Sep 19 19:29:26 2024

@author: Neha
"""

#Assignment1:Create the logs of books and their details using object oriented programming


class book:
    def __init__(self,name,author,publisher,price): 
        self.book_name=name
        self.book_author=author
        self.book_publisher=publisher
        self.book_price=price

    def add_books(self):
        print("Name: " +self.book_name) 
        print("author: " +self.book_author) 
        print("publisher: " +self.book_publisher) 
        print('price: ' +str(self.book_price)) 
        print("book added")

book1=book("hidden hindu","XYZ","ABC publication","33")
book1.add_books() 


book2=book("laughter","Neha","DEF publication","45")
book2.add_books() 





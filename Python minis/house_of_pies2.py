# -*- coding: utf-8 -*-
"""
Created on Sun Oct 18 16:41:58 2020

@author: awsal
"""

shopping = "y"

pie_purchases = []

pie_list = ["Pecan", "Apple Crisp", "Bean", "Banoffee", "Black Bun", "Blueberry", "Buko", "Burek", "Tamale", "Steak"]

print("Welcome to House of Pies! Here is our selection:")

while shopping == "y":
    print("1) Pecan, 2) Apple Crisp, 3) Bean, 4) Banoffee, 5) Black Bun, 6) Blueberry, 7) Buko, 8) Burek, 9) Tamale, 10) Steak")
    
    pie_choice = input("Which pie would you like? ")
    
    pie_purchases.append(pie_choice)
    
    print("Great! We'll have that " + pie_list[int(pie_choice) - 1] + " pie right out for you.")
    
    shopping = input("Would you like to make another purchase: (y)es or (n)o? ")
    
print("You purchased a total of " + str(len(pie_purchases)) + " pies.")
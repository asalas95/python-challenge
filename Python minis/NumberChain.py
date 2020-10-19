# -*- coding: utf-8 -*-
"""
Created on Fri Oct 16 14:22:12 2020

@author: awsal
"""

user_play = "y"

while user_play == "y":

    user_number = int(input("How many numbers? "))
    
    for x in range(user_number):
    
        print(x)
        
    user_play = input("Continue: (y)es or (n)o? ")
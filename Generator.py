#python generators are functions that return the
#transversal object and used to create iterators


#How to create generator in python
#use def to define and yield to return

#successive function call using fo#!/usr/bin/python3
def fizzbuzz():
    for i in range(1, 101):
        if i % 15 == 0:
            print("FizzBuzz ", end="")
        elif i % 5 == 0:
            print("Buzz ", end="")
        elif i % 3 == 0:
            print("Fizz ", end="")
        else:
            print("{:d} ".format(i), end="")

import sys

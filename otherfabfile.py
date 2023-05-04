#!/usr/bin/env python3

# Define function
@task
def message(c):
   # Take a name from the user
   name = input('Enter your name : ')
   # Print the name with greeting
   print('Hello, %s' %name)

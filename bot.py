"""
I want this to be randomized but I haven't quite figured out how.
The goal is to have a female or male bot who gets a randomized name and age (between 18 - 39) everytime the code is executed.
"""

import random

name = input("Hey there.  What's your name? ")
print("Nice to meetchya," ,name)


yes = ['Yes', 'yes']
no = ['No', 'no']
initiate = input("Is there anything you'd like to ask me? ")
if initiate is yes:
  print("Okay then.  Ask away!")
if initiate is no:
    print("Oh. Okay.")
    
    
    
"""    
def config():
  # Bot configuration
  name: 'Jamie'
  age: '34'
  gender: 'female'
"""

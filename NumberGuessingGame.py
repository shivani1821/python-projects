#!/usr/bin/env python
# coding: utf-8

# In[3]:


import random

#generating the random value 
random_num =random.randint(1,100)

#defining the evaluating guess process
for chances in range(8):
    #taking the input from the user
    user_input =int(input("Enter the guess number between 1-100 : "))
    
    if(user_input < random_num):
        print("Too low")
    elif(user_input > random_num):
        print("Too high")
    else:
        print("guessed correctly")
        break


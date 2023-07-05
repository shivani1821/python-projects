#!/usr/bin/env python
# coding: utf-8

# In[11]:


from spellchecker import SpellChecker

correcter =SpellChecker()

inputs =input("Enter the word: ")
if inputs in correcter:
    print("Correct : " , correcter)
else:
    print("Correction : " , correcter.correction(inputs))


# In[ ]:





#!/usr/bin/env python
# coding: utf-8

# In[15]:


#Anagram
# Word or phrase formed by rearranging the letters of a different word or phrase

from collections import defaultdict

def group_anagrams(a):
    #creating defaultdict because simple dict gives keyerror as key not available
    def_dict = defaultdict(list)
    
    for i in a:
        # sorted cretes an array of letters so we have to make it as a string
        sorted_i = "".join(sorted(i))
        # clubbing the words with same letters together 
        def_dict[sorted_i].append(i)
    return def_dict.values()

lists=["angel" , "glean" , "listen" , "silent" ,"ate" ,"arc" ,"car"]
group_anagrams(lists)


# In[ ]:





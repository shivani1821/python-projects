#!/usr/bin/env python
# coding: utf-8

# In[1]:


def findMissingNum(arr):
    nums=set(arr)
    output=[]
    for i in range(1,arr[-1]):
        if i not in nums:
            output.append(i)
    return output

a =[1,3,4,5,6,7,9,10,22]

findMissingNum(a)


# In[ ]:





# In[ ]:





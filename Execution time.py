#!/usr/bin/env python
# coding: utf-8

# In[2]:


from time import time

start =time()
sentence ="Did you know that English is a West Germanic language that was first spoken in early medieval England and is now the global lingua franca? \
Almost everyone wishes to learn this language to its perfection, and many have the privilege of learning it through their environment."
words =sentence.split()

for word in words:
    print(word.lower())

end =time()
print("Execution time: " ,end -start)


# In[ ]:





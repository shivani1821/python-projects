#!/usr/bin/env python
# coding: utf-8

# In[15]:


#find the mean of given array values
def mean(arr):
    avg =sum(arr)/len(arr)
    return avg

##find the median of given array values
def median(arr):
    leng =len(arr)
    arr.sort()
    if leng%2 == 0:
        med = (arr[leng//2] +arr[(leng+1)//2])/2
    else:
        med = arr[(leng+1)//2]
    return med

def mode(arr):
    frequency = {}
    for i in arr:
        if i not in frequency:
            frequency[i] = 1
        else:
            frequency[i] += 1
    return max(frequency , key = frequency.get)

a =[1,3,7,8,7,4,5,6,7,7,9,9,9,8,8,8,9,10,22]

print("Mean" ,mean(a))
print("Median" ,median(a))
print("Mode" ,mode(a))


# In[ ]:





# In[ ]:





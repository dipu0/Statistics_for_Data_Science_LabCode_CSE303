#!/usr/bin/env python
# coding: utf-8

# In[2]:


# Mean function for problem 4
def mean(x):
    total = 0
    count = 0
    for i in x:
        total= total+i
        count=count+1
    own_mean = total/count
    return own_mean


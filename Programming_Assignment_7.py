#!/usr/bin/env python
# coding: utf-8

# # Programming_Assignment-7

# In[ ]:





# In[ ]:


get_ipython().set_next_input('1.Write a Python Program to find sum of array');get_ipython().run_line_magic('pinfo', 'array')
Ans:


# In[1]:


def Sum(n):
    arr=[]
    sum=0
    for i in range(n):
        ele = int(input(n))
        arr.append(ele)
    for i in range(n):
        sum= sum+arr[i]
    return sum
        


# In[ ]:





# In[ ]:


get_ipython().set_next_input('2.Write a Python Program to find largest element in an array');get_ipython().run_line_magic('pinfo', 'array')
Ans:


# In[2]:


import math


# In[3]:


def largestSum(n):
    arr=[]
    num=arr[0]
    for i in range(n):
        ele = int(input(n))
        arr.append(ele)
    for i in range(n):
        if arr[i]>max:
            max=arr[i]
    return max


# In[ ]:





# In[ ]:


get_ipython().set_next_input('3.Write a Python Program for array rotation');get_ipython().run_line_magic('pinfo', 'rotation')
Ans:


# In[4]:


def rotation(a,d):
    temp = []
    n=len(a)
    for i in range(d,n):
        temp.append(a[i])
    i = 0
    for i in range (0,d):
        temp.append(a[i])
    a=temp.copy()
    return a


# In[ ]:





# In[ ]:


get_ipython().set_next_input('4.Write a Python Program to Split the array and add the first part to the end');get_ipython().run_line_magic('pinfo', 'end')
Ans:


# In[ ]:


def arraySplit(arr, n, k):
    for i in range(0, k):
        x = arr[0]
        for j in range(0, n-1):
            arr[j] = arr[j + 1]
        arr[n-1] = x
arr = [15, 40, 15, 16, 50, 36]
n = len(arr)
position = 2
SplitArray(arr, n, position)
for i in range(0, n):
    print(arr[i], end = ' ')


# In[ ]:





# In[ ]:


get_ipython().set_next_input('5.Write a Python Program to check if given array is Monotonic');get_ipython().run_line_magic('pinfo', 'Monotonic')
Ans:


# In[ ]:


def ismonotone(a):
    n=len(a) 
    if n==1:
        return True
    else:
        if all(a[i]>=a[i+1] for i in range(0,n-1) or a[i]<=a[i+1] for i in range(0,n-1)):
            return True
        else:
            return False


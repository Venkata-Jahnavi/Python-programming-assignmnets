#!/usr/bin/env python
# coding: utf-8

# # Programming_Assignment-6

# In[ ]:





# In[ ]:


get_ipython().set_next_input('1.Write a Python Program to Display Fibonacci Sequence Using Recursion');get_ipython().run_line_magic('pinfo', 'Recursion')
Ans:


# In[1]:


def fib(n):
    if n<1:
        print('Incorrect Input')
    elif n==0:
        return 0
    elif n==1 or n==2:
        return 1
    else:
        return fib(n-1)+fib(n-2)


# In[ ]:





# In[ ]:


get_ipython().set_next_input('2.Write a Python Program to Find Factorial of Number Using Recursion');get_ipython().run_line_magic('pinfo', 'Recursion')
Ans:


# In[2]:


def fact(n):
    if n==0 or n==1:
        return 1
    else:
        return n*fact(n-1)


# In[ ]:





# In[ ]:


get_ipython().set_next_input('3.Write a Python Program to calculate your Body Mass Index');get_ipython().run_line_magic('pinfo', 'Index')
Ans:


# In[3]:


def BMI():
    height=float(input("Enter height in meter"))
    weight=float(input("Enter weight in kg"))
    BMI=weight/(height)**2
    return BMI


# In[ ]:





# In[ ]:


4.Write a Python Program to calculate the natural logarithm of any number
Ans:    


# In[4]:


import math
def naturalLog(num,base):
    return math.log(num,base)


# In[ ]:





# In[ ]:


5.Write a Python Program for cube sum of first n natural numbers
Ans:


# In[5]:


def cubeofNaturalNumber(n):
    for i in range(1,n+1):
        sum +=i*i*i
        return sum
        


# In[ ]:





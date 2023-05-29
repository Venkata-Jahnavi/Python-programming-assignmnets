#!/usr/bin/env python
# coding: utf-8

# # Programming_Assignment-2

# In[ ]:





# In[ ]:


get_ipython().set_next_input('1.Write a Python program to convert kilometers to miles');get_ipython().run_line_magic('pinfo', 'miles')
Ans:


# In[1]:


def milesKmConverter(km):
    mile = 0.621371
    return km*mile
milesKmConverter(3.5)


# In[ ]:





# In[ ]:


get_ipython().set_next_input('2.Write a Python program to convert Celsius to Fahrenheit');get_ipython().run_line_magic('pinfo', 'Fahrenheit')
Ans:


# In[2]:


def fahrenheit(cel):
    return (cel * 1.8) + 32
    
fahrenheit(90)


# In[ ]:





# In[ ]:


get_ipython().set_next_input('3.Write a Python program to display calendar');get_ipython().run_line_magic('pinfo', 'calendar')
Ans:


# In[3]:


import calendar
def calender(yy,mm):
    print(calendar.month(yy,mm))
 # Note utilizing Calendar module   


# In[4]:


calender(2012,3)


# In[ ]:





# In[ ]:


get_ipython().set_next_input('4.Write a Python program to solve quadratic equation');get_ipython().run_line_magic('pinfo', 'equation')
Ans:


# In[5]:


import cmath
def quadraticEquation(a,b,c):
    d = (b**2) - (4*a*c)
    # Two solution for quadratic equation
    ans1 = (-b-cmath.sqrt(d))/(2*a)
    ans2 = (-b+cmath.sqrt(d))/(2*a)
    print('The solution are{0},{1}'.format(ans1,ans2))


# In[6]:


quadraticEquation(2,4,3)


# In[ ]:





# In[ ]:


get_ipython().set_next_input('5.Write a Python program to swap two variables without temp variable');get_ipython().run_line_magic('pinfo', 'variable')
Ans:


# In[7]:


def swapWithoutTemp(a,b):
    print('Before Swap',a,b)
    a=a+b
    b=a-b
    a=a-b
    print('after swap',a,b)
swapWithoutTemp(2,8)


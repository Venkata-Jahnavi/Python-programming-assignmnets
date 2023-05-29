#!/usr/bin/env python
# coding: utf-8

# # Assignmnet-1

# In[ ]:





# In[ ]:


Write a Python program to print "Hello Python"?
Ans:


# In[6]:


def function1():
    print('Hello Python')
function1()


# In[ ]:





# In[ ]:


2.Write a Python program to do arithmetical operations addition and division.?
Ans:


# In[8]:



def function2(*args):
    #Addition
    add = args[0] + args[1]
    print(add)
    #Division
    div = args[0] / args[1]
    print(div)


# In[9]:


function2(2,3)


# In[ ]:





# In[ ]:


get_ipython().set_next_input('3.Write a Python program to find the area of a triangle');get_ipython().run_line_magic('pinfo', 'triangle')
Ans:


# In[10]:


def function3():
    a = float(input())  
    b = float(input()) 
    c = float(input())  
    # Half perimeter 
    hp = (a + b + c) / 2  
    # calculate the area  
    area = (hp*(hp-a)*(hp-b)*(hp-c)) ** 0.5  
    print(area)


# In[11]:


function3()


# In[ ]:





# In[ ]:


get_ipython().set_next_input('4.Write a Python program to swap two variables');get_ipython().run_line_magic('pinfo', 'variables')
Ans:


# In[15]:


def function4():
    a = float(input())  
    b = float(input()) 
    print('Before swap',a,b)
    temp = a
    a=b
    b=temp
    print('After swap',a,b)
    
function4()


# In[ ]:





# In[ ]:


get_ipython().set_next_input('5.Write a Python program to generate a random number');get_ipython().run_line_magic('pinfo', 'number')
Ans:


# In[17]:


import random as rd
def function5():
    print(rd.randint(0,10))


# In[18]:


function5()


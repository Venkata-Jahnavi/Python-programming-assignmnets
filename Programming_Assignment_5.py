#!/usr/bin/env python
# coding: utf-8

# # Programming_Assignment-5

# In[ ]:





# In[ ]:


get_ipython().set_next_input('1.Write a Python Program to Find LCM');get_ipython().run_line_magic('pinfo', 'LCM')
Ans:


# In[1]:


def compute_lcm(x,y):
    if x>y:
        gr = x
    else:
        gr=y
    while(True):
        if((gr % x == 0) and (gr % y == 0)):
            lcm=gr
            break
        gr+=y
    return lcm


# In[2]:


compute_lcm(4,5)


# In[ ]:





# In[ ]:


get_ipython().set_next_input('2.Write a Python Program to Find HCF');get_ipython().run_line_magic('pinfo', 'HCF')
Ans:


# In[3]:


def compute_HCF(x,y):
    if x>y:
        sm=y
    else:
        sm=x
    for i in range(1,sm+1):
        if((x % i == 0) and (y % i == 0)): 
            hcf =i
    return hcf


# In[5]:


compute_HCF(4,8)


# In[ ]:





# In[ ]:


get_ipython().set_next_input('3.Write a Python Program to Convert Decimal to Binary, Octal and Hexadecimal');get_ipython().run_line_magic('pinfo', 'Hexadecimal')
Ans:


# In[6]:


dec = 344
print(bin(dec))
print(oct(dec))
print(hex(dec))


# In[ ]:





# In[ ]:


get_ipython().set_next_input('4.Write a Python Program To Find ASCII value of a character');get_ipython().run_line_magic('pinfo', 'character')
Ans:


# In[7]:


def printASCCI(ch):
    print(ord(ch))


# In[8]:


printASCCI('a')


# In[ ]:





# In[ ]:


get_ipython().set_next_input('5.Write a Python Program to Make a Simple Calculator with 4 basic mathematical operations');get_ipython().run_line_magic('pinfo', 'operations')
Ans:
   


# In[10]:


def simpleCal(str):
   a=int(input())
   b=int(input())
   if(str == '+'):
       print(a+b)
   elif(str == '-'):
       print(a-b)
   elif(str =='*'):
       print(a*b)
   elif(str == '/'):
       print(a/b)
   


# In[11]:


simpleCal('+')


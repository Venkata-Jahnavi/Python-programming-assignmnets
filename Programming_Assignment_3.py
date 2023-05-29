#!/usr/bin/env python
# coding: utf-8

# # Programming_Assignment-3

# In[ ]:





# In[ ]:


get_ipython().set_next_input('1. Write a Python Program to Check if a Number is Positive, Negative or Zero');get_ipython().run_line_magic('pinfo', 'Zero')
Ans:


# In[1]:


def check(n):
    if(n==0):
        print('Zero')
    if(n<0):
        print('Negative')
    else:
        print('Positive')


# In[2]:


check(5)


# In[ ]:





# In[ ]:


get_ipython().set_next_input('2.Write a Python Program to Check if a Number is Odd or Even');get_ipython().run_line_magic('pinfo', 'Even')
Ans:


# In[3]:


def oddEven(n):
    if(n%2 == 0):
        print('Even')
    else:
        print('Odd')


# In[5]:


oddEven(5)


# In[ ]:





# In[ ]:


get_ipython().set_next_input('3.Write a Python Program to Check Leap Year');get_ipython().run_line_magic('pinfo', 'Year')
Ans:


# In[6]:


def checkLeapYear(n):
    if(n%4 )== 0:
        if(n%100) == 0:
            if(n%400) == 0:
                print('{0}Its a leap Year'.format(n))
            else:
                print('{0}Its not a leap Year'.format(n))
        else:
            print('{0} Its a leap year'.format(n))
    else:
        print('{0} Its not a leap year'.format(n))


# In[7]:


checkLeapYear(2011)


# In[ ]:





# In[ ]:


get_ipython().set_next_input('4.Write a Python Program to Check Prime Number');get_ipython().run_line_magic('pinfo', 'Number')
Ans:


# In[9]:


def primeNumber(n):
    if n > 1:
        for i in range(2, int(n/2)+1):
            if (n % i) == 0:
                print(n, "it is ot a Prime Number")
                break
        else:
            print(n, "It is a prime number")
    else:
        print(n, "It is not a prime number")


# In[10]:


primeNumber(9)


# In[ ]:





# In[ ]:


5.Write a Python Program to Print all Prime Numbers in an Interval of 1-10000?
Ans:


# In[11]:


def checkPrimeInterval():
    lb=1
    ub=10000
    for num in range(lb,ub+1):
        if num >1:
            for i in range(2,num):
                if(num%i)==0:
                    break
            else:
                print(num)


# In[12]:


checkPrimeInterval()


# In[ ]:





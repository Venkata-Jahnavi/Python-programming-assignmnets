#!/usr/bin/env python
# coding: utf-8

# # Programming_Assignment_4

# In[ ]:





# In[ ]:


get_ipython().set_next_input('1.Write a Python Program to Find the Factorial of a Number');get_ipython().run_line_magic('pinfo', 'Number')
Ans:


# In[1]:


def factorial(a):
    if(a == 1):
        return 1
    fact = a*factorial(a-1)
    return fact


# In[3]:


factorial(5)


# In[ ]:





# In[ ]:


get_ipython().set_next_input('2.Write a Python Program to Display the multiplication Table');get_ipython().run_line_magic('pinfo', 'Table')
Ans:


# In[4]:


def table(a):
    for i in range(1, 11):
           print(a, 'x', i, '=', a*i)


# In[5]:


table(10)


# In[ ]:





# In[ ]:


get_ipython().set_next_input('3.Write a Python Program to Print the Fibonacci sequence');get_ipython().run_line_magic('pinfo', 'sequence')
Ans:


# In[6]:


def fibb(a):
    if a<= 0:
        return 0
    if a==1 or a==2:
        return 1
    fib = fibb(a-1)+fibb(a-2)
    return fib
    


# In[7]:


fibb(5)


# In[ ]:





# In[ ]:


get_ipython().set_next_input('4.Write a Python Program to Check Armstrong Number');get_ipython().run_line_magic('pinfo', 'Number')
Ans:


# In[8]:


def armstrong():
    n = int(input("Enter a number: "))
    s = 0
    t = n
    while t > 0:
        digit = t % 10
        s += digit ** 3
        t //= 10
    if n == s:
        print(n,"is an Armstrong number")
    else:
        print(n,"is not an Armstrong number")


# In[9]:


armstrong()


# In[ ]:





# In[ ]:


get_ipython().set_next_input('5.Write a Python Program to Find Armstrong Number in an Interval');get_ipython().run_line_magic('pinfo', 'Interval')
Ans:


# In[10]:


def armstrongInterval():
    lr = int(input("Enter lower range: "))  
    ur = int(input("Enter upper range: "))  
    for num in range(lr,ur+1):
        sum=0
        temp = num
        while temp>0:
            t1 = temp%10
            sum+=t1**3
            temp//=10
            if num == sum:
                print(num)


# In[12]:


armstrongInterval()


# In[ ]:





# In[ ]:


get_ipython().set_next_input('6.Write a Python Program to Find the Sum of Natural Numbers');get_ipython().run_line_magic('pinfo', 'Numbers')
Ans:


# In[13]:


def sumNaturalNumber(num):
    # Sum of natural numbers up to num
    if num<0:
        print('Enter a positive Number')
    else:
        sum =0
        while(num>0):
            sum+=num
            num-=1
            print('Natural number sum is',sum)


# In[14]:


sumNaturalNumber(45)


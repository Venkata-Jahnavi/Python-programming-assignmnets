#!/usr/bin/env python
# coding: utf-8

# # Programming_Assignment-10

# In[ ]:





# In[ ]:


get_ipython().set_next_input('1.Write a Python program to find sum of elements in list');get_ipython().run_line_magic('pinfo', 'list')
Ans:


# In[1]:


def listsum(li):
    i=0
    sum =0
    for i in li:
        sum = sum + i
    return sum


# In[2]:


li = [1,2,3,44,5]
listsum(li)


# In[ ]:





# In[ ]:


get_ipython().set_next_input('2.Write a Python program to Multiply all numbers in the list');get_ipython().run_line_magic('pinfo', 'list')
Ans:


# In[3]:


def listsum(li):
    i=0
    sum =1
    for i in li:
        sum = sum * i
    return sum


# In[4]:


li = [1,2,3,44,5]
listsum(li)


# In[ ]:





# In[ ]:


get_ipython().set_next_input('3.Write a Python program to find smallest number in a list');get_ipython().run_line_magic('pinfo', 'list')
Ans:


# In[5]:


def smallestnum(li):
    li.sort()
    print(li[0])


# In[6]:


li = [88,1,2,3,44,5]
smallestnum(li)


# In[ ]:





# In[ ]:


get_ipython().set_next_input('4.Write a Python program to find largest number in a list');get_ipython().run_line_magic('pinfo', 'list')
Ans:


# In[7]:


def largesttnum(li):
    print(max(li))


# In[8]:


li = [2,3,88,1,2,3,44,5]
largesttnum(li)


# In[ ]:





# In[ ]:


get_ipython().set_next_input('5.Write a Python program to find second largest number in a list');get_ipython().run_line_magic('pinfo', 'list')
Ans:


# In[11]:


def secondlargesttnum(li):
    li.sort()
    print(li[-2])


# In[12]:


li = [2,3,88,1,2,3,44,5]
secondlargesttnum(li)


# In[ ]:





# In[ ]:


get_ipython().set_next_input('6.Write a Python program to find N largest elements from a list');get_ipython().run_line_magic('pinfo', 'list')
Ans:


# In[9]:


def largesttnum(li,n):
    li.sort(reverse=True)
    for i in range(n):
        print(li[i])
    


# In[10]:


li = [2,3,88,1,2,3,44,5]
n=4
largesttnum(li,n)


# In[ ]:





# In[ ]:


get_ipython().set_next_input('7.Write a Python program to print even numbers in a list');get_ipython().run_line_magic('pinfo', 'list')
Ans:


# In[13]:


def even(li):
    for i in li:
        if(i%2 == 0):
            print(i)


# In[14]:


li = [2,3,88,1,2,3,44,5]
even(li)


# In[ ]:





# In[ ]:


get_ipython().set_next_input('8.Write a Python program to print odd numbers in a List');get_ipython().run_line_magic('pinfo', 'List')
Ans:


# In[15]:


def odd(li):
    for i in li:
        if(i%2 != 0):
            print(i)


# In[16]:


li = [2,3,88,1,2,3,44,5]
odd(li)


# In[ ]:





# In[ ]:


get_ipython().set_next_input('9.Write a Python program to Remove empty List from List');get_ipython().run_line_magic('pinfo', 'List')
Ans:


# In[20]:


def removingemptylist():
    test_list = [5, 6, [], 3, [], [], 9]
    print("The original list is : " + str(test_list))
    res = list(filter(None, test_list))
    print ("List after empty list removal : " + str(res))
 


# In[ ]:





# In[ ]:


get_ipython().set_next_input('10.Write a Python program to Cloning or Copying a list');get_ipython().run_line_magic('pinfo', 'list')
Ans:


# In[17]:


def cloning(li):
    licopy = []
    licopy = li
    print(licopy)


# In[19]:


li = [2,3,88,1,2,3,44,5]
cloning(li)


# In[ ]:





# In[ ]:


get_ipython().set_next_input('11.Write a Python program to Count occurrences of an element in a list');get_ipython().run_line_magic('pinfo', 'list')
Ans:


# In[21]:


def countX(lst, x):
    count = 0
    for ele in lst:
        if (ele == x):
            count = count + 1
    return count
 


# In[ ]:





#!/usr/bin/env python
# coding: utf-8

# # Programming_Assignment-8

# In[ ]:





# In[ ]:


get_ipython().set_next_input('1.Write a Python Program to Add Two Matrices');get_ipython().run_line_magic('pinfo', 'Matrices')
Ans:


# In[4]:


def additionOfMatrix():
    a=[[1,2,3],[4,5,6],[7,8,9]]
    b=[[1,2,3],[4,5,6],[7,8,9]]
    sum = [a[i][j]+b[i][j] for j in range(len(a[i])) for i in range(len(a))]
    for r in sum:
        print(r)


# In[ ]:


additionOfMatrix()


# In[ ]:





# In[ ]:


get_ipython().set_next_input('2.Write a Python Program to Multiply Two Matrices');get_ipython().run_line_magic('pinfo', 'Matrices')
Ans:


# In[ ]:


def multiplication():
    a=[[1,2,3],[4,5,6],[7,8,9]]
    b=[[1,2,3],[4,5,6],[7,8,9]]
    for i in range(len(A)):
        for j in range(len(B[0])):
            for k in range(len(B)):
                result[i][j] += A[i][k] * B[k][j]
    for i in result:
        print(i)


# In[ ]:





# In[ ]:


get_ipython().set_next_input('3.Write a Python Program to Transpose a Matrix');get_ipython().run_line_magic('pinfo', 'Matrix')
Ans:


# In[7]:


def transpose():
    a=[[1,2,3],[4,5,6],[7,8,9]]
    result=[[0,0,0],[0,0,0],[0,0,0]]
    for i in range(len(a)):
        for j in range(len(a[i])):
            result[j][i] = a[i][j]
            
    for i in result:
        print(i)


# In[ ]:





# In[ ]:


get_ipython().set_next_input('4.Write a Python Program to Sort Words in Alphabetic Order');get_ipython().run_line_magic('pinfo', 'Order')
Ans:


# In[ ]:


def sort():
    words = input('Enter string')
    list =[for word in words.split()]
    list.sort()
    for p in list:
        print(p)


# In[ ]:





# In[ ]:


get_ipython().set_next_input('5.Write a Python Program to Remove Punctuation From a String');get_ipython().run_line_magic('pinfo', 'String')
Ans:


# In[ ]:


def punchutation():
    punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
    strin = input('Enter input string')
    no_punctuation=''
    for ch in strinf:
        if ch not in punchutations:
            no_punctuation + ch
    return no_punctuation


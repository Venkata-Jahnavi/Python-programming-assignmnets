#!/usr/bin/env python
# coding: utf-8

# # Programming_Assignment_11

# In[ ]:





# In[ ]:


get_ipython().set_next_input('1.Write a Python program to find words which are greater than given length k');get_ipython().run_line_magic('pinfo', 'k')
Ans:


# In[1]:


def stringlength(st,k):
    if(len(st)>k):
        print(st)
    


# In[2]:


stringlength("dsfadfsd",3)


# In[ ]:





# In[ ]:


get_ipython().set_next_input('2.Write a Python program for removing i-th character from a string');get_ipython().run_line_magic('pinfo', 'string')
Ans:


# In[3]:


def remove(string,i):
    a = string[:i]
    b = string[i+1:]
    return a+b

def finalString(st,k):
    print(remove(st,k-1))
    


# In[4]:


finalString("sfdfsdf",3)


# In[ ]:





# In[ ]:


get_ipython().set_next_input('3.Write a Python program to split and join a string');get_ipython().run_line_magic('pinfo', 'string')
Ans:


# In[5]:


def splitjoin(str1,str2):
    print(str1.split())
    print(str1.join(str2))


# In[6]:


st2 = "dmhknm"
st1 ="dfgdf"
splitjoin(st1,st2)


# In[ ]:





# In[ ]:


get_ipython().set_next_input('4.Write a Python to check if a given string is binary string or not');get_ipython().run_line_magic('pinfo', 'not')
Ans:


# In[ ]:


def bindarystring():
    myStr =  input('Enter the binary string : ')
    flag = true
    for char in myStr:
        if(char == '0' or char == 1):
            continue
        else:
            flag = false
            print("The String is not a binary string")
            break
    if(flag):
        print("The string is binary")


# In[ ]:





# In[ ]:


get_ipython().set_next_input('5.Write a Python program to find uncommon words from two Strings');get_ipython().run_line_magic('pinfo', 'Strings')
Ans:


# In[7]:


def uncommonwordsstring(s1,s2):
     count = {}
     for word in s1.split():
        count[word] = count.get(word, 0) + 1
     for word in s2.split():
        count[word] = count.get(word, 0) + 1
     return [word for word in count if count[word] == 1]


# In[8]:


s1="String with common"
s2="String without common"
print(uncommonwordsstring(s1, s2))


# In[ ]:





# In[ ]:


get_ipython().set_next_input('6.Write a Python to find all duplicate characters in string');get_ipython().run_line_magic('pinfo', 'string')
Ans:


# In[9]:


def dublicateCharacter():
    for i in range(0, len(string)):  
        count = 1;  
    for j in range(i+1, len(string)):  
        if(string[i] == string[j] and string[i] != ' '):  
            count = count + 1;  
            string = string[:j] + '0' + string[j+1:];  
   
    if(count > 1 and string[i] != '0'):  
        print(string[i]);  


# In[ ]:





# In[ ]:


get_ipython().set_next_input('7.Write a Python Program to check if a string contains any special character');get_ipython().run_line_magic('pinfo', 'character')
Ans:


# In[ ]:


import re
def tocheckspecialchar():
    string = input("Enter the string")
    special_char = re.compile("[@_!#$%^&*()<>?/\|}{~:]")
    if(special_char.search(string) == None):
        print("String does not have special character")
    else:
        print("String have special Character")


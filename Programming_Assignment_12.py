#!/usr/bin/env python
# coding: utf-8

# # Programming_Assignment-12

# In[ ]:





# In[ ]:


get_ipython().set_next_input('1.Write a Python program to Extract Unique values dictionary values');get_ipython().run_line_magic('pinfo', 'values')
Ans:


# In[1]:


def uniqueDic(dic):
    my_dict = {'hi' : [5,3,8, 0],
   'there' : [22, 51, 63, 77],
   'how' : [7, 0, 22],
   'are' : [12, 11, 45],
   'you' : [56, 31, 89, 90]}
    uniqueValue = list(sorted({elem for val in my_dict.values() for elem in val}))
    print(uniqueValue)


# In[ ]:





# In[ ]:


get_ipython().set_next_input('2.Write a Python program to find the sum of all items in a dictionary');get_ipython().run_line_magic('pinfo', 'dictionary')
Ans:


# In[2]:


def dictionarysum():
    sum=0
    my_dict = {'hi' : 4,
   'there' : 5,
   'how' : 4,
   'are' : 34,
   'you' : 36}
    for values in my_dict.values():
        sum = sum + values
    print(sum)


# In[3]:


dictionarysum()


# In[ ]:





# In[ ]:


get_ipython().set_next_input('3.Write a Python program to Merging two Dictionaries');get_ipython().run_line_magic('pinfo', 'Dictionaries')
ANs:


# In[ ]:


def dictionarysum(dict1,dict2):
    return dict1.update(dict2)


# In[ ]:





# In[ ]:


get_ipython().set_next_input('4.Write a Python program to convert key-values list to flat dictionary');get_ipython().run_line_magic('pinfo', 'dictionary')
Ans:


# In[ ]:


def flatDictionary():
    my_dict = {'month_num' : [1, 2, 3, 4, 5, 6], 'name_of_month' : ['Jan', 'Feb', 'March', 'Apr', 'May', 'June']}
    my_result = dict(zip(my_dict['month_num'], my_dict['name_of_month']))
    print(my_result)


# In[ ]:





# In[ ]:


get_ipython().set_next_input('5.Write a Python program to insertion at the beginning in OrderedDict');get_ipython().run_line_magic('pinfo', 'OrderedDict')
Ans:


# In[ ]:


from collections import OrderedDict
def ordereddict():
    iniordered_dict = OrderedDict([('akshat', '1'), ('nikhil', '2')])
    iniordered_dict.update({'manjeet':'3'})
    iniordered_dict.move_to_end('manjeet', last = False)
    print ("Resultant Dictionary : "+str(iniordered_dict))


# In[ ]:





# In[ ]:


6.Write a Python program to check order of character in string using OrderedDict()?
Ans:


# In[ ]:


def dictionairy():     
    key_value ={}   
    key_value[2] = 56      
    key_value[1] = 2
    key_value[5] = 12
    key_value[4] = 24
    key_value[6] = 18     
    key_value[3] = 323
    print ("Task 1:-\n")
    print ("Keys are")
    for i in sorted (key_value.keys()) :
        print(i, end = " ")


# In[ ]:





# In[ ]:


get_ipython().set_next_input('7.Write a Python program to sort Python Dictionaries by Key or Value');get_ipython().run_line_magic('pinfo', 'Value')
Ans:


# In[4]:


d_items = {'Mango':100,'PineApple':22,'Banana':60,'Grape':13}


def sort_dict(in_dict,sort_type):
    if sort_type == 'key':
        print(dict(sorted(in_dict.items(), key=lambda x:x[0], reverse=False)))
    else:
        print(dict(sorted(in_dict.items(), key=lambda x:x[1], reverse=False)))
        
sort_dict(d_items,'key')        
sort_dict(d_items,'value')


# In[ ]:





#!/usr/bin/env python
# coding: utf-8

# # Programming_Assignment-9

# In[ ]:





# In[ ]:


get_ipython().set_next_input('1.Write a Python program to check if the given number is a Disarium Number');get_ipython().run_line_magic('pinfo', 'Number')
Ans:


# In[1]:


def numberLength(num):
    count = 0
    while(num>0):
        count = count+1;
        num = num//10
    return count
    
def disarium(num):
    count = numberLength(num)
    #print(count)
    temp = num
    sum =0
    while(temp!=0):
        rem = temp%10
        sum = sum + int(rem**count)
        temp = temp //10
        count = count-1
    if sum == num:
        print('Its a Disarium Number')
    else:
        print('Its not a Disarium Number')
       


# In[2]:


disarium(324)


# In[ ]:





# In[ ]:


2.Write a Python program to print all disarium numbers between 1 to 100?
Ans:


# In[3]:


def numberLength(num):
    count = 0
    while(num>0):
        count = count+1;
        num = num//10
    return count
    
def disarium(num):
    count = numberLength(num)
    #print(count)
    disariumlist = []
    i =0
    temp = num
    sum =0
    while(temp>0):
        rem = temp%10
        sum = sum + int(rem**count)
        temp = temp //10
        count = count-1
    if num == sum:
        disariumlist.append(sum)
    return disariumlist

def num1to100():
    for i in range(1, 100):
        numberlist = disarium(i)
    for i in numberlist:
        print(i)


# In[4]:


num1to100()


# In[ ]:





# In[ ]:


get_ipython().set_next_input('3.Write a Python program to check if the given number is Happy Number');get_ipython().run_line_magic('pinfo', 'Number')
Ans:


# In[5]:


def happynumber(num):
    rem =0
    sum =0
    while(num>0):
        rem = num%10
        sum = sum + (rem*rem)
        num = num//10;
    return sum

def checkresult(num):
    result = num
    while(result != 1 and result != 4):    
        result = happynumber(result);  
    if(result == 1):    
        print(str(num) + " is a happy number");    
    elif(result == 4):    
        print(str(num) + " is not a happy number");   
        


# In[6]:


checkresult(45)


# In[ ]:





# In[ ]:


4.Write a Python program to print all happy numbers between 1 and 100?
Ans:


# In[7]:


def happynumber(num):
    rem =0
    sum =0
    while(num>0):
        rem = num%10
        sum = sum + (rem*rem)
        num = num//10
    return sum

def checkresult(num):
    result = num
    while(result != 1 and result != 4):    
        result = happynumber(result);  
    if(result == 1):    
        print(str(num) + " is a happy number");    
    elif(result == 4):    
        print(str(num) + " is not a happy number");  
    
def rangeNumber():
    for i in range(1, 100):
        checkresult(i)
    
        


# In[8]:


rangeNumber()


# In[ ]:





# In[ ]:


get_ipython().set_next_input('5.Write a Python program to determine whether the given number is a Harshad Number');get_ipython().run_line_magic('pinfo', 'Number')
Ans:


# In[9]:


def summ(num):
    rem =0
    sum =0
    while(num>0):
        rem = num%10
        sum = sum + rem
        num = num//10
    return sum
    
def harshadNumber(num):
    sum = summ(num)
    if(num%sum == 0):
        print("Its a harshad Number")
    else:
        print("Its not a harshad Number")


# In[10]:


harshadNumber(34)


# In[ ]:





# In[ ]:


6.Write a Python program to print all pronic numbers between 1 and 100?
Ans:


# In[11]:


def isPronicNumber(num):    
    flag = False;    
        
    for j in range(1, num+1):       
        if((j*(j+1)) == num):    
            flag = True;    
            break;    
    return flag;    
     
 
print("Pronic numbers between 1 and 100: ");    
for i in range(1, 101):    
    if(isPronicNumber(i)):    
        print(i),    
        print(" "), 


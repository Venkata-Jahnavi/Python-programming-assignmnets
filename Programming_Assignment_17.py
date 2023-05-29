#!/usr/bin/env python
# coding: utf-8

# # Programming_Assignment_17

# In[ ]:





# In[ ]:


Question1. Create a function that takes three arguments a, b, c and returns the sum of the
numbers that are evenly divided by c from the range a, b inclusive.
Examples
evenly_divisible(1, 10, 20) ➞ 0
# No number between 1 and 10 can be evenly divided by 20.
evenly_divisible(1, 10, 2) ➞ 30
# 2 + 4 + 6 + 8 + 10 = 30
evenly_divisible(1, 10, 3) ➞ 18
# 3 + 6 + 9 = 18


# In[1]:


def evenly_divisible(a,b,c):
    total = sum([x for x in range(a,b+1) if x % c == 0])
    if total > 0:
        print(f"Sum of the numbers that are evenly divided by {c} from range {a},{b} is => {total}.")
    else:
        print(f"No number between {a} and {b} can be evenly divided by {c}.")
        
evenly_divisible(1, 10, 20)
evenly_divisible(1, 10, 2)
evenly_divisible(1, 10, 3)


# In[ ]:





# In[ ]:


Question2. Create a function that returns True if a given inequality expression is correct and
False otherwise.
Examples
correct_signs(&quot;3 &lt; 7 &lt; 11&quot;) ➞ True
correct_signs(&quot;13 &gt; 44 &gt; 33 &gt; 1&quot;) ➞ False
correct_signs(&quot;1 &lt; 2 &lt; 6 &lt; 9 &gt; 3&quot;) ➞ True


# In[3]:


def correct_signs(s):
    regex = eval(s)
    if regex:
        return True
    else:
        return False    
    
print(correct_signs("3 < 7 < 11"))
print(correct_signs("13 > 44 > 33 > 1"))
print(correct_signs("1 < 2 < 6 < 9 > 3"))


# In[ ]:





# In[ ]:


Question3. Create a function that replaces all the vowels in a string with a specified character.
Examples
replace_vowels(&quot;the aardvark&quot;, &quot;#&quot;) ➞ &quot;th# ##rdv#rk&quot;
replace_vowels(&quot;minnie mouse&quot;, &quot;?&quot;) ➞ &quot;m?nn?? m??s?&quot;
replace_vowels(&quot;shakespeare&quot;, &quot;*&quot;) ➞ &quot;sh*k*sp**r*&quot;


# In[4]:


def replace_vowels(str1, char):
    vowels = ['a','e','i','o','u']
    str2 = str1.lower()
    for i in vowels:
        str2 = str2.replace(i,char)
        
    print(f"After replacing vowels from {str1} with {char} => {str2}")

replace_vowels("the aardvark", "#") 
replace_vowels("minnie mouse", "?")
replace_vowels("shakespeare", "*")


# In[ ]:





# In[ ]:


Question4. Write a function that calculates the factorial of a number recursively.
Examples
factorial(5) ➞ 120
factorial(3) ➞ 6
factorial(1) ➞ 1
factorial(0) ➞ 1


# In[5]:


def factorial(num):
    if num == 0:
        return 1
    else:
        return num*factorial(num-1)

inputs = [5,3,1,0]
for i in inputs:
    print(f"Factorial of {i} is => {factorial(i)}")


# In[ ]:





# In[ ]:


Question 5
Hamming distance is the number of characters that differ between two strings.
To illustrate:
String1: &quot;abcbba&quot;
String2: &quot;abcbda&quot;
Hamming Distance: 1 - &quot;b&quot; vs. &quot;d&quot; is the only difference.
Create a function that computes the hamming distance between two strings.
Examples
hamming_distance(&quot;abcde&quot;, &quot;bcdef&quot;) ➞ 5
hamming_distance(&quot;abcde&quot;, &quot;abcde&quot;) ➞ 0
hamming_distance(&quot;strong&quot;, &quot;strung&quot;) ➞ 1


# In[7]:


def hamming_distance(str1, str2):
    if len(str1) == len(str2):
        distance = 0
        for i in range(len(str1)):
            if str1[i] != str2[i]:
                distance += 1
                
        print(f"The hamming distance between {str1} and {str2} is => {distance}")
    
hamming_distance("abcde", "bcdef")
hamming_distance("abcde", "abcde")
hamming_distance("strong", "strung")


# In[ ]:





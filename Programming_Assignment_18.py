#!/usr/bin/env python
# coding: utf-8

# # Programming_Assignment_18

# In[ ]:





# In[ ]:


Question 1
Create a function that takes a list of non-negative integers and strings and return a new list
without the strings.
Examples
filter_list([1, 2, &quot;a&quot;, &quot;b&quot;]) ➞ [1, 2]
filter_list([1, &quot;a&quot;, &quot;b&quot;, 0, 15]) ➞ [1, 0, 15]
filter_list([1, 2, &quot;aasf&quot;, &quot;1&quot;, &quot;123&quot;, 123]) ➞ [1, 2, 123]


# In[1]:


def filter_list(lst):
    filtered_list = []
    for i in lst:
        if type(i) == int:
            filtered_list.append(i)
    return filtered_list

print(filter_list([1, 2, "a", "b"]))
print(filter_list([1, "a", "b", 0, 15]))
print(filter_list([1, 2, "aasf", "1", "123", 123]))


# In[ ]:





# In[ ]:


Question 2
The &quot;Reverser&quot; takes a string as input and returns that string in reverse order, with the
opposite case.
Examples
reverse(&quot;Hello World&quot;) ➞ &quot;DLROw OLLEh&quot;
reverse(&quot;ReVeRsE&quot;) ➞ &quot;eSrEvEr&quot;
reverse(&quot;Radar&quot;) ➞ &quot;RADAr&quot;


# In[2]:


def reverse(s):
    return s[::-1].swapcase()

print(reverse("Hello World"))
print(reverse("ReVeRsE"))
print(reverse("Radar"))


# In[ ]:





# In[ ]:


Question 3
You can assign variables from lists like this:
lst = [1, 2, 3, 4, 5, 6]
first = lst[0]
middle = lst[1:-1]
last = lst[-1]
print(first) ➞ outputs 1
print(middle) ➞ outputs [2, 3, 4, 5]
print(last) ➞ outputs 6
With Python 3, you can assign variables from lists in a much more succinct way. Create
variables first, middle and last from the given list using destructuring assignment
(check the Resources tab for some examples), where:
first ➞ 1
middle ➞ [2, 3, 4, 5]
last ➞ 6

Your task is to unpack the list writeyourcodehere into three variables, being first,
middle, and last, with middle being everything in between the first and last element. Then
print all three variables.


# In[3]:


first, *middle, last = [1,2,3,4,5,6]
print(f'first => {first}')
print(f'middle => {middle}')
print(f'last => {last}')


# In[ ]:





# In[ ]:


Question 4
Write a function that calculates the factorial of a number recursively.
Examples
factorial(5) ➞ 120
factorial(3) ➞ 6
factorial(1) ➞ 1
factorial(0) ➞ 1


# In[4]:


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
Write a function that moves all elements of one type to the end of the list.
Examples
move_to_end([1, 3, 2, 4, 4, 1], 1) ➞ [3, 2, 4, 4, 1, 1]
# Move all the 1s to the end of the array.
move_to_end([7, 8, 9, 1, 2, 3, 4], 9) ➞ [7, 8, 1, 2, 3, 4, 9]
move_to_end([&quot;a&quot;, &quot;a&quot;, &quot;a&quot;, &quot;b&quot;], &quot;a&quot;) ➞ [&quot;b&quot;, &quot;a&quot;, &quot;a&quot;, &quot;a&quot;]


# In[5]:


def move_to_end(lst, elem):
    # Create a new list with all elements that are not equal to the specified element
    filtered_list = [x for x in lst if x != elem]    
    # Add all elements that are equal to the specified element to the end of the filtered list
    filtered_list += [x for x in lst if x == elem]    
    # Return the modified list
    return filtered_list

print(move_to_end([1, 3, 2, 4, 4, 1], 1))
print(move_to_end([7, 8, 9, 1, 2, 3, 4], 9))
print(move_to_end(["a", "a", "a", "b"], "a"))


# In[ ]:





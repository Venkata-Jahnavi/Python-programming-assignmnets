#!/usr/bin/env python
# coding: utf-8

# # Programming_Assignment_16

# In[ ]:


Question1. Write a function that stutters a word as if someone is struggling to read it. The first two letters are repeated twice with an ellipsis ... and space after each, and then the word is pronounced with a question mark ?.

Examples

stutter("incredible") ➞ "in... in... incredible?"

stutter("enthusiastic") ➞ "en... en... enthusiastic?"

stutter("outstanding") ➞ "ou... ou... outstanding?"

Hint:- Assume all input is in lower case and at least two characters long.


# In[1]:


def stutter(word):
    print((word[0:2]+"... ")*2 + word[2:]+"?")

stutter("incredible")
stutter("enthusiastic")
stutter("outstanding")
stutter("ok")


# In[ ]:





# In[ ]:


Question 2.Create a function that takes an angle in radians and returns the corresponding angle in degrees rounded to one decimal place.

Example

radians_to_degrees(1) ➞ 57.3

radians_to_degrees(20) ➞ 1145.9

radians_to_degrees(50) ➞ 2864.8


# In[2]:


import math
def radians_to_degrees(angle):
    radians_angle = round((180/math.pi)*angle, 1)
    print(f"Radian Measure of {angle} degrees is {radians_angle}")
    
radians_to_degrees(1)
radians_to_degrees(20)
radians_to_degrees(50)


# In[ ]:





# In[ ]:


Question 3. In this challenge, establish if a given integer num is a Curzon number. If 1 plus 2 elevated to num is exactly divisible by 1 plus 2 multiplied by num, then num is a Curzon number.

Given a non-negative integer num, implement a function that returns True if num is a Curzon number, or False otherwise.

Example

is_curzon(5) ➞ True
# 2 ** 5 + 1 = 33
# 2 * 5 + 1 = 11
# 33 is a multiple of 11

is_curzon(10) ➞ False
# 2 ** 10 + 1 = 1025
# 2 * 10 + 1 = 21
# 1025 is not a multiple of 21

is_curzon(14) ➞ True
# 2 ** 14 + 1 = 16385
# 2 * 14 + 1 = 29
# 16385 is a multiple of 29


# In[3]:


def is_curzon(num):
    num1 = 2 ** num + 1
    num2 = 2 * num + 1
    if num1 % num2 == 0:
        print(f"{num1} is a multiple of {num2}")
        return True
    else:
        print(f"{num1} is not a multiple of {num2}")
        return False
    
inputs = [5,10,14]
for i in inputs:
    print(f"{i} is {'a curzon number' if is_curzon(i) else 'not a curzon number'}")
    print()


# In[ ]:





# In[ ]:


Question 4.Given the side length x find the area of a hexagon.

Examples
area_of_hexagon(1) ➞ 2.6
area_of_hexagon(2) ➞ 10.4
area_of_hexagon(3) ➞ 23.4


# In[4]:


def area_of_hexagon(length):
    area = (3*(3**0.5)*(length**2)) / 2
    print(f"Area of hexagon having side length {length} is {area}")
    #return area

inputs = [1,2,3]
for i in inputs:
    area_of_hexagon(i)


# In[ ]:





# In[ ]:


Question 5. Create a function that returns a base-2 (binary) representation of a base-10 (decimal) string number. To convert is simple: ((2) means base-2 and (10) means base-10) 010101001(2) = 1 + 8 + 32 + 128.

Going from right to left, the value of the most right bit is 1, now from that every bit to the left will be x2 the value, value of an 8 bit binary numbers are (256, 128, 64, 32, 16, 8, 4, 2, 1).

Examples

binary(1) ➞ "1"
# 1*1 = 1

binary(5) ➞ "101"
# 1*1 + 1*4 = 5

binary(10) ➞ "1010"
# 1*2 + 1*8 = 10


# In[5]:


def binary(num):
    binary_num = bin(num).replace('0b','')
    print(f'Binary of {num} is {binary_num}')

inputs = [1,5,10]
for i in inputs:
    binary(i)


# In[ ]:





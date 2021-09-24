#!/usr/bin/env python
# coding: utf-8

# In[ ]:


7# write a program to print the given pattern
*
**
***
****


# In[12]:


num=int(input("enter the number of row: "))
for i in range(num):
    for j in range(i+1):
        print('*',end="")
    print('')
    


# In[ ]:


9# Write a program to make a calculator using the concept of classes and objects


# In[2]:


# Making calculator
# make the input
# 1.Add this function to add two numbers
def add(a,b):
    return a+b
#2.substract this function to substract 
def substract(a,b):
    return a-b
#3.multiply this function to get multiplicatiion
def multiply(a,b):
    return a*b
#4. this function to get division
def divide(a,b):
    return a/b

print("Select the operation:\n"       "1.add\n"       "2. substract\n"       "3. multiply\n"       "4. divide\n")

select=int(input("select the given operation from 1,2,3,4:"))
n1=int(input("enter the number:"))
n2=int(input("enter the another number:"))
if select ==1:
    print(n1+n2)
if select ==2:
    print(n1-n2)
if select ==3:
    print(n1*n2)
if select ==4:
    print(n1/n2)
else:
    print("invalid record")


# In[ ]:





#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Question 1

#Write a Python program to convert an array to an ordinary list with the same items.

#we can use the np.tolist() function
import numpy as np
array=np.array([[1,2],[3,4],[5,6]])
list1=array.tolist()
print(list1)


# In[2]:


#Question2 

#Write a NumPy program to compute the sum of the diagonal elements of a given array.

#Hint: Two methods to solve this problem: 1. manually(without direct function). 2. using the trace function

import numpy as np
arr1=np.array([[1,2],[3,4],[5,6]])
np.trace(arr1)
#print("Output is: \n", x)


# In[3]:


#Question 3
#Given an array of your choice, get all the values higher than X: 
#If a = [[1,2],[3,5]] and x = 2 :  then 3 and 5 are higher than 2.

import numpy as np 

array=np.random.randint(2, 10, size=(2,4))
print(array)


# In[11]:



import numpy as np
arr = np.random.randint(2,10, size=(2,4))

# declare specified value


# view array
print(arr)
for i in range (arr.shape[0]):
      for j in range (arr.shape[1]):
          if (arr[i,j]>2):
              print(arr[i,j])
          



# In[5]:


#Question 4
#Given two arrays, A & B have the same shape. 
#The task is to apply addition by hand: C is the new array. 

import numpy as np
arr1=np.array([[1,2],[3,4]])
arr2= np.array ([[5,6],[7,8]])

for i in range (arr1.shape[0]):
    for j in range(arr1.shape[1]):
        arr1[i,j]+=arr2[i,j]
        
print (arr1)


# In[ ]:


#question 5
#Write a NumPy program to subtract the mean of each row of a given matrix.
#Hint: use the mean function
import statistics
import numpy as np 
arr1= np.random.randint(1,5,size=(2,2))

# list of positive integer numbers
data1 = [1, 3, 4, 5, 7, 9, 2]
 
x = statistics.mean(data1)
 
# Printing the mean
print("Mean is :", x)
import statistics
 
# list of positive integer numbers
data1 = [1, 3, 4, 5, 7, 9, 2]
 
x = statistics.mean(data1)
 
# Printing the mean
print("Mean is :", x)
import numpy as np
a


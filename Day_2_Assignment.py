#!/usr/bin/env python
# coding: utf-8

# In[5]:


a=int(input("Enter the number : "))
if a>1:
    for i in range(2,a):
        if (a%i)==0:
            print(a,"is not prime")
            break
    else:
            print(a,"is prime num")
else:
    print(a,"is not prime")


# In[7]:


num=int(input("Enter the number : "))

if num < 0:
   print("Enter a positive number")
else:
   sum = 0
   while(num > 0):
       sum += num
       num -= 1
   print("The sum is", sum)


# In[ ]:





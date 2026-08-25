#!/usr/bin/env python
# coding: utf-8

# # Array Easy 12-15

# In[10]:


# find min / max


# In[9]:


def find_min_max(arr):
    mi=ma=arr[0]
    for x in arr:
        if x<mi:
            mi=x
        if x>ma:
            ma=x
    return mi,ma



arr=[1,3,5,7,9,8,6,4,2]

find_min_max(arr)


# In[11]:


#reverse array


# In[17]:


def rev(arr1):
    left = 0
    right = len(arr1)-1
    while left<right:
        arr1[left],arr1[right]=arr1[right],arr1[left]
        left+=1
        right-=1
    return arr1



arr1 = [1,2,3,4,5,6,7]

rev(arr1)


# In[21]:


arr11 = [11,22,33,44,55]
arr11[::-1]


# In[22]:


#liner search


# In[42]:


def lin(arr2,target):
    a=0
    for x in arr2:
        if x == target:
            print(x, "is present in loop at index",arr2.index(x))
            
            
            
            
arr2 = [1,2,3,4,56,7,8,9]

lin(arr2,56)


# In[43]:


#check sorted array


# In[127]:


def sort(arr3):
    for i in range(len(arr3)-1):
        if arr3[i]>arr3[i+1]:
            print("not shorted")
        if arr3[i]<arr3[i+1]:
            print("shorted")

            
arr3 = [1,2,3,4,5,6,7]
sort(arr3)


# In[50]:


#remove dup


# In[67]:


def dup(arr4):
    seen = []
    for x in arr4:
        if x not in seen:
            seen.append(x)
    return seen

arr4 = [11,22,33,44,11,22,33,55,66,77,22,99]
dup(arr4)


# In[68]:


#move zeros to end 


# In[75]:


def zero(arr5):
    pos = 0
    for i in range(len(arr5)):
        if arr5[i] != 0:
            arr5[pos],arr5[i]=arr5[i],arr5[pos]
            pos+=1
    return arr5
    
    
arr5 = [0,1,2,0,3,4,0,6,7]
zero(arr5)


# In[76]:


#two sum


# In[95]:


def two_sum(arr6,target):
    seen = {}
    for i,x in enumerate(arr6):
        complement = target-x
        if complement in seen:
            return [seen[complement],i]
        seen[x] =i
    return []


arr6 = [1,2,3,4,5,6,7,8,9,0]
two_sum(arr6,3)


# In[100]:


#count Frequency


# In[101]:


def count(arr7):
    freq={}
    for x in arr7:
        freq[x] = freq.get(x,0)+1
    return freq


arr7 = [11,22,33,44,11,22,33,55,66,77,22,99]
count(arr7)


# In[102]:


# second largest number


# In[129]:


def second(arr8):
    first = seco = float('-inf')
    for x in arr8:
        if x > first:
            seco = first
            first = x
        elif first>x>seco:
            seco=x    
    return seco


arr8 = [11,22,33,44,11,221,33,55,66,77,22,99]
second(arr8)


# In[ ]:





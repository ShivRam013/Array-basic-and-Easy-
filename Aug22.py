#!/usr/bin/env python
# coding: utf-8

# # Array

# ### basics

# In[109]:


arr = [1,2,3,4,5]


# In[110]:


arr[2] #indexing


# In[111]:


#travarsal
for i in range(len(arr)):
    print(arr[i])


# In[112]:


len(arr)


# In[ ]:





# In[97]:


arr[2] = 100
print(arr[2])


# In[98]:


arr.append(11111)
arr.insert(1,13)


# In[99]:


arr.pop()


# In[100]:


arr.pop(2)


# In[101]:


arr.remove(1)


# In[102]:


arr.clear()


# In[103]:


del(arr)


# In[ ]:





# In[67]:


if 0 in arr:
    print("hi")
else:
    print("bye")


# In[62]:


arr.index(3)


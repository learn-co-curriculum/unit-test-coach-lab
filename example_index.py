#!/usr/bin/env python
# coding: utf-8

# Create a dictionary called `friends`

# In[71]:


friends = None


# There should be 3 `keys` for this dictionary, all of which are first names, while the `values` should be last names.

# In[72]:


friends = ['ammar','arif', 'ali']


# Create a function called 'capitalize' that will capitalize all the **values** of the dictionary.

# In[73]:


def capitalize(names_list):
    new_list = []
    for name in names_list:
         new_list.append(name.capitalize())
    return new_list


# Run the function to confirm that works on your `friends` dictionary

# In[74]:


capitalize(friends)


# In[ ]:





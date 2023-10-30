#!/usr/bin/env python
# coding: utf-8

# In[137]:


import re
def password_check(password):
    if len(password) < 6 or len(password) > 12:  
        return "Check passowrd length, Not less than 6 & Not more than 12"
        
    if not re.search("[a-z]", password):
            return "Invalid password"
        
    if not re.search("[A-Z]", password):
            return "Invalid password"
        
    if not re.search("[0-9]", password):
            return "Invalid password"
        
    if not re.search("[$#@_&%]", password):
            return "Invalid password"
        
    return "password accepted"


# In[139]:


password_check("@Abc2023")


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





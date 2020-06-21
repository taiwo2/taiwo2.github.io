#!/usr/bin/env python
# coding: utf-8

# In[1]:


import matplotlib.pyplot as plt
import pandas as pd
ri = pd.read_csv('temp_datalab_records_social_facebook.csv')
ri.head()


# In[2]:


ri.isnull().sum()


# In[3]:


ri.shape


# In[4]:


ri.dtypes


# In[5]:


pounds = ri['likes']
ounces = ri['talking_about_count']


# In[9]:


pounds.value_counts().sort_index()

pounds.describe()


# In[7]:


plt.scatter(pounds,ounces)
plt.xlabel('Birth weight (lb)')
plt.ylabel('Fraction of births')
plt.show()


# In[ ]:





# In[ ]:





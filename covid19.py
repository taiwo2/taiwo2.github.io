#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import xlrd
import openpyxl
import numpy as np


# In[2]:


excel =pd.ExcelFile("geopoll.xlsx")
#Export every single sheet of the .xlsx file as a .csv file.
sheet_1=excel.parse("Sheet1")
print(sheet_1)
sheet_1.to_csv("sheet1.csv",index=0,header=None)
sheet1=pd.read_csv("sheet1.csv",)
print(sheet1)


# In[12]:


sheet1.head()


# In[4]:


sheet1.describe()


# In[5]:


country_name =sheet1['Unnamed: 1']
country_name
Gender = sheet1['Unnamed: 4']
awareness =sheet1['Unnamed: 5']
birth =sheet1['Unnamed: 3']
challenge = sheet1['Unnamed: 7']
concern =sheet1['Unnamed: 8']
import numpy as np


# ## spread number among the  african countries

# In[6]:


# country that has the highest number of confirmed cases
np.max(country_name)


# In[7]:


#country that has the highest number of year cases
birth.describe().top


# In[8]:


#country that has the highest number of chalenge 
challenge.describe().top


# In[9]:


sheet1.shape


# In[ ]:





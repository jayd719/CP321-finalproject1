#!/usr/bin/env python
# coding: utf-8

# # CP321 Final Project

# In[16]:


import pandas as pd
import numpy as np


# In[17]:


datafile='/Users/jashan/projects/CP321/data/projectDataAll.csv'


# In[38]:


raw_data = pd.read_csv(datafile, skiprows=8)
raw_data


# Remove unnecessary rows.

# In[52]:


df = raw_data.iloc[8:]
df.set_index(df.columns[0],inplace=True)
df


# In[58]:


df.columns

def remove_trailing_chars(col):
    col = col.split(" ")
    col.pop()
    return "_".join(col)

for each in df.columns:
    if "Unnamed" not in each:
        print(remove_trailing_chars(each))


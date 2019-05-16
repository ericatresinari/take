#!/usr/bin/env python
# coding: utf-8

# In[110]:


import numpy as np
import pandas as pd


# In[111]:


from pandas import ExcelWriter
from pandas import ExcelFile


# In[112]:


df = pd.read_excel('C:\\Users\\ericat\\Downloads\\Blip Users Navigation (7).xlsx', header = 8)


# In[113]:


df.head()


# In[114]:


df_user_messages = df[df['Enviada Pelo'].str.contains("Bot")!=True]


# In[115]:


df_user_messages.head()


# In[116]:


df_filtered = df_user_messages.drop_duplicates(subset=['Usuário'], keep='first', inplace=False)


# In[117]:


df_filtered


# In[27]:


df_filtered.to_csv("C:\\Users\\ericat\\Downloads\\usuariosnextelsmsapple.csv", sep=';')


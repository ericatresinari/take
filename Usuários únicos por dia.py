#!/usr/bin/env python
# coding: utf-8

# In[2]:


import numpy as np
import pandas as pd


# In[ ]:


from pandas import ExcelWriter
from pandas import ExcelFile


# In[4]:


df = pd.read_excel('C:\\Users\\ericat\\Downloads\\Blip Users Navigation (7).xlsx', header = 8)


# In[6]:


df.head()


# In[9]:


df_user_messages = df[df['Enviada Pelo'].str.contains("Bot")!=True]
def convert_to_year(date_in_some_format):
    return str(date_in_some_format)[:10]
df_user_messages['Data'] = df_user_messages['Data'].apply(convert_to_year)


# In[10]:


df_user_messages.head()


# In[ ]:


#grouppedByDay = df_user_messages.groupby(['Data'])
#for key, item in grouppedByDay:
    #print(grouppedByDay.get_group(key), "\n\n")
#list_user = np.unique(df['Usuário'].values)


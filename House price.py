#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np


# In[6]:


data = pd.read_csv('houseprice.csv')


# In[11]:


type(data)


# In[7]:


data.columns


# In[10]:


data.shape


# In[8]:


data.head()


# In[9]:


data.info()


# In[12]:


data.index


# In[46]:


price=data['Price_house']
type(price)
plt.plot(price)
plt.show()


# In[19]:


data.describe()


# In[45]:


data.plot(kind='box',rot=45,layout =(100,900),fontsize=20)
plt.ylabel('cm')
plt.show()


# In[ ]:


data.plot(kind='scatter')


# In[3]:


corr=data.corr()
plt.figure(figsize=(13,8))
sns.heatmap( data.corr(),linewidths=0.1,vmax=1.0,square=True,linecolor='black',annot=True)


# In[ ]:





# In[ ]:





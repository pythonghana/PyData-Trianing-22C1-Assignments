#!/usr/bin/env python
# coding: utf-8

# In[24]:


get_ipython().system('pip install pyreadstat --upgrade --quiet')


# In[1]:


import numpy as np
import pandas as pd


# In[2]:



dataset = pd.read_spss("C:/Users/AFARI/Desktop/1ResearchProjectData.sav")


# In[3]:


dataset


# In[4]:


dataset.info()


# In[ ]:





# # Data cleaning 

# In[5]:


dataset.isnull().sum()


# In[6]:


dataset.dropna(inplace=True)


# In[7]:


dataset.isnull().sum()


# In[8]:


dataset.shape


# In[9]:


dataset.ndim


# In[10]:


dataset.describe()


# In[11]:


dataset['Method'] = dataset['wesson'].apply(lambda x: 'Standard' if 'Ruger_Smith' in x else 'Traditional')


# In[12]:


dataset


# In[13]:


dataset['Ethnic'].unique()


# In[ ]:





# In[14]:


dataset['Teacher'].unique()


# In[15]:


dataset['Method'].unique()


# In[17]:


dataset['Gender'].value_counts()


# In[18]:


dataset['Freeredu'].value_counts()


# In[22]:


dataset.groupby('Teacher').Score.sum()


# In[27]:


dataset.groupby('Ethnic').Score.sum()


# In[28]:


dataset.groupby("Method").Score.sum()


# From the result of dataset.groupby("Method").Score.sum() you may think that the standard method of teaching is the best because it has the highest valuethat is 8727.0 as compared to the traditional method which is 5372.0. 
# But if you consider it based on individual teacher performance, that is dataset.groupby('Teacher').Score.sum(), also you can not conclude that the traditional methed is the best which is thought by Ms Wesson because Ms Smith who uses the standard method isn't far from the total scores obtain by Ms Wesson.
# From the above I think both method are not bad but attention should paid Mrs Ruger as why her are students are doing well.
# 

# In[ ]:





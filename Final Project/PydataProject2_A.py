#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd 
import datetime


# In[2]:


data_df = pd.read_csv('C:/Users/AFARI/Desktop/PA_singlestate_timeseries - PA_singlestate_timeseries.csv')


# In[3]:


data_df


# # Overview of the dataset
# * The numbers of infected peoples keeps increasing on daily basis.
# * The number of deaths keeps increasing on a daily basis.
# * The number of peoples who are being vaccinated on each day keep increasing 

# In[149]:


data_df.info()


# In[151]:


data_df.describe(include = 'object')


# In[152]:


data_df.describe()


# In[75]:


data_df.duplicated().sum()


# In[76]:


duplicate = data_df[data_df.duplicated()]


# In[77]:


duplicate


# In[155]:


data_df["date"] = pd.to_datetime(data_df["date"])


# In[156]:


data_df.info()


# In[157]:


data_df['state'][491]


# In[159]:


new_cases = data_df.at[491,'actuals.newCases'] 


# In[160]:


new_cases


# In[ ]:





# In[161]:


new_deaths = data_df.at[491,'actuals.newDeaths'] 


# In[162]:


new_deaths


# # Cases per 100k population calculated using a 7-day rolling average.

# In[ ]:





# # Ratio of the population that has completed the vaccination

# In[169]:


ratio_c = data_df['metrics.vaccinationsCompletedRatio'][491]


# In[170]:


ratio_c


# # Ratio of the population that has initiated vaccination

# In[167]:


ratio_v = data_df['metrics.vaccinationsInitiatedRatio'][491]


# In[168]:


ratio_v


# # cumulative deaths that suspected or confirmed

# In[138]:


data_df['cumulative deaths'] =  data_df['actuals.deaths'].cumsum()


# In[139]:


c_deaths = data_df['cumulative deaths'][491]


# In[140]:


print('The cumulative deaths recorded on June 16th 2021 is {}'.format(c_deaths))


# # cumulative confirmed or suspected cases

# In[145]:


data_df['cumulative cases'] = data_df['actuals.newCases'].cumsum()


# In[146]:


c_cases = data_df['cumulative cases'][491]


# In[147]:


print('The cumulative cases recorded on June 16th 2021 is {}'.format(c_cases))


# In[171]:


data_dict = {
    'state': data_df['state'][491],
    'New Deaths': new_deaths,
    'New Cases': new_cases,
    'Cumulative Cases': c_cases,
    'Cumulative Deaths': c_deaths,
    'Initiated Vaccination Ratio': ratio_v,
    'Completed Vaccination Ratio': ratio_c
    
}


# In[172]:


data_dict


# In[173]:


from matplotlib import pyplot as plt


# In[176]:


data_df.plot(x='actuals.cases', y='metrics.vaccinationsCompletedRatio')


# * Yes, there is a salient trend
# 

# In[ ]:





# In[ ]:





# In[32]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





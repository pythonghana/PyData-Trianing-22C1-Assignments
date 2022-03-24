#!/usr/bin/env python
# coding: utf-8

# In[54]:


import urllib.request
from bs4 import BeautifulSoup as bs


headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36'
}
req = urllib.request.Request('https://www.jumia.com.gh/laptops/', headers=headers)

page = urllib.request.urlopen(req)

doc = bs(page, "html.parser")

print(doc)


# In[55]:


laptops_names1 = doc.find_all('h3', {'class': 'name'})
len(laptops_name)


# In[56]:


laptops_price= doc.find_all('div', {'class': 'prc'})

len(laptops_price)


# In[57]:


laptops_names2 = doc.find_all('div', {'class': 'name'})


# In[58]:


len(laptops_names2)


# In[59]:


laptops_names = laptops_names1 + laptops_names2


# In[60]:


len(laptops_names)


# In[61]:


product_name = []
for items in laptops_names:
    product_name.append(items.text)
product_name[:5]


# In[62]:


price = []
for items in laptops_price:
    price.append(items.text)
price[:5]


# In[63]:


import pandas as pd

laptops_dict = {
    'laptops_name': product_name,
    'laptops_price': price
}


# In[64]:


laptops_df = pd.DataFrame(laptops_dict)


# In[65]:


laptops_df


# In[66]:


laptops_df.to_csv('laptops.csv')


# In[ ]:





# In[ ]:





#!/usr/bin/env python
# coding: utf-8

# In[2]:


import urllib.request
from bs4 import BeautifulSoup as bs


headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36'
}
req = urllib.request.Request('https://www.jumia.com.gh/phones-tablets/', headers=headers)

page = urllib.request.urlopen(req)

doc = bs(page, "html.parser")




# In[3]:


phone_name = doc.find_all('div', {'class': 'name'})


# In[4]:


phone_name[:10]


# In[5]:


phone_n = doc.find_all('h3', {'class': 'name'})


# In[6]:


phone_n[:10]


# In[7]:


product_name = phone_name + phone_n


# In[8]:


product_name


# In[9]:


price_tag = doc.find_all('div', {'class': 'prc'})


# In[10]:


price_tag[:10]


# In[11]:


url_link_tag = doc.find_all('a', {'class':'core'})


# In[12]:


url_link_tag[:138]


# In[13]:


url_link_tag[0]['href']


# In[14]:


phone0_link = 'https://www.jumia.com.gh' + url_link_tag[8]['href']


# In[15]:


phone0_link


# In[16]:


phone_names_tags= []
for tag in product_name[:130]:
    phone_names_tags.append(tag.text)
len(phone_names_tags)


# In[17]:


price = []
for tag in price_tag[:130]:
    price.append(tag.text)
len(price)


# In[18]:


phone_url = []

base_url = base_url = 'https://www.jumia.com.gh'
for tag in url_link_tag:
    if 'href' in tag.attrs:
        phone_url.append(base_url + tag['href'])
len(phone_url)


# In[19]:


phone_dict = {
    'phone_name': phone_names_tags,
    'phone_price': price,
    'url_links': phone_url,
}


# In[20]:


import pandas as pd
phone_df = pd.DataFrame(phone_dict)


# In[21]:


phone_df[:130]


# In[22]:


phone_df.to_csv('phone.csv')


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[31]:





# In[33]:





# In[ ]:





# In[ ]:





# In[ ]:





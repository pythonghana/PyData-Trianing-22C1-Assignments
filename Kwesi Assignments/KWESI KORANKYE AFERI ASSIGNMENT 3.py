#!/usr/bin/env python
# coding: utf-8

# In[16]:


# import webdriver from selenium
from selenium import webdriver
url = 'https://www.jumia.com.gh/laptops/'
# use the url to scrap the information
driver = webdriver.Chrome()
# the webdriver is used to open Chrome
driver.get(url)
# Open the url link using chrome webdriver


# In[19]:


laptops = [names.text for names in driver.find_elements_by_xpath('//h3')]
laptops

# The xpath is used to get all the names of the laptops. The laptops names are wrapped in the tag h3


# In[18]:


laptop_price = [prices.text for prices in driver.find_elements_by_xpath('//div[@class="info"]//child::div[@class="prc"]')]
laptop_price                      

# The xpath is used to get all the prices of the laptops. The laptop prices are wrapped in the tad div with class name 'prc'. Also, all div with class 'prc' is a child of the div with class 'info'.


# In[23]:


laptop_url_links = [links.get_attribute('href') for links in driver.find_elements_by_xpath('//article[contains(@class,"prd _fb")]//child::a')]
laptop_url_links

# use xpath to get all the laptops links. The links are in the tag 'a'.
# These 'a' tag are wrapped in the 'article' tag.
# The article tag has two separate class name prd_fb col c-prd and pr_fb_spn c-prd col
# The contains methed is used with the common name between the two classes to get all the article tag and get the child element as well. the tag 'a' is a child of the article tag.
# The get_attribute method(href) is used to get the links


# In[26]:


import pandas as pd
# import the pandas libruary
laptop_dict = {
    'laptop_name': laptops,
    'laptop_price': laptop_price,
    'url_link': laptop_url_links
} 

# Create a dictionary((laptop_dict)) for your data

laptop_df = pd.DataFrame(laptop_dict)
# put the dictionary(laptop_dict) into a datafram
laptop_df


# In[27]:


laptop_df.to_csv('laptop_prod.csv')


# In[ ]:





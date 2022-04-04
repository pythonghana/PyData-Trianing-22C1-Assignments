#!/usr/bin/env python
# coding: utf-8

# In[38]:


import pandas as pd
from bs4 import BeautifulSoup as bs
import requests 


# In[39]:


url='https://www.yarnplaza.com/yarn/dmc'
data=requests.get(url).text
data


# In[46]:


url1='https://www.yarnplaza.com/product/4216/dmc-natura-xl.html'
nxl=requests.get(url1).text
nxl


# In[47]:


url2='https://www.yarnplaza.com/yarn/drops?page=3'
a=requests.get(url2).text
a


# In[49]:


url3='https://www.yarnplaza.com/yarn/drops/drops-safran'
fran=requests.get(url3).text
fran


# In[50]:


url4='https://www.yarnplaza.com/yarn/stylecraft?page=2'
sky=requests.get(url4).text
soup1=bs(dk,'html.parser')
soup1


# In[51]:


url5='https://www.yarnplaza.com/yarn/stylecraft/stylecraft-special-dk'
ssd=requests.get(url5).text
ssd


# In[8]:


data1=bs(data,'html.parser')
data1


# In[52]:


dataa1=bs(nxl,'html.parser')
dataa1


# In[53]:


a1=bs(a,'html.parser')
a1


# In[54]:


soup=bs(fran,'html.parser')
soup


# In[ ]:





# In[ ]:





# In[55]:


book=bs(ssd,'html.parser')
book


# In[15]:


data2=data1.find_all('h3',class_='productlist-title gtm-product-impression')
data3= [t.text.strip() for t in data2][10]
data3[:3]


# In[16]:


a2=a1.find_all('div',class_='productlist-topfx')
a3= [t.text.strip() for t in a2][7]
a3[:6]


# In[58]:


dk1=soup1.find_all('div',class_='productlist-topfx')
dk2=[t.text.strip() for t in dk1][8]
dk2[:11]


# In[18]:


data25=data1.find_all('h3',class_='productlist-title gtm-product-impression')
data26= [t.text.strip() for t in data2][10]
data26[4:]


# In[19]:


a9=a1.find_all('div',class_='productlist-topfx')
a10= [t.text.strip() for t in a9][7]
a10[6:]


# In[20]:


dk3=soup1.find_all('div',class_='productlist-topfx')
dk4=[t.text.strip() for t in dk3][8]
dk4[10:]


# In[21]:


data4=data1.find_all('div',class_='productlist-priceholder')
data5= [t.text.strip() for t in data4][10]
y=list(data5)
y[2]='9'
x=y[0] + y[2]
x


# In[25]:


a70=a1.find_all('div',class_='productlist-bottomfx')
a70
a80= [t.text.strip() for t in a70][7][:6]
p=list(a80)
l=p[0] + p[2]
l


# In[23]:


price=soup1.find_all('span',class_='productlist-price')
prices=[t.text.strip() for t in price]
h=list(prices[8])
h[2] = '3'
q=h[0] + h[2]
q


# In[26]:


dataa2=dataa1.find_all('tr')
dataa2
dataa3= [t.text.strip() for t in dataa2][8]
dataa3[11:]


# In[27]:


comp=soup.find_all('tr')
comp1= [t.text.strip() for t in comp]
comp1[8][11:]


# In[28]:


comu=book.find_all('tr')
compo1= [t.text.strip() for t in comu]
compo1[8][11:]


# In[29]:


dataa4=dataa1.find_all('tr')
dataa5= [t.text.strip() for t in dataa4][9]
dataa5[11:]


# In[30]:


nsize=soup.find_all('tr')
nsize1= [t.text.strip() for t in nsize ][9]
nsize1[11:]


# In[31]:


nsiz=book.find_all('tr')
nsiz1= [t.text.strip() for t in nsiz]
nsiz1[9][11:]


# In[32]:


import pandas as pd

results = {
  "Brand": [data3[:3], a3[:6], dk2[:11],],
    
   "Name": [data26[4:], a10[6:], dk4[10:], ], 
    
  "Price": [x, l, q,],
    
"Composition":[dataa3[11:],dataa3[11:],compo1[8][11:]],
               
"Neddle size":[dataa5[11:],nsize1[11:],nsiz1[9][11:]]}


# In[33]:


df = pd.DataFrame(results)


# In[34]:


df


# In[36]:


df.to_csv('final_project1.csv')


# In[ ]:





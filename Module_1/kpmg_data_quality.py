
# coding: utf-8

# In[31]:


import pandas as pd
from pandas import ExcelWriter
from pandas import ExcelFile


# In[37]:


trans=pd.read_excel("kpmg.xlsx",sheet_name='Transactions')


# In[38]:


trans.head()


# In[42]:


trans.info()


# In[45]:


#change int to date
trans['transaction_date']=pd.to_datetime(trans['transaction_date'],unit='s')
trans['transaction_date'].head()


# In[48]:


#chnage int to date
trans['product_first_sold_date']=pd.to_datetime(trans['product_first_sold_date'],unit='s')
trans['product_first_sold_date'].head()


# In[49]:


trans.describe()


# In[52]:


#check values
trans.isnull().sum()


# In[53]:


dups=trans.duplicated()
trans[dups].sum()


# In[55]:


trans['order_status'].value_counts()


# In[56]:


trans['online_order'].value_counts()


# In[57]:


trans['brand'].value_counts()

transactions['product_line'].value_counts()
# In[59]:


trans['product_line'].value_counts()


# In[61]:


trans['product_class'].value_counts()


# In[62]:


trans['product_size'].value_counts()


# In[69]:


ad=pd.read_excel("custadd.xlsx")
ad.head()


# In[70]:


ad['state'].value_counts()


# In[76]:


ad['state'].str.replace('VIC','Victoria')


# In[77]:


ad['state'].str.replace('NSW','New South Wales')


# In[79]:


new=pd.read_excel("newlist.xlsx")
new.head()


# In[80]:


new.info()


# In[81]:


#drop columns
c=['Unnamed: 16','Unnamed: 17','Unnamed: 19','Unnamed: 20']
new=new.drop(c,axis=1)


# In[82]:


#information
new.info()


# In[83]:


#check null data
new.isnull().sum()


# In[84]:


#duplicated data
new.duplicated().sum()


# In[85]:


#count no of people
new['gender'].value_counts()


# In[86]:


#replace U
new['gender'].str.replace('U','Unspecified')


# In[87]:


new['DOB'].describe()


# In[89]:


c=pd.read_excel("customerdemo.xlsx")
c.head()


# In[90]:


c['default'].value_counts()


# In[91]:


c.info()


# In[92]:


c['gender'].value_counts()


# In[93]:


#replace f to female,m to male, u to unspecified
c['gender'] = c['gender'].replace('F','Female').replace('M','Male').replace('Femal','Female').replace('U','Unspecified')


# In[95]:


c['gender'].value_counts()


# In[97]:


#merge customer demographics and customeraddress
cc = pd.merge(c,ad, how='left', on='customer_id')
cc


# In[ ]:





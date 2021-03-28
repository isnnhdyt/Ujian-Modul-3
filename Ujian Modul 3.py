#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')


# In[3]:


df = pd.read_csv('C:/Users/Isnan Hidayat/Desktop/purwadhika/Ujian-Modul-3-main/hotel_bookings.csv')
df


# In[4]:


df.info()


# In[6]:


df.sample(5)


# In[5]:


sns.countplot(x='is_canceled',data=df,hue='deposit_type')


# ##### Total pemesan lebih banyak yg merupakan pemesan tanpa deposit. lebih jauh lagi, dari pemesan yang tidak melakukan cancellation pada saat booking, semuanya merupakan customer yang tidak melakukan deposit sebelumnya. dan untuk kategori yang melakukan cancellation booking, setengah dari keseluruhan merupakan customer yg melakukan booking tanpa refund

# In[7]:


sns.countplot(x='is_canceled',data=df,hue='arrival_date_month')


# In[8]:





# In[10]:


sns.barplot(x='is_canceled', y='days_in_waiting_list', data=df)


# In[13]:


sns.barplot(x='is_canceled', y='lead_time', data=df)


# ##### dari hasil plot diatas dapat disimpulkan apabila lead time pemesanan diatas 80 hari, customer akan melakukan cancellation booking

# In[15]:


sns.countplot(x='is_canceled',data=df,hue='is_repeated_guest')


# ##### dari hasil plot diatas dapat disimpulkan apabila probabilitas paling besar untuk terjadinya cancellation booking adalah untuk tamu yang belum pernah melakukan booking di hotel tersebut. adapun angka cancellation booking yang dilakukan oleh tamu yang sebelumnya pernah menginap tetap ada, namun sangat kecil.

# In[17]:


df1 = df[['is_canceled','lead_time','arrival_date_month','adr','customer_type','days_in_waiting_list','deposit_type','is_repeated_guest']]


# ##### dibuat data frame baru dengan menggunakan feature yang sekiranya mempengaruhi terjadinya cancel booking 

# In[18]:


df1


# In[19]:


plt.figure(figsize = (10,10))
plt.title('Heatmap Correlation')
sns.heatmap(df1.corr(method = 'spearman'), annot = True)


# ##### menyimpulkan dari plot diatas, variabel yang mempengaruhi terjadinya cancellation booking sangat ditentukan oleh 
# 1. apakah tamu teresebut merupakan customer berulang (langganan)
# 2. lamanya customer tersebut berada dalam antrian booking

# In[20]:


df1.info()


# In[21]:


df.isna().sum()/df.shape[0]*100


# ##### dapat dilihat kalau ada data kosong pada feature agent dan company. Dua kolom tersebut selanjutnya akan di drop.

# In[22]:


df=df.drop('agent', axis=1)


# In[23]:


df=df.drop('company', axis=1)


# In[25]:


df.info()


# In[ ]:





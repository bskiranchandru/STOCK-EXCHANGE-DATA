#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
data = pd.read_csv('E:/3rd year/5th sem/Data Analytics/Project/archive/indexProcessed.csv')
data


# In[2]:


data.isnull().values.any()


# In[3]:


data.isnull().sum()


# In[6]:


mean = data.mean()
mean


# In[7]:


std = data.std()
std


# In[8]:


variance = data.var()
variance


# In[10]:


data.corr(method = 'pearson')


# In[20]:


import numpy as np
plt.scatter(data.Open, data.High)
plt.show()
m, b = np.polyfit(data.Open, data.High, 1)
plt.plot(data.Open, m*data.Open + b)


# In[22]:


import numpy as np
plt.scatter(data.High, data.Low)
plt.show()
m, b = np.polyfit(data.Open, data.High, 1)
plt.plot(data.Open, m*data.Open + b)


# In[ ]:


# very high Correlation between the values in the dataset 
# USed PCA to detect that 

import plotly.graph_objects as go

import pandas as pd
from datetime import datetime

df = pd.read_csv('E:/3rd year/5th sem/Data Analytics/Project/archive/indexProcessed.csv')

fig = go.Figure(data=[go.Candlestick(x=df['Date'],
                open=df['Open'],
                high=df['High'],
                low=df['Low'],
                close=df['Close'])])

fig.show

#most important graph , has all the necessary data for analysis



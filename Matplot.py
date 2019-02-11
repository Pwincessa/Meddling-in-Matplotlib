
# coding: utf-8

# ### There are diff data visualization libraries such as matplotlib, cborne(commonly used for making plots), choroplot, cufflinks, pandas, bokeh
# 

# In[14]:


import matplotlib.pyplot as plt


# In[18]:


import pandas as pd


# In[19]:


import numpy as np


# In[20]:


# built because of mathlab


# In[22]:


get_ipython().run_line_magic('matplotlib', 'inline')

#or plt.show()

#this line of code helps yo see the code you create inside the jupyter notebook


# In[23]:


x = np.random.randint(0,20,10)


# In[24]:


x


# In[25]:


y = x**2


# In[26]:


y


# In[27]:


plt.plot(x,y)


# In[30]:


plt.plot(x,y, "r+") #others are b-, g*, this shows the color of the graph


# In[29]:


plt.plot(x,y,"b*")
plt.xlabel("X Label")
plt.ylabel("Y Label")
plt.title("A plot of Y against X ")


# In[31]:


plt.subplot(1, 2, 1) #creates a multiplot on the same canvas
plt.plot(x,y,"r-")

plt.subplot(1, 2, 2) #creates a subplot
plt.plot(y,x,)


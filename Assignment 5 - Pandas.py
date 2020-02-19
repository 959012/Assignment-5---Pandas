#!/usr/bin/env python
# coding: utf-8

# # Assignment 5 Questions

# ## Problem Statement

# #### Task 1:
# 
# Read the dataset from the bellow link
# 
# url = https://raw.githubusercontent.com/hadley/data-baby-names/master/baby-names.csv
# 

# In[1]:


import pandas as pd
import matplotlib.pyplot as plt
data = pd.read_csv(r'C:\Users\BISWA\Downloads\baby-names.csv')
data.head()


# In[2]:


data.columns


# Questions

# 1. Delete unnamed columns

# In[3]:


# There is unnamed columns are not availabel in this dataset all columns are having their names


# 2. Show the distribution of male and female

# In[4]:


data['sex'].unique()


# In[5]:


plt.hist(data['sex'])
plt.show()


# 3. Show the top 5 most preferred names

# In[6]:


data['name'].value_counts().head(5)
#data['name'].mode(5)


# 4. What is the median name occurence in the dataset

# In[28]:


a = data.groupby('name').median().head(1)
a


# 5. Distribution of male and female born count by states

# In[14]:





# #### Task 2:
# 
# We have the min and max temperatures in a city In India for each months of the year. We
# would like to find a function to describe this and show it graphically, the dataset given below.
# 
#     Task:
#     1. fitting it to the periodic function
#     2. plot the fit
#     
#     Data
#     Max = 39, 41, 43, 47, 49, 51, 45, 38, 37, 29, 27, 25
#     Min = 21, 23, 27, 28, 32, 35, 31, 28, 21, 19, 17, 18
# 

# In[7]:


x = 39, 41, 43, 47, 49, 51, 45, 38, 37, 29, 27, 25
y = 21, 23, 27, 28, 32, 35, 31, 28, 21, 19, 17, 18


# In[8]:


def periodic(a):
    plt.plot(a)
    k = plt.show
    return(k)


# In[9]:


periodic(x)


# In[10]:


periodic(y)


# In[ ]:





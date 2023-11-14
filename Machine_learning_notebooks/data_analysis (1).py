#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd


# In[11]:


sms_messages= pd.read_csv('SMSSpamCollection',sep='\t',names=['label','messages'])


# In[13]:


sms_messages.describe()


# In[14]:


sms_messages.tail()


# In[16]:


sms_messages.label.value_counts()


# In[17]:


sms_messages['label_number'] = sms_messages.label.map({"ham":0,"spam":1})


# In[20]:


sms_messages.head()


# In[22]:


x = sms_messages.messages
y = sms_messages.label_number


# In[23]:


x.shape


# In[24]:


y.shape


# In[25]:


from sklearn.model_selection import train_test_split


# In[61]:


X_train, X_test, y_train, y_test = train_test_split(x,y, test_size=0.3,random_state = 13 )


# In[62]:


X_train.shape,X_test.shape


# In[63]:


y_train.shape,y_test.shape


# In[64]:


from sklearn.feature_extraction.text import CountVectorizer


# In[65]:


vector = CountVectorizer()


# In[66]:


vector.fit(X_train)


# In[67]:


X_train_dtmatrix = vector.transform(X_train)


# In[68]:


X_train_dtmatrix.shape


# In[69]:


X_train_dtmatrix


# In[70]:


X_test_dtmatrix = vector.transform(X_test)


# In[71]:


X_test_dtmatrix.shape


# In[72]:


X_test_dtmatrix


# In[85]:


from sklearn.naive_bayes import MultinomialNB


# In[105]:


nb_model = MultinomialNB()


# In[106]:


y_train.shape


# In[107]:


nb_model.fit(X_train_dtmatrix,y_train)


# In[110]:


prediction = nb_model.predict(X_test_dtmatrix)


# In[112]:


from sklearn import metrics


# In[113]:


metrics.accuracy_score(y_test,prediction)


# In[115]:


metrics.confusion_matrix(y_test,prediction)


# In[116]:


# logistic regression


# In[117]:


from sklearn.linear_model import LogisticRegression


# In[121]:


log_model = LogisticRegression()


# In[122]:


log_model.fit(X_train_dtmatrix,y_train)


# In[126]:


prediction2 = log_model.predict(X_test_dtmatrix)


# In[127]:


metrics.accuracy_score(y_test,prediction2)


# In[130]:


y_test < prediction
0 < 1


# In[136]:


X_test[y_test < prediction]


# In[144]:


X_test[y_test > prediction2]


# In[140]:


X_test[5427]


# In[141]:


metrics.confusion_matrix(y_test,prediction2)


# In[153]:


len(X_test[y_test > prediction2])


# In[ ]:





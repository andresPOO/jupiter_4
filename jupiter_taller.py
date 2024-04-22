#!/usr/bin/env python
# coding: utf-8

# In[1]:


print("Hola")


# In[2]:


import numpy as np


# In[4]:


#crear un ndarray lleno de ceros
ceros=np.zeros(10)
print(ceros)


# In[8]:


unos=np.ones((5,5))
print(unos)


# In[11]:


aleatorio=np.random.rand(5,5)
print(aleatorio)


# In[12]:


suma=np.sum(aleatorio)
suma


# In[13]:


media=np.mean(aleatorio)
media


# In[14]:


mediana=np.median(aleatorio)
mediana


# In[15]:


desviacion=np.std(aleatorio)
desviacion


# In[17]:


ordenado=np.sort(aleatorio)
ordenado


# In[20]:


import matplotlib.pyplot as plt
#Simular un conjunto de datos que representa la elevación puntual en un terreno
#Crear un conjunto de datos de prueba

elevacion=np.random.randint(0,3000, size=(100,100))
elevacion


# In[32]:


plt.imshow(elevacion, cmap="terrain")
plt.colorbar(label="altura en metros")
plt.show


# In[33]:


listaaltura=(1.80, 1.60, 1.60, 1.60, 1.60, 1.60, 1.75), (1.75, 1.59, 1.72, 1.74, 1.80, 1.60, 1.69)
altura=np.array(listaaltura)
altura


# In[42]:


media=np.mean(listaaltura)
media


# In[39]:


desviacion=np.std(listaaltura)
desviacion


# In[38]:


plt.imshow(listaaltura, cmap="flag")
plt.colorbar(label="altura en metros")
plt.show


# In[ ]:





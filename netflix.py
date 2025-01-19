#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[3]:


df = pd.read_csv(r"C:\Users\AUDREYMAKAM\Desktop\DATA\netflix\netflix_titles.csv")
df


# In[188]:


df.head(20)


# In[17]:


df.tail()


# In[23]:


df.shape


# In[25]:


df.size


# In[27]:


df.columns


# In[31]:


df.dtypes


# In[33]:


df.info()


# In[51]:


# y' a t'il les doublon dans le data set ? si oui retirez 
#nous allons utiliser duplicated()
df.head()


# In[43]:


df.shape


# In[53]:


df[df.duplicated()]


# In[59]:


#supprimez les doublons 
df.drop_duplicates()


# In[67]:


# Y a-t-il une valeur nulle dans une colonne ? Afficher avec carte avec seaborn
df.isnull().sum()


# In[69]:


import seaborn as sns


# In[73]:


sns.heatmap(df.isnull())


# In[83]:


#Pour « blood & water », quel est l’ID du spectacle et qui est le réalisateur de ce spectacle ?
df[df["title"].isin(["Blood & Water"])]


# In[89]:


#En quelle année le plus grand nombre de séries et de films sont sortis ? Afficher avec graphique à barres
df.dtypes


# In[109]:


df["date_M"] = pd.to_datetime(df["date_added"], errors='coerce')
# j'ai utlilisé " errors='coerce' " poue eviter des erreur par exemple si la colonne contient des valeur manquantes ou format incorrecte


# In[111]:


df.head()


# In[117]:


df["date_M"].dt.year.value_counts()


# In[121]:


import seaborn as sns 
import matplotlib.pyplot as plt 

plt.figure(figsize=(10, 6))

sns.barplot(df["date_M"].dt.year.value_counts())
plt.show


# In[123]:


#combien de films ont ete vu dans se data set et representez  le avec les bar 


# In[133]:


df.groupby("type").type.count()


# In[135]:


sns.barplot(df.groupby("type").type.count())


# In[143]:


#Afficher tous les films sortis en l’an 2000
df["year"] = df["date_M"].dt.year


# In[145]:


df.head()


# In[155]:


df[(df["type"] == "Movie") & (df["year"] == 2020.0)]


# In[180]:


# montrer seulement les titres de tous les tv shows that released in india only
df[ (df["type"] == "TV Show") & (df["country"] == "India")] ["title"]


# In[184]:


#Les 10 réalisateurs qui ont donné le plus grand nombre de séries télévisées et de films à Netflix
df["director"].value_counts().head(10)


# In[196]:


# afficher les enregistrements dont la categorie est movie de type comedie ou le que le soit united kingdom

df[ (df["type"] == "Movie") & (df["type"] == "TV Show") | (df["country"] == "United States")]


# In[208]:


# nombre de fiml ou tv que Luna Wedler a realisé
df[df["cast"] .str.contains("Melissa McCarthy")]


# In[212]:


df_new = df.dropna() # efface toute les ligne ayant des problemes 


# In[214]:


df_new.head()


# In[216]:


df_new.shape


# In[220]:


df_new[df_new["cast"] .str.contains("Melissa McCarthy")]


# In[222]:


df.rating.nunique() # retourne le nombre de valeur dans la col rainting


# In[224]:


df.rating.unique() # retourne les valeur unique dans la col rating


# In[228]:


# combien de film Le film a obtenu le rati de la TV-14 au canada 
df[(df["type"] == "Movie") & (df["rating"] == "TV-14") & (df["country"] == "Canada")].shape


# In[234]:


#combien de tv obtenu l'annotation par la R apres 2018
df[(df["type"] == "TV Show") & (df["rating"] == "R") & (df["year"] < 2018)].shape


# In[ ]:





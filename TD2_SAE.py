#!/usr/bin/env python
# coding: utf-8

# # Exercice 1 Exemple

# In[27]:


import csv
import matplotlib.pyplot as plt


# 1. a. Récupérer le fichier file bands.xlsx sur Plubel.  

# b. Ouvrir ce fichier avec un tableur et l’enregistrer au format .csv.  

# c. Créer un script Python pour importer ce fichier sous forme d’une liste de listes ou d’un dictionnaire.  

# In[11]:


table=[]
with open("/home/Etudiants/RT/BUT-RT-1/lg409538/Téléchargements/file_bands.csv",newline='') as csvfile:
    reader=csv.reader(csvfile,delimiter=',')
    for ligne in reader:
        table.append(ligne)
print(table)


# 2. a. Supprimer un des albums de la liste.  

# In[12]:


del table[0]
print(table)


# b. Ajouter un album à la liste.  

# In[13]:


album_moi = ['Majster','Despo Rutti' ,'2016','20','120']
table.append(album_moi)
print(table)


# c. Calculer la durée moyenne des albums.  

# In[24]:


for i in range(len(table)):
    table[i][4] = int(table[i][4])
    duree = [int(album[4]) for album in table]
    duree_moyenne = sum(duree) / len(duree)

print(table)
print(duree_moyenne)


# d. Trier les albums dans l’ordre chronologique.  

# In[25]:


table.sort(key=lambda x: int(x[2])) 
print(table)


# e. Calculer les effectifs cumul´es croissants de sortie d’albums en fonction des ann´ees.  

# In[26]:


annees = [int(album[2]) for album in table]
effectifs_cumules = [sum(1 for annee in annees if annee <= a) for a in annees]
print(effectifs_cumules)


# f. Donner la repr´esentation graphique des effectifs cumul´es croissants calcul´es pr´ec´edemment.  

# In[28]:


plt.plot(annees, effectifs_cumules, marker='o')
plt.xlabel('Année')
plt.ylabel('Effectif cumulé')
plt.title('Effectifs cumulés croissants en fonction des années')
plt.show()


# # Exercice 2 Le format .ics

# In[ ]:





import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#chargement du jeu de données
trimestre = pd.read_csv('Data_set/trimestres.csv')
vente = pd.read_csv('Data_set/vente.csv')
vente.head()
trimestre.head()

#fonction pour le lissage exponentiel
def lissage_simple(Data_set,alpha ,donnée, horizon) :
    n = donnée -1 -horizon
    trimestre_lissée = [Data_set[0]]
    base = []
    diff = 1 - alpha
    suite_geo = (1-alpha)/(1-alpha**n)
    resultat = 0
    i = 1
    j = n
    k = 1
    while( i <= n) :
        val =  diff*Data_set[i] + alpha*trimestre_lissée[i-1]
        trimestre_lissée.append(val)
        base.append(n)
        i += 1
    while(j < donnée) :
        trimestre_lissée.append(trimestre_lissée[i-1])
        base.append(n)
        j += 1
        i -+ 1
    while(k <= n-1) :
        resultat += (alpha**k)*(Data_set[n-k])
        k += 1
    resultat = resultat*suite_geo
    plt.figure(figsize=(12,4))
    plt.title(f'Série lissée  à l`horizon {horizon} pour alpha valant {alpha} avec pour une erreur de {resultat}')
    plt.axis([1 , 28 , 9320 ,12100])
    plt.plot(Data_set , label='jeu de données initial' , color = 'black')
    plt.plot(base ,Data_set , label=f'base de la prévision  à l`horizon h = {horizon}' , color = 'black')
    plt.plot(trimestre_lissée ,'--',label=f'lissage pour alpha = {alpha}',color = 'red')
    plt.legend()
    
    return 

#appel de la fonction à l'horizon 1
lissage_simple(trimestre.Donnée,0.1 , 26 , 1)
lissage_simple(trimestre.Donnée,0.2 , 26 , 1)
lissage_simple(trimestre.Donnée,0.3 , 26 , 1)
lissage_simple(trimestre.Donnée,0.4 , 26 , 1)
lissage_simple(trimestre.Donnée,0.5 , 26 , 1)
lissage_simple(trimestre.Donnée,0.6 , 26 , 1)
lissage_simple(trimestre.Donnée,0.7 , 26 , 1)
lissage_simple(trimestre.Donnée,0.8 , 26 , 1)
lissage_simple(trimestre.Donnée,0.9 , 26 , 1)

#appel de la fonction à l'horizon 7
lissage_simple(trimestre.Donnée ,0.1 , 26 , 7)
lissage_simple(trimestre.Donnée ,0.2 , 26 , 7)
lissage_simple(trimestre.Donnée ,0.3 , 26 , 7)
lissage_simple(trimestre.Donnée ,0.4 , 26 , 7)
lissage_simple(trimestre.Donnée ,0.5 , 26 , 7)
lissage_simple(trimestre.Donnée ,0.6 , 26 , 7)
lissage_simple(trimestre.Donnée ,0.7 , 26 , 7)
lissage_simple(trimestre.Donnée ,0.8 , 26 , 7)
lissage_simple(trimestre.Donnée ,0.9 , 26 , 7)

# fonction pour traiter le second jeux de données
def lissages_simple(Data_set,alpha ,donnée, horizon) :
    n = donnée - 1 - horizon
    trimestre_lissée = [Data_set[0]]
    base = []
    diff = 1 - alpha
    suite_geo = (1-alpha)/(1-alpha**n)
    resultat = 0
    i = 1
    j = n
    k = 1
    while( i <= n) :
        val =  diff*Data_set[i] + alpha*trimestre_lissée[i-1]
        trimestre_lissée.append(val)
        base.append(n)
        i += 1
    while(j < donnée) :
        trimestre_lissée.append(trimestre_lissée[i-1])
        base.append(n)
        j += 1
        i -+ 1
    while(k <= n-1) :
        resultat += (alpha**k)*(Data_set[n-k])
        k += 1
    resultat = resultat*suite_geo
    plt.figure(figsize=(14,5))
    plt.title(f'Série lissée  à l`horizon {horizon} pour alpha valant {alpha} avec pour une erreur de {resultat}')
    plt.axis([0 , 37 , 2.649*1e6 , 3.5*1e6])
    plt.plot(Data_set , label='jeu de données initial' , color = 'black')
    plt.plot(base ,Data_set , label=f'base de la prévision  à l`horizon h = {horizon}' , color = 'black')
    plt.plot(trimestre_lissée ,'--',label=f'lissage pour alpha = {alpha}',color = 'red')
    plt.legend()
    
    return 

#appel de la fonction à l'horizon 1
lissages_simple(vente.VENTES,0.1 , 36 , 1)
lissages_simple(vente.VENTES,0.2 , 36 , 1)
lissages_simple(vente.VENTES,0.3 , 36 , 1)
lissages_simple(vente.VENTES,0.4 , 36 , 1)
lissages_simple(vente.VENTES,0.5 , 36 , 1)
lissages_simple(vente.VENTES,0.6 , 36 , 1)
lissages_simple(vente.VENTES,0.7 , 36 , 1)
lissages_simple(vente.VENTES,0.8 , 36 , 1)
lissages_simple(vente.VENTES,0.9 , 36 , 1)

#appel de la fonction à l'horizon 8
lissages_simple(vente.VENTES,0.1 , 36 , 8)
lissages_simple(vente.VENTES,0.2 , 36 , 8)
lissages_simple(vente.VENTES,0.3 , 36 , 8)
lissages_simple(vente.VENTES,0.4 , 36 , 8)
lissages_simple(vente.VENTES,0.5 , 36 , 8)
lissages_simple(vente.VENTES,0.6 , 36 , 8)
lissages_simple(vente.VENTES,0.7 , 36 , 8)
lissages_simple(vente.VENTES,0.8 , 36 , 8)
lissages_simple(vente.VENTES,0.9 , 36 , 8)
import pandas as pd
from matplotlib import pyplot as plt

from PoczciwyStudent import PoczciwyStudent
from PoczciwyAltruistycznyStudent import PoczciwyAltruistycznyStudent
from System import *
from Task import *
from Procesor import *
from Alg import *
from LeniwyStudent import *
import seaborn as sns

Alglist = [PoczciwyStudent(12,0.5),LeniwyStudent(12,0.5,4),PoczciwyAltruistycznyStudent(12,0.5,0.1)]
System = System((Alglist),0.5,12)
dane = System.processAll(1,10000)
nazwy = ["Poczciwy","Leniwy","Altruista"]

def showObciazanie():
    lista = dane[1]
    fig, axes = plt.subplots(1, 3,figsize=(15,8))

    for i in range(len(nazwy)):
        axes[i].set_title(nazwy[i])
    i = 0
    for l in lista:
        data = pd.DataFrame(l)
        print(data)



        sns.heatmap(data.transpose(),cmap=  "Reds",ax=axes[i])
        i+=1
    plt.show()
def showSrednia_variance():
    lista= dane[0]
    fig, axes = plt.subplots(2, 3,figsize=(15,15),sharey="row")
    for i in range(len(nazwy)):
        axes[0,i].set_title(nazwy[i])
    axes[0,0].set_ylabel("średnia")
    axes[1,0].set_ylabel("odchylenie std")
    i=0

    for l in lista:
        data = pd.DataFrame(l)
        column_means= list(data.mean())
        print(column_means)
        sns.barplot(x=[x for x in range(len(column_means))],y=column_means,ax=axes[0,i])

        column_std = list(data.std())
        sns.barplot(x=[x for x in range(len(column_std))],y=column_std,ax=axes[1,i])
        i+=1
    plt.show()
def showLiczbaMigracjiiZapytan():
    migracje= dane[2]
    zapytania = dane[3]
    fig,axes = plt.subplots(1,2,figsize=(15,15))

    axes[0].set_title("Migracje")
    axes[1].set_title("Zapytania")



    sns.barplot(x=nazwy,y=migracje,ax=axes[0])
    sns.barplot(x=nazwy,y=zapytania,ax=axes[1])
    plt.show()



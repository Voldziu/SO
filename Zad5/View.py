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

def showObciazanie():
    lista = dane[1]
    for l in lista:
        data = pd.DataFrame(l)
        print(data)

        sns.heatmap(data.transpose(),cmap=  "Reds")
        plt.show()
def showSrednia_variance():
    lista= dane[0]
    for l in lista:
        data = pd.DataFrame(l)
        column_means= list(data.mean())
        print(column_means)
        sns.barplot(x=[x for x in range(len(column_means))],y=column_means)
        plt.show()
        column_std = list(data.std())
        sns.barplot(x=[x for x in range(len(column_std))],y=column_std)
        plt.show()


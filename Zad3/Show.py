import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

import Processing
from ALRU import ALRU
from Algorythm import Algorythm
from Generator import  generate
from RAND import RAND
from Re import Req1
from Disk import ProcessParalelly
from FIFO import FIFO
from OPT import OPT
from LRU import LRU
from Generator import *
import copy

import numpy as np

from FIFO import FIFO
from Proporcjonalne import Proporcjonalne
from RAM import RAM
from Rowne import Rowne
from SterowanieHerz import Sterowanie
from Strefowe import Strefowe
from Zad4Alg import Alg4


ram = RAM(np.array([[50, 40], [50, 100], [20, 200], [10, 45], [100, 150], [50, 100], [50, 100], [50, 100], [50, 100], [50, 100],
         [50, 100], [50, 100], [50, 100]]), Ramki=50)
fryzjer = Rowne(ram=copy.deepcopy(ram), szamotuly=50)
ster = Sterowanie(ram=copy.deepcopy(ram), szam=50, low=0.2, high=0.7, critical=0.9, MaxProcesowNaraz=5)
propor = Proporcjonalne(ram=copy.deepcopy(ram), szam=50)
strefa = Strefowe(ram=copy.deepcopy(ram), szam=50, MaxProcesowNaraz=5)
lista = []

lista.append(copy.deepcopy(fryzjer))
lista.append(copy.deepcopy(ster))
lista.append(copy.deepcopy(propor))
lista.append(copy.deepcopy(strefa))
def ShowLocals():

    df = generate(generatelist(0,20,0.4,200))[0]

    print(df)
    sns.lineplot(df,x="arrtime",y='position',marker="o")
    plt.show()




def ShowHeatmapAlg():
    alglist=[FIFO(),RAND(),OPT(),LRU(),ALRU()]
    df = ProcessParalelly(alglist,20,0.05,50,5,20)
    bitowalista = df[2]
    Szamotuly=df[3]
    lol = df[1]
    df=df[0]


    print(bitowalista)
    print(lol)


    for i in range(len(alglist)):
        sns.heatmap(df[i].transpose(),annot=True,cmap="Reds")
        plt.show()
        print(bitowalista[i])
        print(Szamotuly[i])
        # fig, axes = plt.subplots(1, 2)
        #
        # sns.scatterplot(x=range(len(bitowalista[i])),y=bitowalista[i],ax=axes[0])
        # sns.scatterplot(x=range(len(Szamotuly[i])),y=Szamotuly[i],ax=axes[1])
        plt.show()


def ShowBarsPageError():
    alglist = [FIFO(), RAND(),OPT(),LRU(),ALRU()]
    df = ProcessParalelly(alglist, 50, 0.1, 100, 4,20)[1]

    print(df)


def ShowSzamotuly():
    alglist = [FIFO(), RAND(), OPT(), LRU(), ALRU()]
    df = ProcessParalelly(alglist, 20, 0.05, 10000, 5, 20)
    szamotuly = df[3]
    for i in range(len(alglist)):

        sns.lineplot(x=range(len(szamotuly[i])),y=szamotuly[i])
        plt.show()



def GiveInfoZad4():

    return  Processing.ProcessAll(copy.deepcopy(lista))



def ShowHeatmapAlg4():
    duzalista= GiveInfoZad4()
    for i in range(len(lista)):
        danei = duzalista[i]
        print(danei[0])
        for df in danei[0]:
            sns.heatmap(df.transpose(),annot=True,cmap="Reds")
            plt.show()


def ShowSumyBledow():
    duzalista=GiveInfoZad4()
    for i in range(len(lista)):
        danei=duzalista[i]
        listabledow = danei[1]
        print(lista[i].name)
        print(listabledow)
        suma =0
        for dupa in listabledow:
            suma+=dupa
        print(suma)
def ShowSzamotanie():

    duzalista=GiveInfoZad4()
    szamotuly=lista[0].szamotuly
    for i in range(len(lista)):
        danei=duzalista[i]
        listabitowa=danei[2]
        print(listabitowa)
















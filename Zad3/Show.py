import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

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

def ShowLocals():

    df = generate(generatelist(20,0.4,200))[0]

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











#
#
#
#

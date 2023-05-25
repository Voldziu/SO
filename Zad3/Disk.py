import numpy as np
import pandas as pd
import seaborn as sns


from Algorythm import Algorythm
from FIFO import  FIFO
from Generator import *
from Re import Req1


def ProcessParalelly(AlgList: list[Algorythm],n:int,p:float,leng:int,ramki:int,szamotuly:int):
    globallist= generate(generatelist(n,p,leng))[1]
   # u =[9, 9, 9, 3, 9, 4, 4, 3, 3, 4, 4, 4, 1, 8, 4, 8, 4, 4, 4, 1, 8, 1, 2, 6, 6, 2, 7, 2, 7, 7, 6, 7, 2, 6, 8, 6, 8, 8, 8, 3, 8, 6, 3, 8, 8, 2, 8, 8, 4, 8, 4, 4, 8, 4, 4, 5, 7, 5, 3, 7, 5, 5, 7, 3, 3, 3, 2, 1, 1, 1, 2, 1, 6, 1, 2, 1, 2, 2, 8, 3, 8, 3, 3, 3, 8, 8, 2, 2, 7, 7, 7, 6, 9, 6, 9, 7, 7, 7, 7, 2, 5, 3, 5, 5, 3, 5, 3, 3, 3, 2, 3, 9, 9, 9, 3, 9, 3, 3, 7, 7, 9, 6, 5, 2, 6, 6, 2, 2, 5, 6, 6, 5, 7, 7, 8, 7, 8, 8, 8, 5, 8, 5, 5, 5, 8, 8, 8, 5, 8, 5, 4, 8, 8, 4, 9, 9, 2, 9, 2, 7, 7, 9, 7, 2, 9, 3, 9, 1, 3, 9, 3, 9, 1, 3, 3]
    #globallist=generate(u)[1]
    #initialize
    dflist=[]
    bledylist=[]
    ListaBitowa=[]
    Szamotuly=[]
    for alg in AlgList:
        alg.Queue=globallist.copy()
        alg.Ramki=ramki
        alg.ListaRamek=[None for x in range(ramki)]
        alg.HistoriaRamek=np.zeros(shape=(1,ramki),dtype=int)
        print("chuj")
        while(alg.Queue!=[]):
            alg.process()
        df = pd.DataFrame(alg.HistoriaRamek[1:])
        dflist.append(df)
        bledylist.append(alg.LiczbaBledowStron)
        ListaBitowa.append(alg.ListaBitowa)
        dlugosc = len(alg.ListaBitowa)
        suma=0
        szams=[]
        for i in range(dlugosc):
            if(i%szamotuly==0):
                szams.append(suma/szamotuly)
                suma=alg.ListaBitowa[i]


            else:
                suma=suma+alg.ListaBitowa[i]
        Szamotuly.append(szams[1:])




















    return [dflist,bledylist,ListaBitowa,Szamotuly]


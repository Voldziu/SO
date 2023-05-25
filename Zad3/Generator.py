import numpy as np
import random

import pandas as pd

from Re import Req1


def generate(lista:list[int]):
    a:list[Req1]=[]
    for i in range(len(lista)):
        a.append(Req1(lista[i],i))






    return [pd.DataFrame.from_records(vars(o) for o in a),a]



def generatelist(n:int,probability:float,length:int):
    list = []
    k = round(n/10) #rozpietosc podzbioru

    i = 0
    while(i<length):
        print(i)
        if(random.random()<=probability):
            j=0
            p =random.randrange(5*k)

            startnumber = random.randrange(n - k)
            while j < p and i<length:
                liczba = random.randint(startnumber,startnumber+k)
                if liczba==0:
                    liczba=1

                list.append(liczba)

                i=i+1
                j+=1

        else:
            list.append(random.randrange(n))
            i=i+1





    return list










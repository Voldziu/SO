import numpy as np
import random

import pandas as pd

from Re import Req1

import random

def distribute_elements(N, M):
    pots = [0] * M  # Initialize pots with zero elements

    # Distribute N elements randomly
    for _ in range(N):
        pot_index = random.randint(0, M - 1)
        pots[pot_index] += 1

    return pots




def generate(lista:list[int]):
    a:list[Req1]=[]
    for i in range(len(lista)):
        a.append(Req1(lista[i],i))






    return [pd.DataFrame.from_records(vars(o) for o in a),a]



def generatelist(start:int,n:int,probability:float,length:int):
    list = []
    k = round((n-start)/10) #rozpietosc podzbioru

    i = 0
    while(i<length):
        print(i)
        if(random.random()<=probability):
            j=0
            p =random.randrange(5*k)

            startnumber = random.randrange(start,n - k)
            while j < p and i<length:
                liczba = random.randint(startnumber,startnumber+k)
                if liczba==0:
                    liczba=1

                list.append(liczba)

                i=i+1
                j+=1

        else:
            list.append(random.randrange(start,n))
            i=i+1





    return list

def generate2d(array:np.ndarray,Probability:float):
    ret:[list]=[]
    rozpietosci = (array[:,0])
    dlugosci =(array[:,1])
    size = len(rozpietosci)

    start=0
    for i in range(size):
        ret.append(generate(generatelist(start,rozpietosci[i]+start,Probability,dlugosci[i]))[1]) #100 mozna zmienic na cos losowego.
        start+=rozpietosci[i]
        print(ret[i])
    return ret













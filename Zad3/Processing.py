import copy

import numpy as np

from FIFO import FIFO
from Proporcjonalne import Proporcjonalne
from RAM import RAM
from Rowne import Rowne
from SterowanieHerz import Sterowanie
from Strefowe import Strefowe
from Zad4Alg import Alg4

ram = RAM(np.array([ [50,40],[50,100],[20,200 ],[10,45],[100,150],[50,100],[50,100],[50,100],[50,100],[50,100],[50,100],[50,100],[50,100]]),Ramki=100)
fryzjer = Rowne(ram=copy.deepcopy(ram),szamotuly=50)
chuj = Sterowanie(ram=copy.deepcopy(ram),szam=50,low=0.2,high=0.8,critical=0.9,MaxProcesowNaraz=5)
lol = Proporcjonalne(ram=copy.deepcopy(ram),szam=50)
dupa = Strefowe(ram=copy.deepcopy(ram),szam=50,MaxProcesowNaraz=5)

def ProcessAll(Alglist:list[Alg4]):
    wholelist=[]
    for alg in Alglist:
        wholelist.append(alg.process(FIFO()))
    return wholelist



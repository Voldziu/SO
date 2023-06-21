import numpy as np
import pandas as pd
import seaborn as sns

from Algorythm import Algorythm
from FIFO import  FIFO
from Generator import *
from Re import Req1



class RAM:
    def __init__(self,CreateArray:np.ndarray,Ramki:int):
        self.Array = CreateArray
        self.Data = (generate2d(CreateArray,0.5))
        self.Ramki=Ramki



















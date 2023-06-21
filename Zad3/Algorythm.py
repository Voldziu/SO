import numpy as np

from Re import Req1
class Algorythm:
    def __init__(self,name:str):
        self.Queue: list[Req1]=[]
        self.name = name
        self.Ramki:int=0
        self.ListaRamek=[]
        self.LiczbaBledowStron=0
        self.HistoriaRamek = None
        self.ListaBitowa:list[int]=[]
        self.IsShutDown:bool=False
        self.ChceRamke:bool=False
        self.MozeDacRamke:bool=False
        self.balans:int=0
        self.ChwilowaLiczbaBledowStron = 0
        self.Rozszerzenie=0
        self.KwantowaLista=[]
        self.Swiezak:bool = False





    def process(self):
        pass



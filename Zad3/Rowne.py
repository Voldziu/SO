import copy

import numpy as np
import pandas as pd

from Algorythm import Algorythm
from RAM import RAM
from Zad4Alg import Alg4


class Rowne(Alg4):
    def __init__(self,ram:RAM,szamotuly:int):
        super().__init__(ram,name="Rowne",szamutuly=szamotuly)


    def process(self,algorg:Algorythm):
        dflist = []
        bledylist = []
        ListaBitowa = []
        Szamotuly = []

        data = self.ram.Data
        ramki = self.ram.Ramki
        procesy = len(data)
        RamkiNaProces = ramki//procesy
        reszta = ramki - RamkiNaProces * procesy
        lista=[] #lista przechowuje liczbe ramek dla danego procesu
        for i in range(procesy):
            if(reszta>0):
                lista.append(RamkiNaProces+1)
                reszta-=1
            else:
                lista.append(RamkiNaProces)

        for i  in range(len(lista)):
            alg=copy.deepcopy(algorg)
            alg.Ramki=lista[i]
            alg.Queue=data[i]
            alg.ListaRamek = [None for x in range(alg.Ramki)]
            alg.HistoriaRamek = np.zeros(shape=(1, alg.Ramki), dtype=int)
            while(alg.Queue!=[]):
                alg.process()

            df = pd.DataFrame(alg.HistoriaRamek[1:])
            dflist.append(df)
            bledylist.append(alg.LiczbaBledowStron)
            ListaBitowa.append(alg.ListaBitowa)
            dlugosc = len(alg.ListaBitowa)
            suma = 0
            szams = []
            for i in range(dlugosc):
                if (i % self.szamotuly == 0):
                    szams.append(suma / self.szamotuly)
                    suma = alg.ListaBitowa[i]


                else:
                    suma = suma + alg.ListaBitowa[i]
            Szamotuly.append(szams[1:])
            # Adflist.append(dflist)
            # AListaBitowa.append(ListaBitowa)
            # Abledylist.append(bledylist)
            # ASzamotuly.append(Szamotuly)

        return [dflist, bledylist, ListaBitowa, Szamotuly]









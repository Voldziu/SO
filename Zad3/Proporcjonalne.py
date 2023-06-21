import copy

import numpy as np
import pandas as pd

from Algorythm import Algorythm
from RAM import RAM
from Zad4Alg import Alg4


class Proporcjonalne(Alg4):
    def __init__(self,ram:RAM,szam):
        super().__init__(ram,name="Proporcjonalne",szamutuly=szam)
    def process(self,algorg:Algorythm):
        dflist = []
        bledylist = []
        ListaBitowa = []
        Szamotuly = []

        data = self.ram.Data
        array = self.ram.Array
        ramki = self.ram.Ramki
        procesy = len(data)



        zwrotlista = [1 for i in range(len(array[:,0]))]
        pozostale = ramki - len(array[:,0])
        suma = 0
        klucze = array[:,1]
        for i in range(len(klucze)):
            suma += klucze[i]

        suma1 = 0
        for i in range(len(zwrotlista)):
            rozpietosc = klucze[i]
            procent = rozpietosc / suma
            przydzial = pozostale * procent
            suma1 += round(przydzial + 1)

            zwrotlista[i] = round(zwrotlista[i] + przydzial)
        sortlista = sorted(zwrotlista, reverse=True)

        # zabierz najbogatszym
        print(sortlista)
        for i in range(suma1 - ramki):
            zwrotlista[zwrotlista.index(sortlista[i])] = sortlista[i] - 1

        print(zwrotlista)








        for i  in range(len(zwrotlista)):
            alg=copy.deepcopy(algorg)

            alg.Ramki=zwrotlista[i]
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
            # dflist.append(dflist)
            # ListaBitowa.append(ListaBitowa)
            # bledylist.append(bledylist)
            # Szamotuly.append(Szamotuly)

        return [dflist, bledylist, ListaBitowa, Szamotuly]


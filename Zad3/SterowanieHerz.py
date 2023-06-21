import numpy as np
import pandas as pd

from Algorythm import Algorythm
from RAM import RAM
from Zad4Alg import Alg4
from Generator import *
import copy


class Sterowanie(Alg4):
    # szamotuly - badanie

    def __init__(self,ram:RAM,szam,low:float,high:float,critical:float,MaxProcesowNaraz:int):
        super().__init__(ram,name="Sterowanie Czestotliwoscia Bledu Strony",szamutuly=szam)
        self.low = low
        self.high=high
        self.c=critical
        self.MaxProcesowNaraz =MaxProcesowNaraz
        self.WolneRamki = 0


    def process(self, alg: Algorythm):
        dflist = []
        bledylist = []
        ListaBitowa = []
        Szamotuly = []

        data = self.ram.Data
        array = self.ram.Array
        ramki = self.ram.Ramki
        procesy = len(data)

        zwrotlista = [1 for i in range(len(array[:self.MaxProcesowNaraz, 0]))]
        pozostale = ramki - len(array[:self.MaxProcesowNaraz, 0])
        suma = 0
        klucze = array[:self.MaxProcesowNaraz, 1]
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

        Alglist = [copy.deepcopy(alg) for i in range(len(zwrotlista))]




        # lista algorytmow dla kazdego procesu

        SposobOdwolania=distribute_elements(self.szamotuly,len(zwrotlista))

        #zaladowanie poczatkowe
        #k - przesuniecie zeby brac kolejne procesy
        k=0
        for i in range(len(zwrotlista)):
            Alglist[i].Queue=data[i]
            Alglist[i].Ramki=zwrotlista[i]
            Alglist[i].ListaRamek=[None for x in range(Alglist[i].Ramki)]
            Alglist[i].HistoriaRamek= np.zeros(shape=(1, Alglist[i].Ramki), dtype=int)

        flag=True
        while(flag):
            print("lol")

            for i in range(len(zwrotlista)):


                if(not Alglist[i].IsShutDown and flag):
                    for j in range(SposobOdwolania[i]): # wykonaj sie tyle razy, ile zostalo przydzielone losowo (permutacje)
                        if Alglist[i].Queue !=[]:
                            Alglist[i].process()
                        else:
                            k+=1
                            if k<= (len(data)-len(zwrotlista)):
                                self.WolneRamki+=Alglist[i].Ramki
                                df = pd.DataFrame(Alglist[i].HistoriaRamek[1:])
                                dflist.append(df)
                                bledylist.append(Alglist[i].LiczbaBledowStron)
                                ListaBitowa.append(Alglist[i].ListaBitowa)

                                Alglist[i] = copy.deepcopy(alg)
                                Alglist[i].Queue = data[len(zwrotlista)+k-1]
                                Alglist[i].Ramki = self.WolneRamki
                                self.WolneRamki=0
                                Alglist[i].ListaRamek = [None for x in range(Alglist[i].Ramki)]
                                Alglist[i].HistoriaRamek = np.zeros(shape=(1, Alglist[i].Ramki), dtype=int)
                                break
                            else:
                                flag=False


                                for i in range(len(zwrotlista)):
                                    if(Alglist[i].Queue!=[]):
                                        flag=True
                                if(not flag):
                                    print("KONIEC")
                                    for i in range(len(zwrotlista)):
                                        df = pd.DataFrame(Alglist[i].HistoriaRamek[1:])
                                        dflist.append(df)
                                        bledylist.append(Alglist[i].LiczbaBledowStron)
                                        ListaBitowa.append(Alglist[i].ListaBitowa)
                                        print(Alglist[i].Queue)
                                    break


                    liczbabledow = Alglist[i].ChwilowaLiczbaBledowStron
                    Alglist[i].ChwilowaLiczbaBledowStron=0
                    if(SposobOdwolania[i]!=0):
                        stosunek =liczbabledow/SposobOdwolania[i]
                        print(f'stosunek{stosunek}')
                    else:
                        print("brejk")
                        break
                    if stosunek<self.low:
                        Alglist[i].MozeDacRamke=True
                    elif stosunek>self.high:
                        Alglist[i].ChceRamke=True
                    if stosunek>self.c:
                        Alglist[i].IsShutDown=True
                        Alglist[i].ChceRamke=False
                        self.WolneRamki += Alglist[i].Ramki
                else:
                    if(self.WolneRamki>Alglist[i].Ramki):
                        Alglist[i].IsShutDown=False
                        self.WolneRamki-=Alglist[i].Ramki+1
            SposobOdwolania = distribute_elements(self.szamotuly, len(zwrotlista)) #nowy sposob odwolania

            for i in range(len(zwrotlista)):
                alg1 = Alglist[i]
                if(alg1.MozeDacRamke):
                    alg1.Ramki-=1
                    self.WolneRamki+=1
                    alg1.MozeDacRamke=False
                    alg1.balans-=1
                    alg1.ListaRamek=alg1.ListaRamek[:-1]
                elif(alg1.ChceRamke and self.WolneRamki>0):
                    alg1.Ramki+=1
                    self.WolneRamki-=1
                    alg1.ChceRamke=False
                    alg1.ListaRamek.append(None)
                    alg1.balans+=1
                    alg1.Rozszerzenie+=1
                # if(alg1.IsShutDown):
                #

        return [dflist,bledylist,ListaBitowa]


















        # for i in range(len(zwrotlista)):
        #     alg.Ramki = zwrotlista[i]
        #     alg.Queue = data[i]
        #     alg.ListaRamek = [None for x in range(alg.Ramki)]
        #     alg.HistoriaRamek = np.zeros(shape=(1, alg.Ramki), dtype=int)
        #     while (alg.Queue != []):
        #         alg.process()
        #
        #     df = pd.DataFrame(alg.HistoriaRamek[1:])
        #     dflist.append(df)
        #     bledylist.append(alg.LiczbaBledowStron)
        #     ListaBitowa.append(alg.ListaBitowa)
        #     dlugosc = len(alg.ListaBitowa)
        #     suma = 0
        #     szams = []
        #
        #     #cum sum
        #
        #     for i in range(dlugosc):
        #         if (i % self.szamotuly == 0):
        #             szams.append(suma / self.szamotuly)
        #             suma = alg.ListaBitowa[i]
        #
        #
        #         else:
        #             suma = suma + alg.ListaBitowa[i]
        #
        #     Szamotuly.append(szams[1:])
        #     # dflist.append(dflist)
        #     ListaBitowa.append(ListaBitowa)
        #     bledylist.append(bledylist)
        #     Szamotuly.append(Szamotuly)
        #
        # return [dflist, bledylist, ListaBitowa, Szamotuly]


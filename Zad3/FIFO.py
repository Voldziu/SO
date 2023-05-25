import numpy as np

from Algorythm import Algorythm


class FIFO(Algorythm):
    def __init__(self):
        super().__init__("FIFO")


    def process(self):
        print(len(self.Queue))
        cpr = self.Queue[0]
        print(cpr)


        self.Queue.remove(cpr)
        znalezione = False
        for req in self.ListaRamek:
            if(req!=None):
                if(req.position==cpr.position):
                    znalezione=True


        if (not znalezione):
            print(self.name+": Błąd strony")
            self.LiczbaBledowStron+=1
            self.ListaBitowa.append(1)
            condition = True
            con=True
            i=0
            while(condition and con):
                if(self.ListaRamek[i]!=None):
                    i+=1
                    if(i==self.Ramki):
                        con=False
                else:
                    self.ListaRamek[i]=cpr
                    condition=False
            if(condition): #Jezeli wszystkie ramki są zapelnione
                oldest = min(self.ListaRamek,key=lambda x:x.arrtime)
                indeXoldest = self.ListaRamek.index(oldest)
                self.ListaRamek[indeXoldest]=cpr
        else:
            print(self.name+": Brak błędu strony")
            self.ListaBitowa.append(0)

        newrow = np.array([[x.position if x!=None else 0 for x in self.ListaRamek]])

        self.HistoriaRamek= np.concatenate((self.HistoriaRamek,newrow),axis=0)

        print(self.HistoriaRamek[1:])










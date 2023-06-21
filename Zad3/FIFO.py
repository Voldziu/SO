import numpy as np

from Algorythm import Algorythm


class FIFO(Algorythm):
    def __init__(self):
        super().__init__("FIFO")



    def process(self):

        print(len(self.Queue))

        cpr = self.Queue[0]
        self.KwantowaLista.append(cpr)
        print(self.KwantowaLista)
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
            self.ChwilowaLiczbaBledowStron+=1

            self.ListaBitowa.append(1)

            condition = True
            con=True
            i=0
            while(condition and con):
                # print("chuj2")
                # print(self.Queue)
                # print(self.balans)
                # print(self.IsShutDown)
                # print(self.ListaRamek)


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
        print(f'balans{self.balans}, {self.Rozszerzenie}')
        if(self.balans<0):
            przesuniecie = abs(self.balans)
            print(newrow)
            newrow=np.concatenate((newrow,np.array([przesuniecie*[-1]])),axis=1)
        elif(self.balans>0):

            for _ in range(self.balans):
                self.HistoriaRamek=np.concatenate((self.HistoriaRamek,np.expand_dims(np.array(self.HistoriaRamek.shape[0]*[-1]),axis=1)),axis=1)
            # newrow = np.concatenate((newrow,np.array([(self.Rozszerzenie-self.balans)*[-1]])),axis=1)
            print("lol")
            self.balans = 0



        print(self.HistoriaRamek)
        print(newrow)
        self.HistoriaRamek= np.concatenate((self.HistoriaRamek,newrow),axis=0)

        print(self.HistoriaRamek[1:])










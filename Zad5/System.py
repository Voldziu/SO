import random
from copy import copy

from Alg import Alg
from Procesor import CPU
from Task import Task


class System():
    def __init__(self,alglist:list[Alg],prob:float,N:int):
        self.Alglist:list[Alg]=alglist
        self.prob=prob
        self.N:int=N


    def processAll(self,mode:int,TickLen:int):
        i=0
        gHistoriaObciazen=[]
        gHistoriaOH=[]
        while(i<TickLen):
            if(random.random()<self.prob):

                id = random.randint(0, self.N-1)
                time =0
                p=0
                if(mode==1): #losowe
                    p = random.uniform(0.01,0.7)
                    time=random.randrange(1,101)
                elif(mode==2): #mocne,dlugie
                    p=random.uniform(0.4,0.7)
                    time = random.randrange(80,101)
                elif(mode==3): # slabe, krotkie
                    p = random.uniform(0.01,0.15)
                    time=random.randrange(1,11)
                task = Task(id,round(p,2),time)
                print(round(p,2))

                for alg in self.Alglist:
                    alg.CurrentTask=copy(task)
            for alg in self.Alglist:
                alg.process1tick()
            i=i+1
        for alg in self.Alglist:
            gHistoriaObciazen.append(alg.HistoriaObciazen)
            gHistoriaOH.append(alg.HistoriaOverHeating)
        print(gHistoriaOH)
        print(gHistoriaObciazen)
        return [gHistoriaOH,gHistoriaObciazen]








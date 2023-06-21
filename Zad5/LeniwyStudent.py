import random
from copy import copy

from Alg import Alg
from Procesor import CPU


class LeniwyStudent(Alg):
    def __init__(self ,N: int, p: float, z: int):
        super().__init__(name="leniwystudent", N=N, p=p)
        self.Z:int=z


    def process1tick(self):

        if( self.CurrentTask!=None):
            print(f'{self.CurrentTask.CPUid} dupa')

            print([cpu.id for cpu in self.CPUlist])
            i=0
            lista = copy(self.CPUlist)
            lista=[cpu for cpu in lista if cpu.id!=self.CurrentTask.CPUid]

            while(i<self.Z):

                cpu =random.choice(lista)
                lista.remove(cpu)
                self.IleZapytan+=1
                if(cpu.obciazenie<self.p):

                    self.IleMigracji+=1
                    break #koniec szukania
                i += 1
            if(i==self.Z):
                cpu = [cpu for cpu in self.CPUlist if cpu.id==self.CurrentTask.CPUid][0]
            cpu.taski.append(self.CurrentTask)
            cpu.obciazenie += self.CurrentTask.obciazenie
            self.CurrentTask=None
        super().sub1tick()














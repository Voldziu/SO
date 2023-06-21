from copy import copy
import random

from Alg import Alg


class PoczciwyStudent(Alg):
    def __init__(self ,N: int, p: float):
        super().__init__(name="poczciwystudent", N=N, p=p)



    def process1tick(self):

        if( self.CurrentTask!=None):
            print(f'{self.CurrentTask.CPUid} dupa')

            cpu = [cpu for cpu in self.CPUlist if cpu.id == self.CurrentTask.CPUid][0]
            if(cpu.obciazenie>self.p):

                flag=True
                lista = copy(self.CPUlist)
                lista=[cpu for cpu in lista if cpu.id!=self.CurrentTask.CPUid]
                while(flag and lista!=[]):


                    cpu =random.choice(lista)
                    lista.remove(cpu)
                    self.IleZapytan+=1
                    if(cpu.obciazenie<self.p):

                        self.IleMigracji+=1
                        flag=False #koniec szukania
                if(lista==[]):
                    cpu = [cpu for cpu in self.CPUlist if cpu.id == self.CurrentTask.CPUid][0]
            cpu.taski.append(self.CurrentTask)
            cpu.obciazenie += self.CurrentTask.obciazenie




            self.CurrentTask=None
        super().sub1tick()











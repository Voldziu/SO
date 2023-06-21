from copy import copy
import random

from Alg import Alg


class PoczciwyAltruistycznyStudent(Alg):
    def __init__(self ,N: int, p: float, r:float):
        super().__init__(name="poczciwyaltruistycznystudent", N=N, p=p)
        self.r:float=r


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


        niedociazeni = [cpu for cpu in self.CPUlist if cpu.obciazenie<self.r]
        if(niedociazeni!=[] ):
            for cpu in niedociazeni:
                listacpu = copy(self.CPUlist)
                flag=True
                while(flag and listacpu!=[]):
                    source = random.choice(listacpu)
                    self.IleZapytan+=1
                    if(source.obciazenie>self.p):
                        flag=False
                        cpu.taski=sorted(cpu.taski,key=lambda task:task.obciazenie,reverse=True)

                        while(source.obciazenie>self.p):
                            task = source.taski.pop(0)
                            source.obciazenie=round(source.obciazenie-task.obciazenie,2)
                            print(task.obciazenie)
                            cpu.obciazenie=round(cpu.obciazenie+ task.obciazenie,2)
                            cpu.taski.append(task)
                            self.IleMigracji+=1

                    else:
                        listacpu.remove(source)














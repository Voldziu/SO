import numpy as np

from Procesor import CPU
from Task import Task


class Alg():
    def __init__(self,name:str, N: int, p: float):
        self.name: str = name
        self.N: int = N
        self.p: float = p
        self.CurrentTask: Task = None
        self.CPUlist:list[CPU]=[CPU(i,0,[]) for i in range(N)]
        self.HistoriaObciazen:np.ndarray =np.zeros((1,N),dtype=int)
        self.HistoriaOverHeating:np.ndarray=np.zeros((1,N),dtype=int)
        self.IleZapytan:int=0
        self.IleMigracji:int=0

    def process1tick(self):
        pass


    def sub1tick(self):

        for cpu in self.CPUlist:
            for task in cpu.taski:
                task.czas -= 1
                if (task.czas == 0):
                    cpu.taski.remove(task)
                    cpu.obciazenie = round(cpu.obciazenie- task.obciazenie,2)

            if (cpu.obciazenie > 1):
                cpu.OverHeating = 1
            else:
                cpu.OverHeating = 0
        newrow = np.array([cpu.obciazenie for cpu in self.CPUlist])
        print(newrow)
        self.HistoriaObciazen = np.vstack((self.HistoriaObciazen, newrow))

        rownew = np.array([cpu.OverHeating for cpu in self.CPUlist])
        print()
        print(rownew)
        print()
        self.HistoriaOverHeating=np.vstack((self.HistoriaOverHeating,rownew))

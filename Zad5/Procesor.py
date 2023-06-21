from Task import Task
import numpy as np


class CPU():
    def __init__(self,id:int,obciazenie:float,listaprocesow:list[Task]):
        self.obciazenie:float=obciazenie
        self.taski:list[Task] = listaprocesow
        self.id:int=id
        self.OverHeating:int=0
        self.HistoriaOverHeating:np.ndarray
        self.HistoriaObciazanie:np.ndarray




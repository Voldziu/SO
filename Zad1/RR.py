import functools

from Algorythm import Algorythm
from Request import Request

class RR(Algorythm):
    def __init__(self,k:int):
        super().__init__("RR")
        self.k=k # time quant
        self.i=0 #iterates through tasklist
        self.j=0 #iterates through timeleft
        self.quants=0

    def __repr__(self):

        return "{}: {}".format(self.__class__.__name__, vars(self))

    def initialize(self):
        self.tasklist=sorted(list(self.tasklist),key=functools.cmp_to_key(self.compare))
        self.CPR=self.tasklist[0]
        self.CPR.state = "being processed"



    def work(self):

        print("Before tick:")
        print()
        print(self.CPR)

        if self.tasklist!=[]:
            if(self.j==0):
                self.quants=min(self.k,self.CPR.timeleft)

            if(self.j < self.quants):
                self.CPR.timeleft-=1
                self.CPR.overall_time+=1
                for task in self.tasklist[1:]:

                    if(task.state=="waiting"):
                        task.waiting_time_till_start+=1

                    else:
                        task.overall_time += 1
                self.j+=1
            else:
                if(self.CPR.timeleft==0):
                    self.CPR.state='finished'
                    self.tasklist.remove(self.CPR)
                    self.FinishedCPRList.append(self.CPR)
                else:

                    self.CPR.state="abandonded"

                self.j=0
                self.i +=1
                if(self.tasklist!=[]):
                    self.i=self.i%len(self.tasklist)
                    self.CPR = self.tasklist[self.i]
                    self.CPR.state = "being processed"
                    self.SwitchCounter += 1






            print("After tick:")
            print(self.CPR)
            print(f'SwitchCounter: {self.SwitchCounter}')
            print()
        else:
            print("List empty!")



















































    def compare(self, item1: Request, item2: Request):
        if item1.arrive_time > item2.arrive_time:
            return 1
        elif item1.arrive_time == item2.arrive_time:
            return 0
        else:
            return -1
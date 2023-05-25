import functools

from Algorythm import  Algorythm
from Req import Req


class SCAN(Algorythm):
    def __init__(self):
        super().__init__("SCAN")
        self.GoRight=True
        self.QueueList=[Req]

    def __repr__(self):
        return "{}: {}".format(self.__class__.__name__, vars(self))



    def work(self):
        self.HeaderPositionHistoryList.append(self.HeaderPosition)
        self.PriorityHistoryList.append("Non-Priority")
        if self.tasklist!=[]:
            if self.GoRight:

                self.QueueList=sorted([req for req in self.tasklist if req.Position>=self.HeaderPosition],key=functools.cmp_to_key(self.compare))
            else:
                self.QueueList = sorted([req for req in self.tasklist if req.Position <= self.HeaderPosition],key=functools.cmp_to_key(self.compare2))

            if(self.QueueList!=[]):

                self.CPR= self.QueueList[0]
        if(self.HeaderPosition==self.CPR.Position):
            self.tasklist.remove(self.CPR)
            self.QueueList.remove(self.CPR)
            self.CPR.tickwhenfinished=self.TimeNeeded
            self.CompletedTasksList.append(self.CPR)




        if(self.GoRight and self.HeaderPosition<self.DiskLen):
            self.HeaderPosition+=1

        elif(self.HeaderPosition==self.DiskLen):
            self.GoRight=False
            self.HeaderPosition-=1

        elif( not self.GoRight and self.HeaderPosition>0):
            self.HeaderPosition-=1
        elif(self.HeaderPosition==0):
            self.GoRight=True
            self.HeaderPosition+=1
        for task in self.tasklist:
            task.waitingtime += 1


        self.TimeNeeded+=1

        return len(self.CompletedTasksList)

    def compare(self, item1: Req, item2: Req):
        if item1.Position >item2.Position:
            return 1
        elif item1.Position ==item2.Position:
            return 0
        else:
            return -1

    def compare2(self, item1: Req, item2: Req):
        if item1.Position <item2.Position:
            return 1
        elif item1.Position ==item2.Position:
            return 0
        else:
            return -1














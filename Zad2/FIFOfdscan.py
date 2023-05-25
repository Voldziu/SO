import functools

from Algorythm import Algorythm
from Req import Req


class FIFOdfscan(Algorythm):


    def __init__(self):
        super().__init__("FIFOfdscan")
        self.WasPriority:bool = False
        self.flagOver=True
        self.PossiblePriorityStart = False
        self.GoRight=False
        self.CPR2:Req
        self.QueueList=[Req]
        self.Abandonded=[Req]




    def __repr__(self):
        return "{}: {}".format(self.__class__.__name__, vars(self))

    def initialize(self):
        self.CPR= self.tasklist[0]




    def work(self):
        if(self.PriorityList!=[] and self.PossiblePriorityStart):

            if not self.Priority:
                self.flagOver=True
            self.Priority=True
        else:
            if(self.Priority):
                self.WasPriority=True
            self.Priority=False
            self.PossiblePriorityStart=False
        self.TimeNeeded += 1

        if(self.Priority):
            self.HeaderPositionHistoryList.append(self.HeaderPosition)
            self.PriorityHistoryList.append("Priority")
            if(self.flagOver):
                dupa = self.PriorityList

                self.PriorityList   = [req for req in self.PriorityList if req.Priority>=abs(self.HeaderPosition-req.Position)]
                self.Abandonded = [req for req in dupa if req not in self.PriorityList]

                if(self.PriorityList!=[]):
                    self.CPR =sorted(self.PriorityList,key=functools.cmp_to_key(self.compare))[0]
                else:
                    return
                print(self.CPR)
                print("--------------------------------------------")
                self.flagOver=False

            print(self.name)
            print(f'Before tick:\t Header position: {self.HeaderPosition}\t')
            print()
            print(f'Going towards: {self.CPR.Position}')



            if (self.CPR.Position > self.HeaderPosition):
                self.GoRight=True
            elif(self.CPR.Position < self.HeaderPosition):
                self.GoRight=False

            if self.GoRight:

                self.QueueList=sorted([req for req in self.tasklist if req.Position>=self.HeaderPosition],key=functools.cmp_to_key(self.compare3))
            else:
                self.QueueList = sorted([req for req in self.tasklist if req.Position <= self.HeaderPosition],key=functools.cmp_to_key(self.compare4))
            if(self.QueueList!=[]):

                self.CPR2 = self.QueueList[0]
            else:
                self.CPR2=None


            if(self.HeaderPosition==self.CPR.Position):
                if(self.CPR in self.tasklist):
                    self.tasklist.remove(self.CPR)
                if(self.CPR in self.PriorityList):

                    self.PriorityList.remove(self.CPR)

                print("usunieto usunietousunietousunietousunietousunietousunietousunietousunietousunieto")
                if(self.PriorityList!=[]):
                    self.flagOver=True






            elif (self.HeaderPosition == self.CPR2.Position):
                self.tasklist.remove(self.CPR2)

                self.CompletedTasksList.append(self.CPR2)
                self.CPR2.tickwhenfinished=self.TimeNeeded
                print("----------------------------------------------------")




            if (self.GoRight and self.HeaderPosition < self.DiskLen):
                self.HeaderPosition += 1

            elif (self.HeaderPosition == self.DiskLen):
                self.GoRight = False
                self.HeaderPosition -= 1

            elif (not self.GoRight and self.HeaderPosition > 0):
                self.HeaderPosition -= 1
            elif (self.HeaderPosition == 0):
                self.GoRight = True
                self.HeaderPosition += 1






            for task in self.PriorityList:
                task.Priority -= 1

                if(task.Priority==0):
                    self.MissedPriorityTasks.append(task)
                    self.CompletedTasksList.append(task)
                    if (self.CPR in self.tasklist):
                        print("chuj")
                        self.tasklist.remove(self.CPR)
                    if (self.CPR in self.PriorityList):
                        self.PriorityList.remove(self.CPR)
                    task.tickwhenfinished=self.TimeNeeded
                    if(task==self.CPR):
                        print("chuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuj")
                        if self.PriorityList!=[]:

                            self.flagOver=True

            for task in self.Abandonded:
                task.Priority =0
                self.MissedPriorityTasks.append(task)
                self.CompletedTasksList.append(task)
                if(task in self.tasklist):
                    self.tasklist.remove(task)
                self.Abandonded.remove(task)
                task.tickwhenfinished = self.TimeNeeded











        else:
            if len(self.tasklist)==1 or self.WasPriority:
                self.CPR=self.tasklist[0]
                self.WasPriority=False

            self.HeaderPositionHistoryList.append(self.HeaderPosition)
            self.PriorityHistoryList.append("Non-Priority")
            print(self.name)
            print(f'Before tick:\t Header position: {self.HeaderPosition}\t')
            print()
            print(f'Going towards: {self.CPR.Position}')



            if(self.tasklist!=[]):


                if(self.CPR.Position>self.HeaderPosition):
                    self.HeaderPosition+=1 #
                else:
                    self.HeaderPosition-=1


                if(self.HeaderPosition ==self.CPR.Position):
                    self.tasklist.remove(self.CPR)
                    self.PossiblePriorityStart=True



                    self.CPR.tickwhenfinished=self.TimeNeeded

                    self.CompletedTasksList.append(self.CPR)
                    if(self.tasklist!=[]):
                        self.CPR=self.tasklist[0]

                for task in self.tasklist:
                    task.waitingtime+=1




            else:
                print("List empty, skipping tick.....")
            print(f'After tick:\t Header position: {self.HeaderPosition}')


            return len(self.CompletedTasksList)

    def compare(self, item1: Req, item2: Req):
        if abs(item1.Position - self.HeaderPosition) > abs(item2.Position - self.HeaderPosition):
            return 1
        elif abs(item1.Position - self.HeaderPosition) == abs(item2.Position - self.HeaderPosition):
            return 0
        else:
            return -1



    def compare2(self, item1: Req, item2: Req):
        if abs(item1.Position - self.HeaderPosition) < abs(item2.Position - self.HeaderPosition):
            return 1
        elif abs(item1.Position - self.HeaderPosition) == abs(item2.Position - self.HeaderPosition):
            return 0
        else:
            return -1

    def compare3(self, item1: Req, item2: Req):
        if item1.Position >item2.Position:
            return 1
        elif item1.Position ==item2.Position:
            return 0
        else:
            return -1

    def compare4(self, item1: Req, item2: Req):
        if item1.Position <item2.Position:
            return 1
        elif item1.Position ==item2.Position:
            return 0
        else:
            return -1


















import functools

from Algorythm import Algorythm
from Req import Req


class FIFOedf(Algorythm):


    def __init__(self):
        super().__init__("FIFOedf")
        self.WasPriority:bool = False
        self.flagOver=True
        self.PossiblePriorityStart = False





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
            if(self.flagOver):
                self.CPR =sorted(self.PriorityList,key=functools.cmp_to_key(self.compare))[0]
                print(self.CPR)
                print("--------------------------------------------")
                self.flagOver=False
            self.HeaderPositionHistoryList.append(self.HeaderPosition)

            self.PriorityHistoryList.append("Priority")


            print(self.name)
            print(f'Before tick:\t Header position: {self.HeaderPosition}\t')
            print()
            print(f'Going towards: {self.CPR.Position}')






            if (self.CPR.Position > self.HeaderPosition):
                self.HeaderPosition += 1
            elif(self.CPR.Position < self.HeaderPosition):
                self.HeaderPosition -= 1

            elif (self.HeaderPosition == self.CPR.Position):
                self.tasklist.remove(self.CPR)
                self.PriorityList.remove(self.CPR)
                self.CompletedTasksList.append(self.CPR)
                self.CPR.tickwhenfinished=self.TimeNeeded
                print("----------------------------------------------------")
                self.flagOver=True




            for task in self.PriorityList:
                task.Priority -= 1

                if(task.Priority==0):
                    self.MissedPriorityTasks.append(task)
                    self.CompletedTasksList.append(task)
                    self.tasklist.remove(task)
                    self.PriorityList.remove(task)
                    task.tickwhenfinished=self.TimeNeeded
                    if(task==self.CPR):
                        print("chuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuj")
                        self.flagOver=True










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
        if item1.Priority >item2.Priority:
            return 1
        elif item1.Priority ==item2.Priority:
            return 0
        else:
            return -1


















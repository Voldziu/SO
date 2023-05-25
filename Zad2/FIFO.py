from Algorythm import Algorythm


class FIFO(Algorythm):


    def __init__(self):
        super().__init__("FIFO")

    def __repr__(self):
        return "{}: {}".format(self.__class__.__name__, vars(self))

    def initialize(self):
        self.CPR= self.tasklist[0]




    def work(self):
        if len(self.tasklist)==1:
            self.CPR=self.tasklist[0]

        self.HeaderPositionHistoryList.append(self.HeaderPosition)
        self.PriorityHistoryList.append("Non-Priority")
        print(self.name)
        print(f'Before tick:\t Header position: {self.HeaderPosition}\t')
        print()
        print(f'Going towards: {self.CPR.Position}')

        self.TimeNeeded+=1

        if(self.tasklist!=[]):


            if(self.CPR.Position>self.HeaderPosition):
                self.HeaderPosition+=1 #
            else:
                self.HeaderPosition-=1


            if(self.HeaderPosition ==self.CPR.Position):
                self.tasklist.remove(self.CPR)
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


















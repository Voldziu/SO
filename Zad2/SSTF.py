import functools

from Algorythm import Algorythm
from Req import Req


class SSTF(Algorythm):
    def __init__(self):
        super().__init__("SSTF")

    def __repr__(self):
        return "{}: {}".format(self.__class__.__name__, vars(self))

    def initialize(self):
        self.tasklist = sorted(list(self.tasklist), key=functools.cmp_to_key(self.compare))
        self.CPR = self.tasklist[0]


    def work(self):

        if (self.flagOver):
            self.tasklist = sorted(list(self.tasklist), key=functools.cmp_to_key(self.compare))
            self.flagOver = False
            if(self.tasklist!=[]):
                self.CPR=self.tasklist[0]
        if len(self.tasklist) == 1:
            self.CPR = self.tasklist[0]
        self.HeaderPositionHistoryList.append(self.HeaderPosition)
        self.PriorityHistoryList.append("Non-Priority")
        print(self.name)
        print(f'Before tick:\t Header position: {self.HeaderPosition}\t')
        print()
        print(f'Going towards: {self.CPR.Position}')

        if (self.tasklist != []):

            if (self.CPR.Position > self.HeaderPosition):
                self.HeaderPosition += 1  #
            else:
                self.HeaderPosition -= 1

            if (self.HeaderPosition == self.CPR.Position):
                self.tasklist.remove(self.CPR)
                self.flagOver = True
                self.CPR.tickwhenfinished = self.TimeNeeded
                self.CompletedTasksList.append(self.CPR)

            else:
                for task in self.tasklist:
                    task.waitingtime+=1



        else:
            print("List empty, skipping tick.....")
        print(f'After tick:\t Header position: {self.HeaderPosition}')

        self.TimeNeeded += 1

        return len(self.CompletedTasksList)

    def compare(self, item1: Req, item2: Req):
        if abs(item1.Position - self.HeaderPosition) > abs(item2.Position - self.HeaderPosition):
            return 1
        elif abs(item1.Position - self.HeaderPosition) == abs(item2.Position - self.HeaderPosition):
            return 0
        else:
            return -1

    # def compare(self, item1: Req, item2: Req):
    #     if item1.Position >item2.Position:
    #         return 1
    #     elif item1.Position ==item2.Position:
    #         return 0
    #     else:
    #         return -1

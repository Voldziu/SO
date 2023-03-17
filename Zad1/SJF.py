import functools

from Algorythm import Algorythm
from Request import Request


class FCFS2(Algorythm):
    def __init__(self):
        super().__init__("SJF")

    def __repr__(self):

        return "{}: {}".format(self.__class__.__name__, vars(self))

    def work(self):
        if self.tasklist!=[]:

            self.tasklist = sorted(list(self.tasklist), key=functools.cmp_to_key(self.compare))
            self.CPR=self.tasklist[0]
        if len(self.tasklist)==1:
            self.CPR = self.tasklist[0]
            self.CPR.state = "started"
        print("Before tick:")
        print()
        print(self.CPR)

        if self.tasklist != []:

            if (self.CPR.timeleft == 0):

                self.CPR.state = "finished"
                self.SwitchCounter += 1
                self.tasklist.remove(self.CPR)
                self.FinishedCPRList.append(self.CPR)
                if (self.tasklist != []):
                    self.CPR = self.tasklist[0]
                    self.CPR.state = "started"



            else:
                self.CPR.timeleft -= 1
                self.CPR.overall_time += 1
                for cpr in self.tasklist[1:]:
                    cpr.waiting_time_till_start += 1
                    cpr.overall_time += 1
            print("After tick:")
            print(self.CPR)
            print(f'SwitchCounter: {self.SwitchCounter}')
            print()
        else:
            print("List empty!")

    def compare(self, item1: Request, item2: Request):
        if item1.processing_time > item2.processing_time:
            return 1
        elif item1.processing_time == item2.processing_time:
            return 0
        else:
            return -1

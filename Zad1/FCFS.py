import functools

from Algorythm import Algorythm
from Request import Request
class FCFS(Algorythm):
    def __init__(self):
        pass



    def work(self,InitialRequest,TickLimit,GlobalCurrentTick):

        RequestList = sorted(list(InitialRequest), key=functools.cmp_to_key(self.compare))
        print("chuj")

        return RequestList




    def compare(self,item1:Request,item2:Request):
        if item1.arrive_time>item2.arrive_time:
            return 1
        elif item1.arrive_time== item2.arrive_time:
            return 0
        else:
            return -1


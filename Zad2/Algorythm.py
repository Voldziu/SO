from Req import Req


class Algorythm:
    def __init__(self,name:str):
        self.name = name
        self.tasklist:list[Req] = []
        self.MissedPriorityTasks=[]
        self.TimeNeeded=0
        self.HeaderPosition=0
        self.DiskLen=0
        self.CompletedTasksList=[]
        self.CPR:Req = Req(0,0,0,"0")
        self.HeaderPositionHistoryList=[int]
        self.flagOver=False
        self.Priority: bool = False
        self.PriorityList:list[Req]=[]
        self.PriorityHistoryList = []






    def work(self):
        pass
    def initialize(self):
        pass


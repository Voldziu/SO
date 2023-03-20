from Request import Request


class Algorythm:
    def __init__(self,name):

        self.name=name
        self.tasklist:list=[]
        self.GlobalCurrentTick=0
        self.SwitchCounter=0
        self.CPR:Request=Request(0,0,0,0,0,0)
        self.FinishedCPRList=[]



    def work(self):
        pass
    def initialize(self):
        pass
class Req:

    def __init__(self,id:int, Position :int, Priority:int,algname:str):
        self.id=id
        self.Position=Position
        self.Priority=Priority
        self.algname=algname
        self.waitingtime=0
        self.tickwhenfinished=0






    def __str__(self):
        return f'Request   Position: {self.Position}  WaitingTime: {self.waitingtime} Priority: {self.Priority}'



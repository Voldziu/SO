class Req1:
    def __init__(self,position:int,arrtime:int):
        self.position = position
        self.arrtime = arrtime
        self.BitZycia=1



    def __str__(self):
        return f'Position: {self.position}'

    def __repr__(self):
        return str(self)
    def __eq__(self, other):
        if(isinstance(other,self.__class__)):
            return self.position==other.position
        else:
            return False





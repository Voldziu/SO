import numpy as np
import pandas as pd

# l =np.array([[100,100,100],[200,200,200],[300,300,300]])
# p= np.zeros(shape=(1,3),dtype=int)
#
# newrow = np.array([[1,2,3]])
# p = np.concatenate((p,newrow),axis=0)
# df = pd.DataFrame(p,index=None)
# print(df)
#
l=[1,2,3]
l[1]="chuj"
print(l)

class Dog:
    def __init__(self,how,like):
        self.how = how
        self.like = like
    def __eq__(self, other):
        return self.how ==other.how


list = [Dog("lol",1),Dog("lol",2),Dog("lol",3),Dog("pies",1)]
list2 =[Dog("lol",1)]






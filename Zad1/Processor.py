import random
import numpy as np
import Algorythm

from FCFS import FCFS
from Request import Request

TickLimit = 10
GlobalTickLimit = 0

tasklist = [Request(1, "lol", 4, 10, "waiting"), Request(1, "lol", 3, 10, "waiting"),
            Request(1, "lol", 2, 10, "waiting")]




def NewTaskArrival(id, tasklist, lengthlevel):
    p = 0
    if lengthlevel == 1:
        p = abs(round(np.random.normal(10, 5)))
    elif lengthlevel == 2:
        p = abs(round(np.random.normal(50, 16)))
    elif lengthlevel == 3:
        p = abs(round(np.random.normal(80, 5)))

    tasklist.add(Request(id, 'lol', 0, p, "waiting"))


def RandomTaskLength(mean, std):
    p = abs(round(np.random.normal(mean, std)))
    return p


def NewTaskArrivalBoolean(k):
    if random.random() >= k:
        return True
    else:
        return False





def Processing(algorythm:Algorythm):
    algorythm.work(tasklist,TickLimit,GlobalTickLimit)










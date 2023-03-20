import random
import numpy as np
import Algorythm
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from FCFS import FCFS
from Request import Request




# tasklist = [
#             Request(1, "lol", 2, 0, "waiting")]




def NewTaskArrival(id,Algname, tasklist, lengthlevel):
    p = 0
    if lengthlevel == 1:
        p = abs(round(np.random.normal(10, 5)))
    elif lengthlevel == 2:
        p = abs(round(np.random.normal(50, 16)))
    elif lengthlevel == 3:
        p = abs(round(np.random.normal(80, 5)))

    tasklist.append(Request(id, 'lol', 0, p, "waiting",Algname))



def RandomTaskLength(mean, std):
    p = abs(round(np.random.normal(mean, std)))
    return p


def NewTaskArrivalBoolean(k):
    if random.random() >= k:
        return True
    else:
        return False





def Processing(algorythm:Algorythm):
    tasklist = [Request(1, "lol", 4, 10, "waiting",algorythm.name), Request(2, "lol", 3, 10, "waiting",algorythm.name),
                Request(3, "lol", 2, 1, "waiting",algorythm.name)]
    SwitchCounter=0
    TickLimit = 100
    GlobalCurrentTick = 0
    CPR:Request=Request(0,0,0,0,0,"name")
    FinishedCPRList=[]
    ID=len(tasklist)+1


    while GlobalCurrentTick<TickLimit:
        print(GlobalCurrentTick)
        if (NewTaskArrivalBoolean(0.01)):
            NewTaskArrival(ID,algorythm.name, tasklist, 1)
            ID+=1
        algorythm.work()





        GlobalCurrentTick+=1


    for task in FinishedCPRList:
        print(task)
    df= pd.DataFrame.from_records(vars(o) for o in FinishedCPRList)
    print(df.describe())
    print(df.columns)
    df_new = (df.iloc[:,[0,1,5,6,7,8]])
    print(df_new.head())




def ProcessingAll(AlgList:list):
    TickLimit = 10**5
    GlobalCurrentTick = 0
    Switchcounter = 0
    FinishedCPRList=[]


    for alg in AlgList:  # Initializing

        alg.tasklist = [Request(1, "lol", 4, 30, "waiting", alg.name),
                    Request(2, "lol", 3, 10, "waiting", alg.name),
                    Request(3, "lol", 2, 1, "waiting", alg.name)]
        alg.GlobalCurrentTick=GlobalCurrentTick
        alg.SwitchCounter=Switchcounter
        alg.FinishedCPRList=FinishedCPRList
        alg.initialize()







    ID= len(AlgList[0].tasklist)+1

    while GlobalCurrentTick<TickLimit:
        print(GlobalCurrentTick)

        NewTaskBoolean = NewTaskArrivalBoolean(0.95)


          # TO DO: wspolbiezne dzialanie algorytmow

        if(NewTaskBoolean):
            for alg in AlgList:
                NewTaskArrival(ID,alg.name,alg.tasklist,2)
            ID+=1     
        for alg in AlgList:

            alg.work()
            alg.GlobalCurrentTick+=1



        GlobalCurrentTick+=1

    DFList=[]
    for alg in AlgList:


        DFList+=alg.FinishedCPRList
    df = pd.DataFrame.from_records(vars(o) for o in DFList)
    column_list= list(df[["processing_time","waiting_time_till_start","overall_time"]].columns)
    print(df.columns)
    print(column_list)
    fig, axes = plt.subplots(1,3,figsize=(20,10))



    sns.violinplot(data=df, x="algname", y="waiting_time_till_start", ax=axes[0])
    sns.violinplot(data=df, x="algname", y="overall_time", ax=axes[1])
    sns.violinplot(data=df,x="algname",y="processing_time",ax=axes[2])

    # sns.histplot(data=df,x="processing_time",hue="algname")
    plt.show()




























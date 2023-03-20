import random
import numpy as np
import Algorythm
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from FCFS import FCFS
from Request import Request

from FCFS import FCFS
from SJF import SJF
from RR import RR



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
    SwitchCounterList=[]
    NameList=[]
    for alg in AlgList:
        NameList.append(alg.name)
        SwitchCounterList.append(alg.SwitchCounter)




        DFList+=alg.FinishedCPRList

    cprdata = pd.DataFrame.from_records(vars(o) for o in DFList)
    SwitchCounterDict = {'Alg_Name': NameList,'No_of_switches': SwitchCounterList}




    Switchdata=pd.DataFrame.from_dict(data=SwitchCounterDict)
    return [cprdata,Switchdata]





def ShowData():
    datalist=ProcessingAll([SJF(),FCFS(),RR(10)])
    df=datalist[0]
    Switchdata=datalist[1]
    print(Switchdata)
    print(df)
    column_list = list(df[["processing_time", "waiting_time_till_start", "overall_time"]].columns)
    print(df.columns)
    print(column_list)
    fig, axes = plt.subplots(4, 3, figsize=(28, 12))

    sns.violinplot(data=df, x="algname", y="waiting_time_till_start", ax=axes[0,0])
    sns.violinplot(data=df, x="algname", y="overall_time", ax=axes[0,1])
    sns.violinplot(data=df, x="algname", y="processing_time", ax=axes[0,2])


    sns.histplot(data=df,x="waiting_time_till_start",hue="algname",ax=axes[1,0],kde=True)
    sns.histplot(data=df, x="overall_time", hue="algname", ax=axes[1,1],kde=True)
    sns.histplot(data=df, x="processing_time", hue="algname", ax=axes[1, 2],kde=True)

    sns.histplot(data=Switchdata,x="Alg_Name",y="No_of_switches",ax=axes[2,0])



    plt.show()




























import random

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

import Algorythm
from CSCAN import CSCAN
from FIFO import FIFO
from Req import Req
from SSTF import SSTF
from Scan import SCAN
from FIFOedf import FIFOedf
from FIFOfdscan import  FIFOdfscan


def NewTaskLen(lengthlevel, n):
    p = 0
    priority = 0
    plist = []
    if lengthlevel == 1:
        p = random.randint(0, n)  ## random
    elif lengthlevel == 2:
        pstart = abs(round(np.random.normal(n / 2, n / 6)))

        plist.append(round(n / 2) + pstart)  ##edges
        plist.append(-round(n / 2) + pstart)
        if (pstart <= 250):
            p = plist[0]
        else:
            p = plist[1]

            # XDDDD
    elif lengthlevel == 3:
        p = abs(round(np.random.normal(n / 2, n / 6)))  ## normal dist

    # if(Priorityboolean):
    #     priority = np.random.normal(n/3,n/20)

    return p


def NewPriorityLen(n):
    return round(abs(np.random.normal(n / 3, n / 20)))


# def NewTaskArrival(id, Algname, len, n, plen: int):
#     return Req(id, len, plen, Algname)


def NewTaskArrivalBoolean(k):
    if random.random() <= k:
        return True
    else:
        return False


def NewPriorityBoolean(k):  ## 1/3 - 1/10 normalnych taskow

    if random.random() <= k:
        return True
    else:
        return False


def processingAllParalelly(Alglist: list[Algorythm], HeaderPosition: int, DiscSpaceLen: int, Limit: int, mode: int,tasklen:int):
    for alg in Alglist:
        alg.tasklist = [Req(1, 20, -1, algname=alg.name)]
        alg.HeaderPosition = HeaderPosition
        alg.DiskLen = DiscSpaceLen
        alg.initialize()

    if mode == 1:
        # TickLimit

        for i in range(Limit):
            if (NewTaskArrivalBoolean(0.05)):
                len = NewTaskLen(tasklen, n=DiscSpaceLen)
                plen = -1
                newtaskboolen = NewTaskArrivalBoolean(0.01)
                if (newtaskboolen):
                    plen = NewPriorityLen(DiscSpaceLen)


                for alg in Alglist:
                    NewRequest = Req(1, len, plen, alg.name)
                    alg.tasklist.append(NewRequest)
                    if(newtaskboolen):
                        alg.PriorityList.append(NewRequest)


            for alg in Alglist:
                alg.work()

        for alg in Alglist:
            print(alg.HeaderPositionHistoryList)
            print("[{}]".format(", ".join(str(obj) for obj in alg.CompletedTasksList)))







    # elif mode == 2:
    #     tasklen = 0
    #     # TaskLimit
    #
    #     while (Limit > tasklen):
    #         if (NewTaskArrivalBoolean(0.1)):
    #             leng = NewTaskLen(1, n=DiscSpaceLen)
    #             plen = -1
    #             if (NewTaskArrivalBoolean(0.03)):
    #                 plen = NewPriorityLen(DiscSpaceLen)
    #
    #             for alg in Alglist:
    #                 # NewTaskArrival(1, alg.name, alg.tasklist, leng, DiscSpaceLen, plen)
    #
    #         for alg in Alglist:
    #             tasklen = max(tasklen, alg.work())
    #     for alg in Alglist:
    #         print(alg.HeaderPositionHistoryList)
    #         print("[{}]".format(", ".join(str(obj) for obj in alg.CompletedTasksList)))

    NameList = []
    HeaderHistoryListofLists = []
    CompletedTaskLists = []
    dict = {}
    dict2 = {}

    for alg in Alglist:

        NameList.append(alg.name)

        dict[alg.name] = alg.HeaderPositionHistoryList[1:]
        dict[alg.name+"Priority"]=alg.PriorityHistoryList
        CompletedTaskLists += alg.CompletedTasksList



    return [pd.DataFrame(dict), pd.DataFrame.from_records(vars(o) for o in CompletedTaskLists)]


def ShowData():
    tasklist = [Req(1, 20, -1, "fifo")]
    startingposition = 250
    DiskLen=500
    Ticks= 10000
    taskmode=3
    taskmodestring=""
    if(taskmode==1):
        taskmodestring="Taski pojawiają się losowo"
    elif(taskmode==2):
        taskmodestring="Taski pojawiają się na krańcach, modyfikacja rozkładu normalnego"
    elif taskmode==3:
        taskmodestring="Taski pojawiają się zgodnie z rozkładem normalnym. Mean:n/2, std: n/6"


    fig, axes = plt.subplots(4, 4, figsize=(20, 20))
    fig.suptitle(f'Witam, to wykresiki analizy algorytmów.\n Długość dysku: {DiskLen}   Pozycja startowa: {startingposition}   Liczba Ticków: {Ticks}   Tryb: {taskmodestring}',fontsize=20)



    dfs = processingAllParalelly([SSTF(), FIFO(), SCAN(), CSCAN(),FIFOedf(),FIFOdfscan()], startingposition,DiskLen, Ticks, 1,taskmode)
    df = dfs[0]
    df2 = dfs[1]

    df2["status"] = np.select([(df2['Priority']==-1),(df2['Priority']==0) | (df2['Priority']<-1),(df2['Priority']>0)] , ["Non-priority","Missed","Caught"])
    df2["color"] = np.select([(df2["status"]=="Non-priority"),(df2["status"]=="Missed"),(df2["status"]=="Caught")],["royalblue","chartreuse","firebrick"])
    df["fifoedfcolor"]= np.select([(df["FIFOedfPriority"]=="Non-Priority"),(df["FIFOedfPriority"]=="Priority")],["royalblue","firebrick"])


    print(df)
    print(df2)
    print(df2[df2["status"]=="Missed"])

    df2reduced = df2.iloc[:, [1, 3, 4, 5,6,7]]

    dfsstf = df2reduced[df2reduced["algname"] == "SSTF"]

    dffifo = df2reduced[df2reduced["algname"] == "FIFO"]
    dfscan = df2reduced[df2reduced["algname"] == "SCAN"]
    dfcscan = df2reduced[df2reduced["algname"] == "CSCAN"]
    dffifoedf = df2reduced[df2reduced["algname"]=="FIFOedf"]
    dffifofdscan = df2reduced[df2reduced["algname"]=="FIFOfdscan"]

    print(dffifoedf)

    palette = {"Non-priority": "royalblue", "Caught": "chartreuse", "Missed": "firebrick"}
    palette1 = sns.color_palette("husl", len(dffifoedf["color"].unique()))


    sns.scatterplot(dfsstf, y="Position", x="tickwhenfinished", ax=axes[0, 0], hue="waitingtime", legend=False, color='royalblue')
    sns.scatterplot(dffifo, y="Position", x="tickwhenfinished", ax=axes[0, 1], hue="waitingtime", legend=False)
    sns.scatterplot(dfscan, y="Position", x="tickwhenfinished", ax=axes[0, 2], color="orange", hue="waitingtime",
                    legend=False)
    sns.scatterplot(dfcscan, y="Position", x="tickwhenfinished", ax=axes[0, 3], color="yellow", hue="waitingtime",
                    legend=False)


    sns.lineplot(df["SSTF"], ax=axes[1, 0], color="red")
    sns.lineplot(df["FIFO"], ax=axes[1, 1], color="blue")
    sns.lineplot(df["SCAN"], ax=axes[1, 2], color="orange")
    sns.lineplot(df["CSCAN"], ax=axes[1, 3], color="yellow")
    sns.scatterplot(dfsstf, y="Position", x="tickwhenfinished", ax=axes[2, 0], hue="waitingtime", legend=False,
                    color='royalblue')
    sns.scatterplot(dffifo, y="Position", x="tickwhenfinished", ax=axes[2, 1], hue="waitingtime", legend=False)
    sns.scatterplot(dfscan, y="Position", x="tickwhenfinished", ax=axes[2, 2], color="orange", hue="waitingtime",
                    legend=False)
    sns.scatterplot(dfcscan, y="Position", x="tickwhenfinished", ax=axes[2, 3], color="yellow", hue="waitingtime",
                    legend=False)

    sns.lineplot(df["SSTF"], ax=axes[2, 0], color="red")
    sns.lineplot(df["FIFO"], ax=axes[2, 1], color="blue")
    sns.lineplot(df["SCAN"], ax=axes[2, 2], color="orange")
    sns.lineplot(df["CSCAN"], ax=axes[2, 3], color="yellow")
    plt.show()

    fg, xx = plt.subplots(1,2,figsize=(20,10))
    plt.tight_layout()
    sns.scatterplot(dffifoedf, y="Position", x="tickwhenfinished", ax=xx[0], hue="status", palette=palette)




    sns.scatterplot(dffifoedf, y="Position", x="tickwhenfinished", ax=xx[1], hue="status", palette=palette,legend=False)
    sns.lineplot(df["FIFOedf"], ax=xx[1], color="grey")

    fig1, ax1 = plt.subplots(1,2,figsize=(20,10))
    plt.tight_layout()
    sns.scatterplot(dffifofdscan, y="Position", x="tickwhenfinished", ax=ax1[0], hue="status", palette=palette)

    sns.scatterplot(dffifofdscan, y="Position", x="tickwhenfinished", ax=ax1[1], hue="status", palette=palette,legend=False)
    sns.lineplot(df["FIFOfdscan"], ax=ax1[1], color="grey")




    # for i in range(0, len(df["FIFOedf"])):
    #     print(i)
    #     if(df["FIFOedfPriority"][i]=="Non-Priority"):
    #
    #         sns.lineplot(df["FIFOedf"][i:i+2],
    #              color="blue", ax=xx[2], linewidth=0.5)
    #     else:
    #         sns.lineplot(df["FIFOedf"][i:i+2],
    #                      color="red", ax=xx[2], linewidth=0.5)




    plt.show()

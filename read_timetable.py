import pandas as pd
import math
from datetime import datetime,date

def set_all_data():
    df = pd.read_excel (path_table)
    xl=df.to_numpy().tolist()
    
    for i in range(len(xl)):
        if i==0:
            global times
            times=xl[0][1:]
        else:
            table[xl[i][0]]=[]
            for j in range(1,len(xl[i])):
                table[xl[i][0]].append(xl[i][j])
def get_sub():
    today=date.today().weekday()
    now_time=datetime.now().strftime("%H:%M")
    period=get_class(now_time)
    if period=="none":
        return period
    if days[today] not in table:
        return math.nan
    return table[days[today]][period]
def get_class(cur_time):
    for x in range(len(times)):
        i=times[x].split(" ")
        left_time=time_left(cur_time,i[0].strip())
        if -35<left_time<=15:
            return x
    return "none"
def time_left(now,targ):
    x=now.split(':')
    y=targ.split(':')
    x[0]=int(x[0])
    x[1]=int(x[1])
    y[0]=int(y[0])
    y[1]=int(y[1])
    hrs=0
    if x[0]>12:
        if y[0]<=12:
            hrs=24-x[0]+y[0]
    if y[0]>12:
        if x[0]<=12:
            hrs=y[0]-x[0]
    if hrs==0:
        hrs=y[0]-x[0]
    diff=hrs*60+(int(y[1])-int(x[1]))
    return diff

def get_time(unit):
    today=date.today().weekday()
    ind=-1
    if unit=="lunch":
        ind=table[days[today]].index(unit)
        return times[ind].split(" ")[2]
    elif unit=="start":
        return times[0].split(" ")[0]
    elif unit=="end":
        return times[-1].split(" ")[2]

times=[]
table={}
path_table=r"path"                                                                              #Add the path for tiime table here
days =["MON", "TUE", "WED", "THU", "FRI","SAT","SUN"]
set_all_data()

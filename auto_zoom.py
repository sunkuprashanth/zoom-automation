import os,psutil,time,math,numpy
from read_timetable import get_sub,time_left,get_time
from datetime import datetime
from win32gui import GetWindowText, GetForegroundWindow
from pynput.mouse import Button,Controller
mouse=Controller()
from pynput.keyboard import Key,Controller
key_b=Controller()

meet_id={"subject_name":"id"}
meet_pass={"subject_name":"password"}                                                   #The subject name must same as the one in time table
sub=""
path=r"path"                                                                            #Add the path to your zoom app here
now=datetime.now().strftime("%H:%M")
start_time=get_time("start")
end_time=get_time("end")
while(now<start_time or now>end_time):
    now=datetime.now().strftime("%H:%M")
    slp=time_left(now,"09:30")*60
    print("sleeping for ",slp/60," mins until ",start_time)
    time.sleep(slp+6)
while (start_time<=datetime.now().strftime("%H:%M")<=end_time):
    sub=get_sub()
    if isinstance(sub,float):
        break
    if sub=="lunch":
        now=datetime.now().strftime("%H:%M")
        lunch_sleep=time_left(now,get_time("lunch"))
        print("process in sleep for lunch for ",lunch_sleep," mins")
        time.sleep(lunch_sleep*60)
        continue
    os.startfile(path)
    join_meet=(600,355)
    active=False
    while(not active):
        if "Zoom"==GetWindowText(GetForegroundWindow()):
            active=True
        else:
            os.startfile(path)
            active=False
    time.sleep(2)
    mouse.position=join_meet
    mouse.click(Button.left,1)
    time.sleep(2)
    mt_id=meet_id[sub]
    mt_pass=meet_pass[sub]
    key_b.type(mt_id)
    turnoff_audio=(675,480)
    turnoff_video=(670,506)
    join_meet=(795,545)
    mouse.position=turnoff_audio
    mouse.click(Button.left,1)
    mouse.position=turnoff_video
    mouse.click(Button.left,1)
    mouse.position=join_meet
    mouse.click(Button.left,1)
    time.sleep(3)
    active=False
    while(not active and mt_pass!=''):
        if "Enter meeting password"==GetWindowText(GetForegroundWindow()):
            active=True
        else:
            time.sleep(2)
            active=False
    if "Enter meeting password"==GetWindowText(GetForegroundWindow()):
        key_b.type(mt_pass)
        mouse.position=join_meet
        mouse.click(Button.left,1)
    now=datetime.now().strftime("%H:%M:%S")
    print(sub," class joined at ",now)
    end=False
    while not end:
        if "Leave meeting"==GetWindowText(GetForegroundWindow()):
            mouse.position=(940,475)
            mouse.click(Button.left,1)
            end=True
        else:
            time.sleep(2)
    time.sleep(2)
print("All classes have been ended")

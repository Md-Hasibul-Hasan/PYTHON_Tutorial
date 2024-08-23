
import time

x=float(input("enter on time in minute:"))
y=float(input("enter running time in minute:"))

i=0
j=0

motor_on=x*60
motor_running=y*60
motor_forward=True

stime=time.time()
while True:
    ctime=time.time()
    if ctime-stime <=motor_on:
        i+=1
        print(f"{i} motor off")
        time.sleep(1)
    elif ctime-stime>motor_on and ctime-stime <=(motor_on+motor_running):
        j+=1
        if motor_forward:
            print(f"{j} motor running forward")
        else:
            print(f"{j} motor running backward")
        time.sleep(1)
    else:
        stime=time.time()
        if motor_forward:
            motor_forward=False
        else:
            motor_forward=True
        i=0
        j=0
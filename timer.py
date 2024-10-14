import time

def countdown_timer(seconds):
    while seconds>0:
        mins=int(seconds/60)
        secs=int(seconds%60)
        timer=f'{mins}:{secs}'
        #1:15 if total secs are 75
        print(timer)
        time.sleep(1)
        seconds -=1 #or seconds=seconds
    print("time up!")

#input time in seconds
seconds=input("Enter the time in seconds :  ")

#function call
countdown_timer(int(seconds))
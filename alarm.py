from playsound import playsound
from datetime import datetime

current = datetime.now().time()
print(current)

only_curr = str(current).split(".")[0]
print(only_curr)

while(True):
    print(only_curr)
    if only_curr >= "10:25:00": 
        playsound("alarm_tone.wav")
#TEMPERATURE AND HUMIDITY MONITORING IN CHENNAI
import random
temp=random.randrange(24,50,5)
hum=random.randrange(10,100)
while(True):
    print("TEMPERATURE:",temp)
    if(temp>=40):
        print("HIGH TEMPERATURE DETECTED")
    print("HUMIDITY:",hum)

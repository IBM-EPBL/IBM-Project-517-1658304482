import random
import time
threshold1=int(input("Enter the threshold value for temperature:"))
threshold2=int(input("Enter the threshold value for humidity:"))

while(1):     
    temp=random.uniform(0,50)
    humidity=random.uniform(0,100)     
    print("temperature is : {0:.2f}".format(temp)) 
    print("humidity is : {0:.2f} %".format(humidity))
    time.sleep(1)
    if temp>=threshold1 and humidity>=threshold2: 
        print("\nHIGH ALERT\nHumidity alarm and Temperature alarm are ON \n")
        time.sleep(2) 
    elif(temp<threshold1 and humidity>=threshold2): 
        print("\nHumidity alarm is ON and Temperature alarm is OFF \n")
        time.sleep(2)
    elif (temp>=threshold1 and humidity<threshold2):
        print("\nHumidity alarm is OFF and Temperature alarm is ON \n")
        time.sleep(2)
    else:
        print("\nBoth alarms are OFF \n")
        time.sleep(2)

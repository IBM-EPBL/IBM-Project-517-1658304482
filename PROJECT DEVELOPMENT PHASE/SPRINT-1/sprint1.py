import random     
while(True):
        
        
        temp=random.uniform(92,110)
        Humid=random.uniform(60,100)
        ThreshHold = 60
        gassensor = random.uniform(0,100)
        print("Temperature : {:.2f}°C  Humidity : {:.2f}%".format(temp,Humid))
        print("Gas Concentration: {:.2f}".format(gassensor))
        if(gassensor>=ThreshHold):
            print("GAS LEAKAGE ALERT!!")
            print("BUZZER ON")
        else:
            print("ALL GOOD SAFE!")
            print("BUZZER OFF")
        print()
        
        
        
        

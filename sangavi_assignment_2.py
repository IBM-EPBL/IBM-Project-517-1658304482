import random
import time

while True:
    temp = random.randint(0,50)
    humidity = random.randint(0,100)
    print(f"Temperature = {temp} Humidity = {humidity}%")
    if temp > 40:
        print("!!! HIGH TEMPERATURE !!!")

    if humidity > 85:
        print("!!! HIGH HUMIDITY !!!")
    time.sleep(3)

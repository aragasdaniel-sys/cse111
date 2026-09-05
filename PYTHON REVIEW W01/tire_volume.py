import math
from datetime import datetime

current_time = datetime.now()
today = current_time.strftime("%Y-%m-%d") #Date
width = float(input("Enter the width of the tire in mm (ex 205): ")) #Width
aspect = float(input("Enter the aspect ratio of the tire (ex 60): ")) #Aspect
diameter = float(input("Enter the diameter of the wheel in inches (ex 15): ")) #Diameter
tire_volume = (math.pi * width ** 2 * aspect * (width * aspect + 2540 * diameter))/10000000000 #Tire_volume

print(f"The approximate volume is {tire_volume:.2f} liters")

with open("volumes.txt", "at") as volumes_txt:
    print(f"{today}, {width}, {aspect}, {diameter}, {tire_volume:.2f}", end = "\n", file = volumes_txt)
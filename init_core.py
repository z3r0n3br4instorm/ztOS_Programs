import os
print("Zerone Laboratories CENTRAL OPERATIONS REGISTER ENGINE [CORE] INITIALIZING...")
print("SYSTEM AUTHENTICATION REQUIRED !")
print("CHECKING USER...")
os.system("whoami")
print("DO NOT CLOSE THIS PROGRAM ! THIS CONTROLS HARDWARE SYSTEMS AND OTHER ztOS SYSTEMS...")
import time
from pyfirmata import Arduino, util
import pyfirmata
import psutil
def display_snapshot():
    print("Zerone Laboratories CENTRAL OPERATIONS REGISTER ENGINE [CORE] INITIALIZING...")
    print("SYSTEM AUTHENTICATION REQUIRED !")
    print("CHECKING USER...")
    os.system("whoami")
    print("DO NOT CLOSE THIS PROGRAM ! THIS CONTROLS HARDWARE SYSTEMS AND OTHER ztOS SYSTEMS...")
def hardware_control():
    switch = "off"
    print("EXTERNAL HARDWARE CONTROL SYSTEM ACTIVE !")
    board = Arduino('/dev/ttyUSB0')
    pin_number = 9
    board.digital[pin_number].mode = pyfirmata.OUTPUT
    temperature_info = psutil.sensors_temperatures()
    while True:
        os.system("clear")
        temperature_info = psutil.sensors_temperatures()
        if "coretemp" in temperature_info:
                cpu_temperatures = temperature_info["coretemp"]
                for entry in cpu_temperatures:
                        if "Package" in entry.label:
                                temp = int(entry.current)
                                if temp >=82 :
                                    board.digital[pin_number].write(0)
                                    switch = "on"
                                elif temp <= 75:
                                    board.digital[pin_number].write(1)
                                    switch = "off"
                                display_snapshot()
                                print("\ntemp :"+str(temp)+" switch_stat:"+switch)
                                time.sleep(0.5)
    #board.digital[pin_number].write(0)
    board.exit()



if __name__ == "__main__":
    hardware_control()


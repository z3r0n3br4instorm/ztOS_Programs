#!/usr/bin/python
from lib2to3.pgen2 import driver
import os
from datetime import datetime
from pyfirmata import Arduino, util, STRING_DATA
import time 
import psutil
from time import strftime,sleep, perf_counter
import GPUtil
import threading
import pyttsx3
import sys
# os.system("echo INITIALIZING > core_stat.txt")
# os.system("echo LOCKED > core_stat.txt&")
#time.sleep(5)
#os.system("cvlc ccbootdone.mp3&")
# time.sleep(4)
# os.system("cvlc lowpower.mp3&")
# time.sleep(5)
os.system("/home/zerone/anaconda3/bin/python /home/zerone/ztos_home_3.0.py&")
os.system("/home/zerone/anaconda3/bin/python /home/zerone/ztos_lockdown.py")
os.system("/home/zerone/anaconda3/bin/python /home/zerone/terminal_2.py&")
#os.system("/home/zerone/anaconda3/bin/python /home/zerone/systemstat.py&")
# try:
#     #os.system("/home/zerone/anaconda3/bin/python /home/zerone/laptopstat.py&")
#     os.system("ls /dev/tty*")
#     # print("[ANOMALLY]ARDUINO BOARD DETECTION FAIL !...")
#     # os.system("/usr/bin")
#     # print("Choose board manually !")
#     # y = input(str("Board USB Value :"))
#     string = '/dev/ttyUSB0'
#     global board
#     board = Arduino(string)
#     #print("Arduino board detected on /dev/ttyUSB !",y)
#     #os.system("/home/zerone/anaconda3/bin/python /home/zerone/anomally.py 'C.O.R.E FAILED TO DETECT ARDUINO BOARD !' 0")
#     os.system("echo 'C.O.R.E waiting for arduino boot seq' > console_log.txt")
#     os.system("cvlc hdctrl_online.mp3&")
#     time.sleep(1)
#     print("WAITING FOR ARDUINO BOARD BOOT SEQUANCE")
#     time.sleep(3)
#     os.system("cat ztos_core.py")
#     print("__ztOS CORE[Central Operations Register Engine] Subsystems controller v0.3__")
#     data = " "+"MARK1_UPSILON"
#     data2 = "  "+ "ztCC_ztOS"
#     # global x
#     # x = ""
#     board.send_sysex(STRING_DATA, util.str_to_two_byte_iter("sublight.off"))
#     board.send_sysex(STRING_DATA, util.str_to_two_byte_iter("fan.off"))
#     board.send_sysex(STRING_DATA, util.str_to_two_byte_iter("gpucool.off"))
#     board.send_sysex(STRING_DATA, util.str_to_two_byte_iter("ztOS C.O.R.E"))
#     board.send_sysex(STRING_DATA, util.str_to_two_byte_iter("CONNECTED !"))
#     # os.system("echo  > remote.txt")
#     # synth = pyttsx3.init(driverName='espeak')
#     # synth.setProperty('voice', synth.getProperty('voices')[11].id)
#     # synth.setProperty('rate',170)
#     # synth.say("debug shell initialized, ")
#     # synth.say("Zerone technlogies central computer successfully booted to zerone technologies operating system version 1.0, codename upsilon")
#     # synth.runAndWait()

#     # synth.say("Central Computer startup complete !")
#     # synth.runAndWait()

#     # synth.say("zee tee o s central operations register engine started !")
#     # synth.runAndWait()
# except:
#     print("MALFUNCTION: HARDWARE LINK")
#     os.system("/home/zerone/anaconda3/bin/python /home/zerone/laptopstat.py&")
#     os.system("ls /dev/tty*")
#     # print("[ANOMALLY]ARDUINO BOARD DETECTION FAIL !...")
#     # os.system("/usr/bin")
#     # print("Choose board manually !")
#     # y = input(str("Board USB Value :"))
#     string = '/dev/ttyUSB1'
#     #global board
#     board = Arduino(string)
#     #print("Arduino board detected on /dev/ttyUSB !",y)
#     #os.system("/home/zerone/anaconda3/bin/python /home/zerone/anomally.py 'C.O.R.E FAILED TO DETECT ARDUINO BOARD !' 0")
#     os.system("echo 'C.O.R.E waiting for arduino boot seq' > console_log.txt")
#     print("WAITING FOR ARDUINO BOARD BOOT SEQUANCE")
#     time.sleep(3)
#     os.system("cat ztos_core.py")
#     print("__ztOS CORE[Central Operations Register Engine] Subsystems controller v0.3__")
#     data = " "+"MARK1_UPSILON"
#     data2 = "  "+ "ztCC_ztOS"
#     # global x
#     # x = ""
#     board.send_sysex(STRING_DATA, util.str_to_two_byte_iter("sublight.off"))
#     board.send_sysex(STRING_DATA, util.str_to_two_byte_iter("fan.off"))
#     board.send_sysex(STRING_DATA, util.str_to_two_byte_iter("gpucool.off"))
#     board.send_sysex(STRING_DATA, util.str_to_two_byte_iter("ztOS C.O.R.E"))
#     board.send_sysex(STRING_DATA, util.str_to_two_byte_iter("CONNECTED !"))
    # os.system("echo  > remote.txt")
    # synth = pyttsx3.init(driverName='espeak')
    # synth.setProperty('voice', synth.getProperty('voices')[11].id)
    # synth.setProperty('rate',170)
    # synth.say("debug shell initialized, ")
    # synth.say("Zerone technlogies central computer successfully booted to zerone technologies operating system version 1.0, codename upsilon")
    # synth.runAndWait()

    # synth.say("Central Computer startup complete !")
    # synth.runAndWait()

    # synth.say("zee tee o s central operations register engine started !")
    # synth.runAndWait()
# try:
#     # synth.say("Calling RigelEngine Assistant !")
#     os.system("/home/zerone/anaconda3/bin/python /home/zerone/rigelAI.py&")
# except:
#     # synth.say("rigel assistant not responding !")
#     alert()
# time.sleep(1)
# synth.runAndWait()
m = 10
# while True:
#     try:
#         board = Arduino("/dev/ttyUSB",x)
#     except:
#           board = Arduino("/dev/ttyUSB",x)
y = 13
a = ""
anomally_loop_time = 0.5
# def alert():
#     os.system("/home/zerone/anaconda3/bin/python /home/zerone/anomally.py 'C.O.R.E SUBSYSTEM CRASHED !' 1&")
#     os.system("/home/zerone/anaconda3/bin/python /home/zerone/anomally.py 'C.O.R.E REBOOT REQUIRED !' 1&")
#     os.system("echo 'ANOMALLY <!>' >> console_log.txt")
#     os.system("echo 'C.O.R.E CRASHED <!>' >> console_log.txt")
#     os.system("echo 'C.O.R.E SUBSYSTEM FAULT DETECTED <!>' >> console_log.txt")
#     os.system("echo 'C.O.R.E REBOOT REQUIRED <!>' >> console_log.txt")
#     os.system("echo 'REBOOT REQUEST SENT <!>' >> console_log.txt")
#     os.system("/home/zerone/anaconda3/bin/python /home/zerone/synth.py 'Central Operations Register Engine Crashed, core reboot required'")
#     os.system("/home/zerone/anaconda3/bin/python /home/zerone/synth.py 'requesting automated central computer core subsystem reboot'")
#     os.system("echo core_reboot > remote.txt")
#     # while True:
#     #     #os.system("cat ztos_core.py")
#     #     board.send_sysex(STRING_DATA, util.str_to_two_byte_iter("sublight.on"))
#     #     time.sleep(anomally_loop_time)
#     #     board.send_sysex(STRING_DATA, util.str_to_two_byte_iter("sublight.off"))
#     #     time.sleep(anomally_loop_time)
#     #     os.system("echo core_reboot > remote.txt")
# # def remote_command():
# #     while True:
# #         with open('remote.txt') as f:
# #             lines = f.readlines()
# #             x = str(lines[0])
# #             print(x)
# #             time.sleep(3)
def send_sys_stat():
        print("memory")
        while True:
            try:
                ramuse = psutil.virtual_memory()[2]
                procuse = psutil.cpu_percent()
                send_proc_temp = "cp /sys/class/thermal/thermal_zone0/temp temp_cpu.zttf"
                send_ram = "echo "+str(ramuse)+" > ramstat.zttf"
                send_processor = "echo "+str(procuse)+" > processor.zttf"
                #send_proc_temp = "echo "+ +" > proc_temp.zttf"
                os.system(send_proc_temp)
                os.system(send_ram)
                os.system(send_processor)
                if ramuse > 65.00:
                    #os.system("echo 'HIGH RANDOM ACCESS USAGE DETECTED !' > remote.txt")
                    os.system('python synth.py "High random access memory usage detected !, system might crash"')
                    os.system("python anomally.py 'HIGH RAM USAGE !' 0")
            except:
                os.system("echo 'C.O.R.E ERROR' > remote.txt")
            time.sleep(0.5)
def comm_exec():
    global board
    os.system("echo ONLINE > core_stat.txt")
    while True:
        try:
            data = open("remote.txt","r")
            comm = data.read().strip("\n")
            print(comm)
            board.send_sysex(STRING_DATA, util.str_to_two_byte_iter(comm))
            if(comm == "core.lockdown" or comm == "system_lockdown"):
                os.system("/home/zerone/anaconda3/bin/python /home/zerone/ztos_lockdown.py&")
            elif(comm == "laptop_stat" or comm == "sys.stat"):
                os.system("/home/zerone/anaconda3/bin/python /home/zerone/laptopstat.py&")
            elif(comm == "shutdown" or comm == "sys.shutdown"):
                os.system("shutdown -h 1")
                os.system("sleep 10")
            send_comm = comm+" > output_log.txt&"
            # board.send_sysex(STRING_DATA, util.str_to_two_byte_iter("zt_HYPERSCAN :"))
            # board.send_sysex(STRING_DATA, util.str_to_two_byte_iter(comm))
            os.system(send_comm)
            os.system("echo > remote.txt")
        except:
            print("nocomm")
        #board.send_sysex(STRING_DATA, util.str_to_two_byte_iter(comm))
        time.sleep(1)
def timecheck():
    print("REACHED TIME LOOP")
    time.sleep(1)
    synth.say("Automated Light system, started !")
    synth.runAndWait()
    while True:
        if(time.localtime().tm_hour >= 17 or time.localtime().tm_hour < 7):
        #     if(time.localtime().tm_hour == 17):
        #         # synth.say("Automated Light system, online !")
        #         # synth.runAndWait()
                
            print("\nAUTOMATED TIME CHECK [RUNNING] - LIGHTS_ON")
            board.send_sysex(STRING_DATA, util.str_to_two_byte_iter("lightsys.on"))
        else:
            # if(time.localtime().tm_hour == 7):
            #     synth.say("Automated Light system, offline !")
            #     synth.runAndWait()
                
            board.send_sysex(STRING_DATA, util.str_to_two_byte_iter("lightsys.off"))
            print("\nAUTOMATED TIME CHECK [RUNNING] - LIGHTS_OFF")
        time.sleep(1)
# def gpucool():
#     print("REACHED GPU_STABILIZER LOOP")
#     synth.say("Automated Graphics processing unit stabilizer program, started !")
#     synth.say("Emergency mode active until gee pee yu temperature check initialize")
#     board.send_sysex(STRING_DATA, util.str_to_two_byte_iter("gpucool.on"))
#     synth.runAndWait()
#     tc = 0
#     while True:
#         time.sleep(m)
#         GPUtil.getAvailable()
#         # os.system("gpustat")
#         # if(time.localtime().tm_hour >= 17 or time.localtime().tm_hour < 7):
#         #     if(time.localtime().tm_hour == 17):
#         #         synth.say("Automated Light system, online !")
#         #         synth.runAndWait()
                
#         #     print("\nAUTOMATED TIME CHECK [RUNNING] - LIGHTS_ON")
#         #     board.send_sysex(STRING_DATA, util.str_to_two_byte_iter("lightsys.on"))
#         # else:
#         #     if(time.localtime().tm_hour == 7):
#         #         synth.say("Automated Light system, offline !")
#         #         synth.runAndWait()
                
#         #     board.send_sysex(STRING_DATA, util.str_to_two_byte_iter("lightsys.off"))
#         #     print("\nAUTOMATED TIME CHECK [RUNNING] - LIGHTS_OFF")
#         gpu = GPUtil.getGPUs()[0]
#         gputemp = int(gpu.temperature)
#         if(gputemp >= 70 and gputemp < 80):
#             if(gputemp == 71 or gputemp == 70 or gputemp == 72 or gputemp > 73):
#                 synth.say("Automated Graphics processing unit stabilizer program, online !")
#                 synth.runAndWait()
#                 #synth.endLoop()
#             print("\nAUTOMATED GPU TEMP CHECK [RUNNING] - STABILIZER_PROG_ONLINE")
#             board.send_sysex(STRING_DATA, util.str_to_two_byte_iter("gpucool.on"))
#             tc = 0
#         elif(gputemp < 55):
#             if(gputemp == 54 or gputemp == 55 or gputemp == 56):
#                 synth.say("Automated Graphics processing unit stabilizer program, offline !")
#                 synth.runAndWait()
#             print("\nAUTOMATED GPU_TEMP CHECK [RUNNING] - STABILIZER_PROG_OFFLINE")
#             board.send_sysex(STRING_DATA, util.str_to_two_byte_iter("gpucool.off"))
#             tc = 0
#         elif(a == "gpucool.off"):
#             os.system("sleep 1000000000000000000000000000000000")
#         elif(gputemp > 80):
#             thread4 = threading.Thread(target=alert)
#             thread4.start()
#             synth.say("Anomally, Automated Graphics processing unit stabilizer program detected critical temperatures in graphics processing unit , automated system shutdown will activate if temperature not decreased, alarm active !")
#             synth.runAndWait()
#             board.send_sysex(STRING_DATA, util.str_to_two_byte_iter("gpucool.on"))
#             os.system("python anomally.py 'HIGH GPU TEMP !' 0 &")
#             if(tc == 1):
#                 #os.system("killall -I vlc")
#                 synth.say("Automated Graphics processing unit stabilizer program will now engage automated system shutdown in tee minus ten seconds, ")
#                 os.system("python anomally.py 'CRITICAL GPU TEMP' 0 &")
#                 synth.runAndWait()
#                 os.system("sleep 10 && shutdown -h now")
#             tc +=1
#             time.sleep(25)
#             #os.system("takskill -I vlc")
#         os.system("echo  > remote.txt") 
# def display():
#     k = 0
#     print(board.get_firmata_version())
#     time_interval = float(0.15)
#     while True:
#         if a == "exit_prog":
#             board.send_sysex(STRING_DATA, util.str_to_two_byte_iter(data))
#             #print(data)
#             time.sleep(time_interval)
#             board.send_sysex(STRING_DATA, util.str_to_two_byte_iter(data2))
#             #print(data2)
#             exit(0)
#             #x = ""
#         elif len(a)<1:
#             loaddata = ("CPU_LOAD:"+str(psutil.cpu_percent()))
#             sendcpu = "echo "+str(psutil.cpu_percent())+" > remote_cpu.txt"
#             os.system(sendcpu)
#             try:
#                 GPUtil.getAvailable()
#                 # os.system("gpustat")
#                 gpu = GPUtil.getGPUs()[0]
#                 gputemp = ("GPU_TEMP:"+str(gpu.temperature))
#                 sendtemp = "echo "+str(gpu.temperature)+" > remote_temp.txt"
#                 os.system(sendtemp)
#             except:
#                 if(k < 1):
#                     print("\nFATAL ERROR! [HARDWARE] : Graphics Processing Unit not responding !")
#                     alert()
#             k += 1
#             board.send_sysex(STRING_DATA, util.str_to_two_byte_iter(loaddata))
#             # #print(data)
#             time.sleep(time_interval)
#             try:
#                 board.send_sysex(STRING_DATA, util.str_to_two_byte_iter(gputemp))
#             except:
#                 board.send_sysex(STRING_DATA, util.str_to_two_byte_iter("GPUERR!"))
#             #print(data2)
#             # board.send_sysex(STRING_DATA, util.str_to_two_byte_iter("GPU_DATA_ERR!"))
#         else:
#             board.send_sysex(STRING_DATA, util.str_to_two_byte_iter("zt_HYPERSCAN :"))
#             board.send_sysex(STRING_DATA, util.str_to_two_byte_iter(x))
#             time.sleep(time_interval)
#             # x = ""
# thread1 = threading.Thread(target=display)
#thread2 = threading.Thread(target=timecheck)
# # thread3 = threading.Thread(target=gpucool)
thread4 = threading.Thread(target=comm_exec)
thread1 = threading.Thread(target=send_sys_stat)
# # thread1.start()
# # time.sleep(1)
# # thread3.start()
# # time.sleep(1)
# thread2.start()
# # time.sleep(1)
thread4.start()
thread1.start()
# i = 0
# iranoutofnamesforthisvariable = 0
# sendlog = str("sed -i '"+str(i+1)+"s/^/[INIT]C.O.R.E READY !/\n' console_log.txt")
# os.system(sendlog)
# try:
#     while True:
#         # timecheck()
#         # x = input(str("\nEnter a value to transmit on to the microcontroller :"))
#         with open('remote.txt') as f:
#             #os.system("killall -I vlc")
#             try:
#                 lines = f.readlines()
#                 x = lines[0][:-1]
#                 a = lines[0][:-1]
#                 os.system("echo  > remote.txt")
#             except:
#                 alert()
#             if(len(x)>0):
#                 try:
#                     x = x.replace('_removspace_',' ')
#                     sendToLog = "echo "+x+" >> terminal_log.txt"
#                     sendToOutputLog = x+" >> output_log.txt&"
#                     sendToOutputLogOld = "echo output_log.txt >> output_old.txt"
#                     #os.system(sendToLog)
#                     os.system(sendToOutputLog)
#                     #os.system(sendToOutputLogOld)
#                     # board.send_sysex(STRING_DATA, util.str_to_two_byte_iter("sublight.on"))
#                     # board.send_sysex(STRING_DATA, util.str_to_two_byte_iter("sublight.off"))
#                 except:
#                     print("\n[INFO]NO SPACES IN REMOTE COMMAND")
#                     sendToLog = "echo "+x+" >> terminal_log.txt"
#                     sendToOutputLog = x+" >> output_log.txt&"
#                     #sendToOutputLogOld = "output_log.txt >> output_old.txt"
#                     os.system(sendlog)
#                     os.system(sendToOutputLog)
#                     #os.system(sendToOutputLogOld)
#             print("[INFO]ztOS CORE\n[Central Operations Register Engine] Subsystems controller v0.3\n[BACKEND_PROCESS|DO NOT SHUTDOWN THIS PROCESS]")
#             print("[RECIVED-COMMAND]COMMAND:",x)
#             os.system("cat remote.txt")
#             os.system("cat terminal_log.txt")
#             os.system("cat output_log.txt")
#             time.sleep(0.1)
#         if len(x)>1:
#             # iranoutofnamesforthisvariable += 1
#             # if iranoutofnamesforthisvariable > 16:
#             #     os.system("echo  > console_log.txt")
#             #     iranoutofnamesforthisvariable = 0
#             sendlog = str('echo "[RECIVED-COMMAND] '+str(x)+'" >> console_log.txt')
#             os.system(sendlog)
#         if x == "lthread.stop":
#             y = 100000
#             print("thread set to")
#             print(y)
#         elif x == "lthread.start":
#             y = 100
#             print("thread set to")
#             print(y)
#         elif x == "shutdown":
#             synth.say("Central Computer shutdown !")
#             synth.runAndWait()
#             os.system("shutdown -h now")
#         elif x == "reboot":
#             synth.say("Engaging central computer system reboot !")
#             synth.runAndWait()
#             os.system('reboot')
#         elif x == "mute":
#             synth.setProperty("volume", 0)
#         elif x == "unmute":
#             synth.setProperty("volume", 1)
#         elif x == "gputhread.on":
#             m = 10
#         elif x == "alert.stop":
#             anomally_loop_time = 10000
#         elif x == "core.shutdown":
#             synth.say("warning, Central Computer core subsystem offline !")
#             os.system("python anomally.py 'CORE SHUTDOWN !'")
#             os.system("echo '<!>C.O.R.E DISCONNECTED!' > console_log.txt")
#             time.sleep(2)
#             sys.exit()
#         time.sleep(1)
#         # else:
#         #     os.system(x)
#         #     x = ""

#         # elif x == "sys.reboot":
#         #     print("RUNNING SYSTEM REBOOT SEQUANCE !")
#         #     x = "sys.shutdown"
#         #     os.system("reboot")
#     # x = sys.argv[1]
#     # display()
#     # exit(0)
# except:
#     os.system("echo 'C.O.R.E COMMAND RECIVER CRASHED !' >> console_log.txt")
#     os.system("echo 'C.O.R.E MANUAL REBOOT REQUIRED !' >> console_log.txt")
#     alert()

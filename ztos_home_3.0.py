#Zerone Technologies And Laboratories Systems
#Zerone Technologies Home Interface (1366x768)
from PyQt5 import QtCore, QtGui, QtWidgets
import os
import sys
import time
import GPUtil
import psutil
import time
from random import seed
from random import randint
from PyQt5.QtGui import QMovie
os.system("echo > remote2.txt")
try:
    gpu = GPUtil.getGPUs()[0]
    gputemp = int(gpu.temperature)
except:
    os.system("cvlc gpufail.mp3&")
# from PyQt5.QtMultimediaWidgets import QVideoWidget
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1383, 894)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(-4, 0, 1371, 801))
        self.label.setText("")
        self.label.setTextFormat(QtCore.Qt.RichText)
        self.label.setPixmap(QtGui.QPixmap("ztos-default.jpg"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(10, 650, 1191, 17))
        self.label_2.setObjectName("label_2")
        self.progressBar = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar.setGeometry(QtCore.QRect(1313, 4, 51, 31))
        self.progressBar.setProperty("value", 24)
        self.progressBar.setObjectName("progressBar")
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(980, 670, 381, 61))
        self.textBrowser.setObjectName("textBrowser")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(990, 510, 111, 17))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(1140, 510, 191, 17))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(990, 530, 121, 20))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(1140, 530, 191, 21))
        self.label_6.setObjectName("label_6")
        self.long_sheet = QtWidgets.QLabel(self.centralwidget)
        self.long_sheet.setGeometry(QtCore.QRect(10, -8, 581, 350))
        self.long_sheet.setText("")
        self.long_sheet.setObjectName("long_sheet")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(1000, 10, 261, 31))
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(990, 556, 111, 21))
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(1140, 556, 151, 21))
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(990, 580, 121, 17))
        self.label_10.setObjectName("label_10")
        self.label_11 = QtWidgets.QLabel(self.centralwidget)
        self.label_11.setGeometry(QtCore.QRect(1140, 580, 121, 17))
        self.label_11.setObjectName("label_11")
        self.label_12 = QtWidgets.QLabel(self.centralwidget)
        self.label_12.setGeometry(QtCore.QRect(990, 600, 121, 17))
        self.label_12.setObjectName("label_12")
        self.label_13 = QtWidgets.QLabel(self.centralwidget)
        self.label_13.setGeometry(QtCore.QRect(1140, 596, 191, 31))
        self.label_13.setObjectName("label_13")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(360, 670, 81, 21))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(460, 670, 131, 21))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(610, 670, 121, 21))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(760, 670, 151, 21))
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_5.setGeometry(QtCore.QRect(360, 700, 151, 33))
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_6 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_6.setGeometry(QtCore.QRect(520, 700, 251, 33))
        self.pushButton_6.setObjectName("pushButton_6")
        self.pushButton_7 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_7.setGeometry(QtCore.QRect(780, 700, 131, 33))
        self.pushButton_7.setObjectName("pushButton_7")
        self.textBrowser_2 = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser_2.setGeometry(QtCore.QRect(10, 410, 581, 241))
        self.textBrowser_2.setObjectName("textBrowser_2")
        self.OHIND = QtWidgets.QLabel(self.centralwidget)
        self.OHIND.setGeometry(QtCore.QRect(1280, 490, 81, 71))
        self.OHIND.setText("")
        self.OHIND.setObjectName("OHIND")
        self.WARN = QtWidgets.QLabel(self.centralwidget)
        self.WARN.setGeometry(QtCore.QRect(930, 6, 51, 41))
        self.WARN.setText("")
        self.WARN.setTextFormat(QtCore.Qt.RichText)
        self.WARN.setPixmap(QtGui.QPixmap("alert.gif"))
        self.WARN.setScaledContents(True)
        self.WARN.setObjectName("WARN")
        self.TEMP = QtWidgets.QLabel(self.centralwidget)
        self.TEMP.setGeometry(QtCore.QRect(860, 6, 61, 41))
        self.TEMP.setText("")
        self.TEMP.setTextFormat(QtCore.Qt.RichText)
        self.TEMP.setPixmap(QtGui.QPixmap("thermal.jpg"))
        self.TEMP.setScaledContents(True)
        self.TEMP.setObjectName("TEMP")
        self.label_16 = QtWidgets.QLabel(self.centralwidget)
        self.label_16.setGeometry(QtCore.QRect(990, 480, 391, 20))
        self.label_16.setObjectName("label_16")
        self.movie = QMovie("backgroud_pattern.gif")
        self.label_17 = QtWidgets.QLabel(self.centralwidget)
        self.label_17.setGeometry(QtCore.QRect(0, 60, 1371, 731))
        self.label_17.setTextFormat(QtCore.Qt.RichText)
        #self.label_17.setPixmap(QtGui.QPixmap("ztLOGO.png"))
        self.label_17.setScaledContents(True)
        self.label_17.setObjectName("label_17")
        self.label_17.setMovie(self.movie)
        self.movie.start()
        self.logo = QtWidgets.QLabel(self.centralwidget)
        self.logo.setGeometry(QtCore.QRect(1180, -1, 191, 121))
        self.logo.setText("")
        self.logo.setTextFormat(QtCore.Qt.RichText)
        self.logo.setPixmap(QtGui.QPixmap("lubuntu_logo.png"))
        self.logo.setScaledContents(True)
        self.logo.setObjectName("logo")
        self.label.raise_()
        self.label_17.raise_()
        self.label_2.raise_()
        self.progressBar.raise_()
        self.textBrowser.raise_()
        self.label_3.raise_()
        self.label_4.raise_()
        self.label_5.raise_()
        self.label_6.raise_()
        self.long_sheet.raise_()
        self.label_7.raise_()
        self.label_8.raise_()
        self.label_9.raise_()
        self.label_10.raise_()
        self.label_11.raise_()
        self.label_12.raise_()
        self.label_13.raise_()
        self.pushButton.raise_()
        self.pushButton_2.raise_()
        self.pushButton_3.raise_()
        self.pushButton_4.raise_()
        self.pushButton_5.raise_()
        self.pushButton_6.raise_()
        self.pushButton_7.raise_()
        self.textBrowser_2.raise_()
        self.logo.raise_()
        self.progressBar.raise_()
        self.OHIND.raise_()
        self.WARN.raise_()
        self.TEMP.raise_()
        self.label_16.raise_()
        self.buffer = QtWidgets.QLabel(self.centralwidget)
        self.buffer.setGeometry(QtCore.QRect(800, 2, 51, 51))
        self.buffer.setText("")
        self.buffer.setTextFormat(QtCore.Qt.RichText)
        self.buffer.setPixmap(QtGui.QPixmap("activity_indicator.gif"))
        self.buffer.setScaledContents(True)
        self.buffer.setObjectName("buffer")
        self.movie2 = QMovie("activity_indicator.gif")
        self.buffer.setMovie(self.movie2)
        self.proc_warn = QtWidgets.QLabel(self.centralwidget)
        self.proc_warn.setGeometry(QtCore.QRect(590, 30, 201, 17))
        self.proc_warn.setObjectName("proc_warn")
        self.temp_warn2 = QtWidgets.QLabel(self.centralwidget)
        self.temp_warn2.setGeometry(QtCore.QRect(590, 10, 211, 17))
        self.temp_warn2.setObjectName("temp_warn2")
        self.movie2.start()
        #self.movie2.hide()
        self.progressBar.hide()
        self.temp_warn2.hide()
        self.proc_warn.hide()
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        #IN AN UPDATE, COPY CODE FROM HERE
        self.textBrowser_2.hide()
        self.label_2.setText("ZERONE:TECH LABORATORY | ztOS 1.4 | Zerone Brianstorm")
        self.label_14 = QtWidgets.QLabel(self.centralwidget)
        self.label_14.setGeometry(QtCore.QRect(1790, 670, 81, 81))
        self.label_14.setText("")
        self.label_14.setTextFormat(QtCore.Qt.RichText)
        self.label_14.setPixmap(QtGui.QPixmap("THERMAL2.png"))
        self.label_14.setScaledContents(True)
        self.label_14.setObjectName("label_14")
        # self.label
        #self.movie.stop()
        #self.label_17.hide()
        #self.movie.stop()
        self._update_timer = QtCore.QTimer()
        self._update_timer.timeout.connect(self.animate_in)
        self._update_timer.timeout.connect(self.get_user_id)
        self._update_timer.timeout.connect(self.get_system_stats)
        self._update_timer.timeout.connect(self.stat_check)
        self._update_timer.start(0)
        def start_dolphin(self):
            os.system("dolphin &")
        def remote_hardware_ctrl(self):
            os.system("/home/zerone/anaconda3/bin/python /home/zerone/ztcc_client.py&")
        def start_rigel(self):
            os.system("python rigelAI.py&")
        def core_reboot(self):
            os.system("echo core.reboot >> remote.txt")
        def shutdown(self):
            os.system("shutdown -h now")
        def sys_reboot(self):
            os.system("reboot")
        def terminal(self):
            os.system("/home/zerone/anaconda3/bin/python /home/zerone/terminal_2.py&")
        self.pushButton.clicked.connect(start_dolphin)
        self.pushButton_2.clicked.connect(remote_hardware_ctrl)
        self.pushButton_3.clicked.connect(start_rigel)
        self.pushButton_4.clicked.connect(core_reboot)
        self.pushButton_5.clicked.connect(sys_reboot)
        self.pushButton_6.clicked.connect(shutdown)
        self.pushButton_7.clicked.connect(terminal)
        # def start_dolphin(self):
        #     os.system("dolphin &")
        # def remote_hardware_ctrl(self):
        #     os.system("python ztcc_client.py&")
        # def start_rigel(self):
        #     os.system("python rigelAI.py&")
        # def core_reboot(self):
        #     os.system("echo core.reboot >> remote.txt")
        # def shutdiown(self):
        #     os.system("shutdown -h now")
        # def terminal(self):
        #     os.system("python terminal.py&")
        ##########################################################
        self.label_16.hide()
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
    #IN AN UPDATE, COPY CODE FROM HERE
    global c,u,m,stat,n,i,g,e,r,stat2
    c,u,m,n = 1250,710,740,-10
    stat = "on"
    stat2 = "idk"
    def stat_check(self):
        global stat,stat2
        try:
            stat = open("remote.txt","r").read().strip().replace("\n","").replace(" ","")
            stat2 = open("remote2.txt","r").read().strip().replace("\n","").replace(" ","")
        except:
            print("err")
    def animate_in(self):
        unlock_stat = open("unlock.txt","r")
        global c,u,m
        global n
        global stat,stat2
        #
        usage = psutil.cpu_percent()
        if stat == "shutdown" or unlock_stat.read().strip() == "lock" or stat2 == "standby":
            self.progressBar.hide()
            self.label_2.setText("| STARGATE | ztOS | ztLABS | System is in standby mode...")
            if c >= 1205:
                self.logo.setGeometry(QtCore.QRect(1205, -60, 191, 121))
                c = 1205
            else:
                self.logo.setGeometry(QtCore.QRect(c, -60, 191, 121))
                #self.textBrowser.setText(str(I))
                c += 1
            if u == 710:
                self.pushButton.setGeometry(QtCore.QRect(360, 710, 81, 21))
                self.pushButton_2.setGeometry(QtCore.QRect(460, 710, 131, 21))
                self.pushButton_3.setGeometry(QtCore.QRect(610, 710, 121, 21))
                self.pushButton_4.setGeometry(QtCore.QRect(760, 710, 151, 21))
            else:
                self.pushButton.setGeometry(QtCore.QRect(360, u, 81, 21))
                self.pushButton_2.setGeometry(QtCore.QRect(460, u, 131, 21))
                self.pushButton_3.setGeometry(QtCore.QRect(610, u, 121, 21))
                self.pushButton_4.setGeometry(QtCore.QRect(760, u, 151, 21))
                u += 1
            if m == 740:
                self.pushButton_5.setGeometry(QtCore.QRect(360, 740, 151, 33))
                self.pushButton_6.setGeometry(QtCore.QRect(520, 740, 251, 33))
                self.pushButton_7.setGeometry(QtCore.QRect(780, 740, 131, 33))
            else :
                self.pushButton_5.setGeometry(QtCore.QRect(360, m, 151, 33))
                self.pushButton_6.setGeometry(QtCore.QRect(520, m, 251, 33))
                self.pushButton_7.setGeometry(QtCore.QRect(780, m, 131, 33))
                m += 1
            if n <= -8:
                self.long_sheet.setGeometry(QtCore.QRect(-8, 70, 581, 350))
            else:
                self.long_sheet.setGeometry(QtCore.QRect(n, 70, 581, 350))
                n-=2
        else:
            self.label_2.setText("| STARGATE | ztOS | ztLABS |")
            if c <= 1180:
                #self.logo.setGeometry(QtCore.QRect(1790, -60, 81, 81))
                c = 1180
                self.progressBar.show()
            else:
                self.logo.setGeometry(QtCore.QRect(c, -60, 191, 121))
                #self.textBrowser.setText(str(I))
                c -= 2
            if u == 670:
                self.pushButton.setGeometry(QtCore.QRect(360, 670, 81, 21))
                self.pushButton_2.setGeometry(QtCore.QRect(460, 670, 131, 21))
                self.pushButton_3.setGeometry(QtCore.QRect(610, 670, 121, 21))
                self.pushButton_4.setGeometry(QtCore.QRect(760, 670, 151, 21))
            else:
                self.pushButton.setGeometry(QtCore.QRect(360, u, 81, 21))
                self.pushButton_2.setGeometry(QtCore.QRect(460, u, 131, 21))
                self.pushButton_3.setGeometry(QtCore.QRect(610, u, 121, 21))
                self.pushButton_4.setGeometry(QtCore.QRect(760, u, 151, 21))
                u -= 1
            if m == 700:
                self.pushButton_5.setGeometry(QtCore.QRect(360, 700, 151, 33))
                self.pushButton_6.setGeometry(QtCore.QRect(520, 700, 251, 33))
                self.pushButton_7.setGeometry(QtCore.QRect(780, 700, 131, 33))
            else :
                self.pushButton_5.setGeometry(QtCore.QRect(360, m, 151, 33))
                self.pushButton_6.setGeometry(QtCore.QRect(520, m, 251, 33))
                self.pushButton_7.setGeometry(QtCore.QRect(780, m, 131, 33))
                m -= 1
            if n >= 10:
                self.long_sheet.setGeometry(QtCore.QRect(10, 70, 581, 350))
            else:
                self.long_sheet.setGeometry(QtCore.QRect(n, 70, 581, 350))
                n += 1
    def get_user_id(self):
        print("debug")
        try:
            f = open("user.txt","x")
            f.close()
        except:
            f = open("user.txt")
            f.close()
        os.system("whoami > user.txt")
        with open('user.txt') as f:
            username = f.read().strip()
            if (username == "zerone"):
                print("Mr.Brianstorm")
                self.label_4.setText("Zerone Brianstorm")
            else:
                print(username)
                self.label_4.setText(username)
    def get_system_stats(self):
        rand = randint(0,296)
        #data = open("ztos_home_2.0.py","r")
        # try:
        #     setData = data.readlines()[rand]
        #     self.long_sheet.setText("EXEC_LINE_READ [DEV_BETA]\n"+setData+"\n THIS SYSTEM IS NOT STILL FUNCTION PROPERLY")
        # except:
        #     print("system_fail")
        print("Overall System Load:LOADING")
        ####CALCULATIONS
        try:
            gpu = GPUtil.getGPUs()[0]
            gputemp = int(gpu.temperature)
        except:
            os.system("echo gpu_data_error! >> sys_output.txt")
            gputemp = 0
        ramuse = psutil.virtual_memory()[2]
        try:
            usage = psutil.cpu_percent()
        except:
            usage = 0
        try:
            processor_temp = float((open("temp_cpu.zttf").readlines()[2]).split()[2].replace("+","").replace("°C",""))
        except:
            processor_temp=0
        if (int(float(processor_temp))/1000 >= 80):
            self.TEMP.show()
            self.temp_warn2.setText("Critical Temperatures Detected")
            self.WARN.show()
            self.temp_warn2.show()
            #os.system("/home/zerone/anaconda3/bin/python /home/zerone/temps_warn.py")
        else:
            self.TEMP.hide()
            self.WARN.hide()
            self.temp_warn2.hide()
        avg_usage = (usage+ramuse)/2
        if(int(avg_usage) > 70):
                    self.buffer.show()
                    self.proc_warn.setText("Heavy Processing Detected !")
                    self.proc_warn.show()
                    self.label_6.setText("OVERLOAD <!>")
                    #os.system("python alert.py 'SYSTEM OVERLOAD DETECTED!' 0")
                    self.progressBar.setStyleSheet("""
                                                QProgressBar {
                                                    border-style: solid;
                                                    border-color: grey;
                                                    border-radius:5px;
                                                    border-width: 2px;
                                                    text-align: center;
                                                    text-color: black;
                                                }
                                                  QProgressBar::chunk
                                                  {
                                                  background-color: #FF3131;
                                                  }""")
        elif(int(avg_usage) >= 50):
                    self.buffer.show()
                    self.proc_warn.setText("Processing Detected !")
                    self.proc_warn.show()
                    self.label_6.setText("UNSTABLE <!>")
                    self.progressBar.setStyleSheet("""
                                                QProgressBar {
                                                    border-style: solid;
                                                    border-color: grey;
                                                    border-radius:5px;
                                                    border-width: 2px;
                                                    text-align: center;
                                                    text-color: black;
                                                }
                                                  QProgressBar::chunk
                                                  {
                                                  background-color: #FF6700;
                                                  }""")
        else:
                    self.proc_warn.hide()
                    self.buffer.hide()
                    self.label_6.setText("STABLE")
                    self.progressBar.setStyleSheet("""
                                                QProgressBar {
                                                    border-style: solid;
                                                    border-color: grey;
                                                    border-radius:5px;
                                                    border-width: 2px;
                                                    text-align: center;
                                                    text-color: black;
                                                }
                                                  QProgressBar::chunk
                                                  {
                                                  background-color: #2f524e;
                                                  }""")
        self.progressBar.setValue(avg_usage) 
        rigel_stat = open("rigel_check.txt")
        rigel_status = rigel_stat.readlines()[0].strip()
        err_check =5
        if(int(rigel_status) < 1):
            self.label_9.setText("OFFLINE")
        else:
            if(int(rigel_status) >= err_check):
                self.label_9.setText("RIGEL_NOT_RESPONING!")
            else:
                self.label_9.setText("ONLINE")
                #os.system("alert 'SUBSYSTEM ERROR DETECTED - RIGEL' 0") 
        core = open("core_stat.txt")
        core_stat = core.read().strip()
        self.label_11.setText(core_stat)
        #########CORE_LOG####################
        try:
            data1 = open("remote.txt")
            #log = open("core_log.txt")
            #output = open("output_log.txt")
            remote_data = data1.readlines()[0].strip()
            #core_log = log.readlines()[0].strip()
            #output_log = output.read()
            self.textBrowser.append("[C.O.R.E MONITOR]")
            self.textBrowser.append(remote_data)
            #self.textBrowser.append(core_log)
            #self.textBrowser.append(output_log)
            meminfo = open("/proc/meminfo","r")
            meminfo_read = meminfo.read()
            self.long_sheet.setText(meminfo_read)
        except:
            self.textBrowser.setText("System Error !")
        ####################################
        current_time = time.localtime(time.time())
        time_set = time.asctime(current_time)
        self.label_7.setText(time_set)


        #####################################
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_2.setText(_translate("MainWindow", "LOADING DATA..."))
        self.textBrowser.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Sony Sketch EF\'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Connecting to C.O.R.E...</p></body></html>"))
        self.label_3.setText(_translate("MainWindow", "USER             :"))
        self.label_4.setText(_translate("MainWindow", "LOADING DATA..."))
        self.label_5.setText(_translate("MainWindow", "System status :"))
        self.label_6.setText(_translate("MainWindow", "STABLE"))
        self.label_7.setText(_translate("MainWindow", "TIME LOADING"))
        self.label_8.setText(_translate("MainWindow", "RIGEL Status   :"))
        self.label_9.setText(_translate("MainWindow", "LOADING DATA..."))
        self.label_10.setText(_translate("MainWindow", "C.O.R.E Status  :"))
        self.label_11.setText(_translate("MainWindow", "LOADING DATA..."))
        self.label_12.setText(_translate("MainWindow", "OS Type          :"))
        self.label_13.setText(_translate("MainWindow", "ztOS for ztCC and ztLAPTOP"))
        self.pushButton.setText(_translate("MainWindow", "HOME"))
        self.label_2.setText("ztos_home_3.0_dev")
        self.pushButton_2.setText(_translate("MainWindow", "C.O.R.E LINK"))
        self.pushButton_3.setText(_translate("MainWindow", "R.I.G.E.L"))
        self.pushButton_4.setText(_translate("MainWindow", "REBOOT C.O.R.E"))
        self.pushButton_5.setText(_translate("MainWindow", "REBOOT SYSTEM"))
        self.pushButton_6.setText(_translate("MainWindow", "SYSTEM SHUTDOWN"))
        self.pushButton_7.setText(_translate("MainWindow", "TERMINAL"))
        self.textBrowser_2.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Sony Sketch EF\'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">ONGOING PROJECTS-</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Zerone Technologies Operating System [ztOS]</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">CENTRAL OPERATIONS REGISTER ENGINE [C.O.R.E]</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">RATIONAL INTELLIGENT GENIUS EXCEPTIONAL LOGICAL ENGINE[R.I.G.E.L ENGINE]</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">TOOD PROJECTS-</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Zerone Technologies Computer Automated Rover [ztCAR]</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Zerone Technologies OS HOME / Auto / Mobile [ztOS_Home / ztOS_AUTO / ztOS_MOBILE]</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Project TIMEFALL</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Project COSMOS</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.label_16.setText(_translate("MainWindow", "ZERONE TECH OS"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

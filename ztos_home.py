# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ztOS_HOME_APLOW_RES.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets

from PyQt5 import QtCore, QtGui, QtWidgets
import os
import sys
import time
import GPUtil
import psutil
import time
from random import seed
from random import randint
from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1262, 745)
        # self.setStyleSheet("""
        # QProgressBar {
        #     border-style: solid;
        # }
        # """)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 0, 1241, 721))
        self.label.setText("")
        self.label.setTextFormat(QtCore.Qt.RichText)
        self.label.setPixmap(QtGui.QPixmap("ztos-default.jpg"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(10, 10, 1191, 17))
        self.label_2.setObjectName("label_2")
        self.progressBar = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar.setGeometry(QtCore.QRect(1185, 545, 51, 41))
        self.progressBar.setProperty("value", 24)
        self.progressBar.setObjectName("progressBar")
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(850, 600, 391, 61))
        self.textBrowser.setObjectName("textBrowser")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(900, 414, 111, 17))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(1050, 414, 241, 17))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(900, 434, 121, 20))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(1050, 434, 191, 21))
        self.label_6.setObjectName("label_6")
        self.long_sheet = QtWidgets.QLabel(self.centralwidget)
        self.long_sheet.setGeometry(QtCore.QRect(10, 30, 931, 261))
        self.long_sheet.setText("")
        self.long_sheet.setObjectName("long_sheet")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(10, 630, 241, 31))
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(900, 460, 111, 21))
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(1050, 460, 151, 21))
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(900, 484, 121, 17))
        self.label_10.setObjectName("label_10")
        self.label_11 = QtWidgets.QLabel(self.centralwidget)
        self.label_11.setGeometry(QtCore.QRect(1050, 484, 121, 17))
        self.label_11.setObjectName("label_11")
        self.label_12 = QtWidgets.QLabel(self.centralwidget)
        self.label_12.setGeometry(QtCore.QRect(900, 504, 121, 17))
        self.label_12.setObjectName("label_12")
        self.label_13 = QtWidgets.QLabel(self.centralwidget)
        self.label_13.setGeometry(QtCore.QRect(1050, 500, 241, 31))
        self.label_13.setObjectName("label_13")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(280, 600, 81, 21))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(380, 600, 131, 21))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(530, 600, 121, 21))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(680, 600, 151, 21))
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_5.setGeometry(QtCore.QRect(280, 630, 151, 33))
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_6 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_6.setGeometry(QtCore.QRect(440, 630, 251, 33))
        self.pushButton_6.setObjectName("pushButton_6")
        self.pushButton_7 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_7.setGeometry(QtCore.QRect(700, 630, 131, 33))
        self.pushButton_7.setObjectName("pushButton_7")
        self.textBrowser_2 = QtWidgets.QLabel(self.centralwidget)
        self.textBrowser_2.setGeometry(QtCore.QRect(10, 350, 581, 241))
        self.textBrowser_2.setObjectName("textBrowser_2")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        #IN AN UPDATE, COPY CODE FROM HERE
        self._update_timer = QtCore.QTimer()
        # self._update_timer.timeout.connect(self.get_user_id)
        self._update_timer.timeout.connect(self.get_system_stats)
        #self._update_timer.timeout.connect(self.get_memory_stat)
        self.label_2.setText("Zerone Technologies And Laboratories [ztLABS-ztOS_UPSILON]")
        self._update_timer.start(0)
        def start_dolphin(self):
            os.system("dolphin &")
        def remote_hardware_ctrl(self):
            os.system("python ztcc_client.py&")
            os.system("python ztos_core_ctrl2.py&")
        def start_rigel(self):
            os.system("python rigel.py&")
        def core_reboot(self):
            os.system("echo core.reboot >> remote.txt")
        def shutdown(self):
            os.system("shutdown -h now")
        def sys_reboot(self):
            os.system("reboot")
        def terminal(self):
            os.system("python terminal.py&")
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
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        #IN AN UPDATE, COPY CODE FROM HERE
        print("debug")
        try:
            f = open("user.txt","x")
        except:
            f = open("user.txt","w")
            f.close()
            f.close()
        os.system("whoami > user.txt")
        with open('user.txt') as f:
            username = f.read().strip()
            if (username == "zerone"):
                print("Mr.Brianstorm")
                self.label_4.setText("Mr.Brianstorm")
            else:
                print(username)
                self.label_4.setText(username)
    def get_system_stats(self):
        rand = randint(0,296)
        data = open("os_home_app.py","r")
        try:
            setData = data.readlines()[rand]
            self.long_sheet.setText("EXEC_LINE_READ [DEV_BETA]\n"+setData+"\n THIS SYSTEM IS NOT STILL FUNCTION PROPERLY")
        except:
            print("system_fail")
        print("Overall System Load:LOADING")
        ####CALCULATIONS
        try:
            gpu = GPUtil.getGPUs()[0]
            gputemp = int(gpu.temperature)
        except:
            os.system("echo gpu_data_error! >> remote.txt")
            gputemp = 0
        try:
            ramuse = psutil.virtual_memory()[2]
            # self.progressBar_2.setValue(int(ramuse))
        except:
            ramuse = 0
        try:
            usage = psutil.cpu_percent()
        except:
            usage = 0
        avg_usage = (usage+ramuse)/2
        if(int(avg_usage) > 70):
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
        rigel_stat = open("rigel_check.txt","r")
        rigel_status = rigel_stat.read().strip()
        self.label_9.setText(rigel_status)
                #os.system("alert 'SUBSYSTEM ERROR DETECTED - RIGEL' 0") 
        core = open("core_stat.txt")
        core_stat = core.read().strip()
        self.label_11.setText(core_stat)
        #########CORE_LOG####################
        data1 = open("remote.txt")
        log = open("core_log.txt","r")
        try:
            remote_data = data1.readlines()[0].strip()
            self.textBrowser.append("[RECIVED_TO_CORE]"+remote_data)
        except:
            self.textBrowser.append("NULL_COMMAND")
        core_log = log.readlines()[0].strip()
        self.textBrowser.append(core_log)
        meminfo = open("/proc/meminfo","r")
        meminfo_read = meminfo.read()
        self.textBrowser_2.setText(meminfo_read)
        # self.textBrowser_2.clear()
        ####################################
        current_time = time.localtime(time.time())
        time_set = time.asctime(current_time)
        self.label_7.setText(time_set)


        #####################################
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_2.setText(_translate("MainWindow", "Zerone Technologies And Laboratories | ztLABS"))
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
        self.pushButton_2.setText(_translate("MainWindow", "Hardware Control"))
        self.pushButton_3.setText(_translate("MainWindow", "R.I.G.E.L"))
        self.pushButton_4.setText(_translate("MainWindow", "REBOOT C.O.R.E"))
        self.pushButton_5.setText(_translate("MainWindow", "REBOOT SYSTEM"))
        self.pushButton_6.setText(_translate("MainWindow", "SYSTEM SHUTDOWN"))
        self.pushButton_7.setText(_translate("MainWindow", "TERMINAL"))
#         self.textBrowser_2.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
# "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
# "p, li { white-space: pre-wrap; }\n"
# "</style></head><body style=\" font-family:\'Sony Sketch EF\'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
# "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">ONGOING PROJECTS-</p>\n"
# "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Zerone Technologies Operating System [ztOS]</p>\n"
# "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">CENTRAL OPERATIONS REGISTER ENGINE [C.O.R.E]</p>\n"
# "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">RATIONAL INTELLIGENT GENIUS EXCEPTIONAL LOGICAL ENGINE[R.I.G.E.L ENGINE]</p>\n"
# "<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
# "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">TOOD PROJECTS-</p>\n"
# "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Zerone Technologies Computer Automated Rover [ztCAR]</p>\n"
# "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Zerone Technologies OS HOME / Auto / Mobile [ztOS_Home / ztOS_AUTO / ztOS_MOBILE]</p>\n"
# "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Project TIMEFALL</p>\n"
# "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Project COSMOS</p>\n"
# "<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

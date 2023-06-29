from PyQt5 import QtCore, QtGui, QtWidgets
import psutil
import subprocess
import threading
import GPUtil
from PyQt5.QtGui import QPainter
from PyQt5.QtCore import QTimer, QMetaObject, Qt
from PyQt5.QtGui import QPainter
from PyQt5.QtWidgets import QApplication, QMainWindow, QProgressBar
import os
global c,u,m,gpu_utilization,cpu_utilization
c = 120
u = 0
gpu_util = 0
gpu_utilization = 0
cpu_utilization = 0
global gpu, temperature
def check_gpu():
        global gpu, temperature
        try:
            gpu = GPUtil.getGPUs()[0]
            temperature = gpu.temperature
        except:
            print("ERR_GPU")
check_gpu()
class Ui_MainWindow(object):
    global u
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1920, 1155)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.progressBar = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar.setGeometry(QtCore.QRect(0, 1020, 341, 71))
        self.progressBar.setProperty("value", 24)
        self.progressBar.setObjectName("progressBar")
        self.progressBar_2 = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar_2.setGeometry(QtCore.QRect(1580, 1020, 341, 71))
        self.progressBar_2.setProperty("value", 24)
        self.progressBar_2.setObjectName("progressBar_2")
        self.progressBar_2.setInvertedAppearance(True)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(1700, -30, 201, 181))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(10, 950, 341, 61))
        self.label_2.setObjectName("label_2")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(1570, 950, 341, 61))
        self.label_4.setObjectName("label_4")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(20, 560, 601, 191))
        self.label_3.setObjectName("label_3")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(20, 750, 61, 31))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(90, 750, 121, 31))
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(90, 780, 121, 31))
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(20, 780, 61, 31))
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(30, 40, 391, 531))
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(20, 10, 391, 21))
        self.label_10.setObjectName("label_10")
        self.label_11 = QtWidgets.QLabel(self.centralwidget)
        self.label_11.setGeometry(QtCore.QRect(0, 0, 1911, 1051))
        self.label_11.setText("")
        self.label_11.setObjectName("label_11")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(505, 930, 221, 28))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(735, 930, 221, 28))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(965, 930, 221, 28))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(1195, 930, 221, 28))
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_5.setGeometry(QtCore.QRect(505, 960, 451, 28))
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_6 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_6.setGeometry(QtCore.QRect(965, 960, 451, 28))
        self.pushButton_6.setObjectName("pushButton_6")
        self.label_12 = QtWidgets.QLabel(self.centralwidget)
        self.label_12.setGeometry(QtCore.QRect(1397, 440, 501, 51))
        self.label_12.setObjectName("label_12")
        self.progressBar_3 = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar_3.setGeometry(QtCore.QRect(1550, 510, 351, 91))
        self.progressBar_3.setProperty("value", 24)
        self.progressBar_3.setObjectName("progressBar_3")
        self.label_11.raise_()
        self.progressBar.raise_()
        self.progressBar_2.raise_()
        self.label.raise_()
        self.label_2.raise_()
        self.label_4.raise_()
        self.label_3.raise_()
        self.label_5.raise_()
        self.label_6.raise_()
        self.label_7.raise_()
        self.label_8.raise_()
        self.label_9.raise_()
        self.label_10.raise_()
        self.pushButton.raise_()
        self.pushButton_2.raise_()
        self.pushButton_3.raise_()
        self.pushButton_4.raise_()
        self.pushButton_5.raise_()
        self.pushButton_6.raise_()
        self.label_12.raise_()
        self.progressBar_3.raise_()
        self._update_timer = QtCore.QTimer()
        self._update_timer.start(u)
        #self._update_timer.timeout.connect(self.get_cpu_utilization)
        self.start()
        self._update_timer.timeout.connect(self.calc_system_utilization)
        self._update_timer.timeout.connect(self.set_mem_disp)
        self._update_timer.timeout.connect(self.animate)
        self._update_timer.timeout.connect(self.animate_switch)
        self._update_timer.timeout.connect(self.update_progress_bars)
        self._update_timer.timeout.connect(self.temp_check)
        MainWindow.setCentralWidget(self.centralwidget)
        # self.statusbar = QtWidgets.QStatusBar(MainWindow)
        # self.statusbar.setObjectName("statusbar")
        # MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
    def set_mem_disp(self):
        meminfo = open("/proc/meminfo","r")
        meminfo_read = meminfo.read()
        self.label_9.setText(meminfo_read)
    def calc_system_utilization(self):
        global gpu_utilization,cpu_utilization
        # GET CPU UTILIZATION
        cpu_percent = int(cpu_utilization)

        # GET GPU UTILIZATION
        gpu_util = int(gpu_utilization)
        
        # GET RANDOMACCESS UTIL
        ram_info = psutil.virtual_memory()
        percent_used = int(ram_info.percent)
        print(percent_used)

        # CALCULATION
        avg_sys_use = int(round(((gpu_util + percent_used + cpu_percent) / 3)))
        print(avg_sys_use)
        self.progressBar_3.setValue(avg_sys_use)

    def start(self):
        # Call this method to start the GPU and CPU utilization updates
        threading.Thread(target=self.get_gpu_utilization).start()
        threading.Thread(target=self.get_cpu_utilization).start()
        self._update_timer.start(10)  # Update every 1 second

    def get_gpu_utilization(self):
        while True:
            try:
                output = subprocess.check_output(['nvidia-smi'])
                output_lines = output.decode('utf-8').strip().split('\n')

                # Find the line containing 'P0'
                p0_line = next((line for line in output_lines if 'P0' in line), None)

                if p0_line:
                    self.gpu_utilization = int(p0_line.split()[11].strip('%'))
                else:
                    self.gpu_utilization = 0
            except:
                self.gpu_utilization = 0
                print("Error")

    def get_cpu_utilization(self):
        while True:
            self.cpu_utilization = int(psutil.cpu_percent(interval=0.3))


    def paintEvent(self, event):
        painter = QPainter(self.progressBar)
        painter.setRenderHint(QPainter.Antialiasing)
        self.progressBar.setValue(self.progressBar.value())
        painter.end()
    def update_progress_bars(self):
        try:
            self.progressBar.setValue(self.cpu_utilization)
            self.progressBar_2.setValue(self.gpu_utilization)
        except:
            print("Error")
    def animate_switch(self):
        global c,u,m
        switch = int(open("switch_data.txt","r").read().replace("\n",""))
        print(switch)
        if switch == 1:
            if c >= 100:
                c = 100
            else:
                c += 1
        else:
            if c <=0:
                c = 0
            else:
                c -= 1
    def temp_check(self):
        global gpu
        try:
            temperature = gpu.temperature
        except:
            print("ERR_GPU")
        if temperature >= 80:
            print("HI_HALT_TEMP")
            os.system("python /home/zerone/temp_warn.py")
    def animate(self):
        global c,u,m
        self.label.setGeometry(QtCore.QRect(1700+c, -30, 201, 181))
        self.pushButton.setGeometry(QtCore.QRect(505, 930-c, 221, 28))
        self.pushButton_2.setGeometry(QtCore.QRect(735, 930-c, 221, 28))
        self.pushButton_3.setGeometry(QtCore.QRect(965, 930-c, 221, 28))
        self.pushButton_4.setGeometry(QtCore.QRect(1195, 930-c, 221, 28))
        self.pushButton_5.setGeometry(QtCore.QRect(505, 960-c, 451, 28))
        self.pushButton_6.setGeometry(QtCore.QRect(965, 960-c, 451, 28))
        self.progressBar.setGeometry(QtCore.QRect(0, 1020+c, 341, 71))
        self.progressBar_2.setGeometry(QtCore.QRect(1580, 1020+c, 341, 71))
        self.label_9.setGeometry(QtCore.QRect(30-c, 40, 391, 531))

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "z t O S Home Interface System"))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p align=\"right\"><span style=\" font-size:26pt;\">z t O S</span></p><p align=\"right\"><span style=\" font-size:10pt;\">upsilon v2.0</span></p><p align=\"right\"><span style=\" font-size:10pt;\">ZERONE LABORATORIES</span></p></body></html>"))
        self.label_2.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:16pt;\">CPU</span></p><p><span style=\" font-size:9pt;\">Central Processing Unit</span></p></body></html>"))
        self.label_4.setText(_translate("MainWindow", "<html><head/><body><p align=\"right\"><span style=\" font-size:16pt;\">NHPPU</span></p><p align=\"right\"><span style=\" font-size:9pt;\">Nvidia High Performance Processing Unit</span></p></body></html>"))
        self.label_3.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:14pt;\">Zerone Laboratories Home Interface v1.5 [UNDER DEV]</span></p><p>User : Zerone Brianstorm</p><p>OS version : ztOS v2.0 Upsilon Redesigned</p><p>ztOS Home : v1.6 Redesigned</p></body></html>"))
        self.label_5.setText(_translate("MainWindow", "C.O.R.E :"))
        self.label_6.setText(_translate("MainWindow", "UNAVAILABLE !"))
        self.label_7.setText(_translate("MainWindow", "UNAVAILABLE !"))
        self.label_8.setText(_translate("MainWindow", "Rigel :"))
        self.label_9.setText(_translate("MainWindow", "Mem Disp"))
        self.label_10.setText(_translate("MainWindow", "MemoryData"))
        self.pushButton.setText(_translate("MainWindow", "Hardware Monitoring Sys"))
        self.pushButton_2.setText(_translate("MainWindow", "Core Control"))
        self.pushButton_3.setText(_translate("MainWindow", "HyperScan"))
        self.pushButton_4.setText(_translate("MainWindow", "Rigel AI"))
        self.pushButton_5.setText(_translate("MainWindow", "ztOS Shutdown"))
        self.pushButton_6.setText(_translate("MainWindow", "ztOS System Reboot"))
        self.label_12.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:18pt;\">Stability Meter</span></p></body></html>"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

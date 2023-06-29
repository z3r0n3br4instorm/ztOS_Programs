# -*- coding: utf-8 -*-

from PyQt5 import QtCore, QtGui, QtWidgets
import os

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(661, 337)
        screen_geometry = QtWidgets.QApplication.desktop().screenGeometry()  # Get screen geometry

        # Calculate the desired position
        dialog_width = Dialog.width()
        dialog_height = Dialog.height()
        dialog_x = int(screen_geometry.width() / 2 - dialog_width / 2)
        dialog_y = int(screen_geometry.height() / 2 - dialog_height / 2)
        Dialog.move(dialog_x, dialog_y)  # Set dialog position

        # Rest of the code...


        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(0, 10, 661, 121))
        self.label.setObjectName("label")
        self.progressBar = QtWidgets.QProgressBar(Dialog)
        self.progressBar.setGeometry(QtCore.QRect(20, 160, 621, 101))
        self.progressBar.setStyleSheet("QProgressBar {background-color: black;} QProgressBar::chunk {background-color: #2f2f2f;} QProgressBar::chunk:disabled {background-color: #606060;}")
        self.progressBar.setFont(QtGui.QFont("Space Mono", 18))
        self.progressBar.setObjectName("progressBar")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(20, 280, 621, 41))
        self.label_2.setObjectName("label_2")
        self.label_2.setFont(QtGui.QFont("Space Mono", 9))

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

        # Slow loading animation
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.updateProgressBar)
        self.timer.start(15)
        self.progressValue = 0

    def updateProgressBar(self):
        self.progressValue += 1
        self.progressBar.setValue(self.progressValue)
        if self.progressValue == 10:
            #os.system("python /home/zerone/ztos_home_4.0.py&")
            print("SKIP")
        if self.progressValue == 48:
            self.label_2.setText("Initializing CORE...")
            os.system("uxterm -e 'neofetch --source /home/zerone/neotext && sudo python init_core.py'&")
        if self.progressValue == 49:
            #os.system("python ztos_lock.py")
            print("SKIP")
        if self.progressValue == 95:
            self.label_2.setText("Initializing ztOS Hardware Monitoring System...")
            os.system("python /home/zerone/ZeroneApps/hwm.py&")
        if self.progressValue >= 100:
            _translate = QtCore.QCoreApplication.translate
            self.label_2.setText("System Initialization Complete! Welcome To ztOS Upsilon v2.0 | ZeroneLabs Team")
            self.label.setText(_translate("Dialog", "<html><head/><body><p align=\"center\"><span style=\" font-size:45pt;\">z t O S - 2.0</span></p><p align=\"center\"><span style=\" font-size:18pt;\">P R O T O T Y P E</span></p></body></html>"))
            self.timer.stop()

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Zerone Technologies And Laboratories Operating System"))
        self.label.setText(_translate("Dialog", "<html><head/><body><p align=\"center\"><span style=\" font-size:45pt;\">z t O S</span></p><p align=\"center\"><span style=\" font-size:18pt;\">I N I T I A L I Z I N G</span></p></body></html>"))
        self.label_2.setText(_translate("Dialog", "Initializing Ui..."))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

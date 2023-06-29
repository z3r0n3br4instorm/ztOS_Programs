# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'lockdown.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
import os
from cryptography.fernet import Fernet
import base64
print("encrypting")
os.system("xterm -e python test.py")
print("encrypted")
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1920, 1080)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 0, 331, 181))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(350, 261, 461, 461))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("Pictures/propictemp.jpg"))
        self.label_2.setScaledContents(True)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(830, 271, 331, 81))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(830, 371, 331, 81))
        self.label_4.setObjectName("label_4")
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(1110, 300, 441, 51))
        self.textEdit.setObjectName("textEdit")
        self.textEdit_2 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_2.setGeometry(QtCore.QRect(1110, 400, 441, 51))
        self.textEdit_2.setObjectName("textEdit_2")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(830, 470, 731, 61))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(310, 90, 1411, 41))
        self.label_6.setObjectName("label_6")
        self.progressBar = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar.setGeometry(QtCore.QRect(830, 520, 731, 23))
        self.progressBar.setProperty("value", 24)
        self.progressBar.setObjectName("progressBar")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(1270, 380, 341, 401))
        self.label_7.setText("")
        self.label_7.setPixmap(QtGui.QPixmap("ZeroneApps/zrn_logo_no_back.png"))
        self.label_7.setScaledContents(True)
        self.label_7.setObjectName("label_7")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(1580, 320, 131, 101))
        self.pushButton.setObjectName("pushButton")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        self.pushButton.clicked.connect(self.decrypt_files_in_folder)
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
    def decrypt_files_in_folder(self):
        # Generate the encryption cipher
        folder_path = os.path.expanduser("/home/zerone/encrypttest/")
        with open('/home/zerone/key.txt', 'rb') as file:
            saved_key = file.read()
        print(saved_key)
        #saved_key_bytes = base64.urlsafe_b64decode(saved_key)
        cipher = Fernet(saved_key)

        # Iterate through all files in the folder
        for root, dirs, files in os.walk(folder_path):
            for file_name in files:
                file_path = os.path.join(root, file_name)

                # Decrypt only encrypted files
                if file_name.lower().endswith(('.jpg', '.jpeg', '.png', '.gif', '.bmp', '.txt', '.pdf', '.docx', '.xlsx', '.pptx', '.mp4', '.avi', '.mkv')):
                    try:
                        # Check if the file is encrypted
                        with open(file_path, 'rb') as file:
                            content = file.read()
                        if not content.startswith(b'GPT3_Encrypted'):
                            print(f"File is not encrypted: {file_path}")
                            self.label_5.setText(f"File is not encrypted: {file_path}")
                            continue  # Skip decryption and move to the next file

                        # Decrypt the file
                        encrypted_data = content[len(b'GPT3_Encrypted'):]
                        decrypted_data = cipher.decrypt(encrypted_data)
                        with open(file_path, 'wb') as file:
                            file.write(decrypted_data)
                        print(f"Decrypted: {file_path}")
                        self.label_5.setText(f"Decrypted: {file_path}")

                    except IOError as e:
                        print(f"Error decrypting {file_path}: {e}")
        self.label_5.setText("DECYPTION COMPLETE !, WELCOME BACK Mr.Brianstorm")
        sys.exit()
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:72pt;\">z t O S</span></p></body></html>"))
        self.label_3.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:28pt;\">U S E R N A M E :</span></p></body></html>"))
        self.label_4.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:28pt;\">P A S S W O R D :</span></p></body></html>"))
        self.label_5.setText(_translate("MainWindow", "File Encryption Running..."))
        self.label_6.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:20pt;\">//syslock v2.1 Enctryption System [incomplete !]</span></p></body></html>"))
        self.pushButton.setText(_translate("MainWindow", "LOGIN"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'destboard.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.

from PyQt5 import  uic,QtWidgets
from  time import sleep
import random
import threading
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1118, 706)
        MainWindow.setToolButtonStyle(QtCore.Qt.ToolButtonIconOnly)
        self.principal = QtWidgets.QWidget(MainWindow)
        self.principal.setObjectName("principal")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.principal)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.principal)
        self.label.setMaximumSize(QtCore.QSize(16777215, 70))
        font = QtGui.QFont()
        font.setFamily("Sitka Banner Semibold")
        font.setPointSize(26)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet("background-color: rgb(0, 22, 26);\n"
"color: rgb(255, 255, 255);")
        self.label.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.conta_imagens = QtWidgets.QFrame(self.principal)
        self.conta_imagens.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.conta_imagens.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.conta_imagens.setFrameShadow(QtWidgets.QFrame.Plain)
        self.conta_imagens.setObjectName("conta_imagens")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.conta_imagens)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_umidade = QtWidgets.QLabel(self.conta_imagens)
        self.label_umidade.setStyleSheet("background-color: rgb(0, 9, 9);")
        self.label_umidade.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label_umidade.setFrameShadow(QtWidgets.QFrame.Plain)
        self.label_umidade.setText("")
        self.label_umidade.setPixmap(QtGui.QPixmap(":/imagem1/temperaturas.png"))
        self.label_umidade.setAlignment(QtCore.Qt.AlignCenter)
        self.label_umidade.setObjectName("label_umidade")
        self.horizontalLayout.addWidget(self.label_umidade)
        self.label_temp = QtWidgets.QLabel(self.conta_imagens)
        self.label_temp.setStyleSheet("background-color: rgb(0, 9, 9);")
        self.label_temp.setText("")
        self.label_temp.setPixmap(QtGui.QPixmap(":/imagem2/temp.png"))
        self.label_temp.setAlignment(QtCore.Qt.AlignCenter)
        self.label_temp.setObjectName("label_temp")
        self.horizontalLayout.addWidget(self.label_temp)
        self.verticalLayout.addWidget(self.conta_imagens)
        self.label_temp_umid = QtWidgets.QFrame(self.principal)
        self.label_temp_umid.setMaximumSize(QtCore.QSize(16777215, 60))
        self.label_temp_umid.setStyleSheet("background-color: rgb(0, 22, 26);")
        self.label_temp_umid.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.label_temp_umid.setFrameShadow(QtWidgets.QFrame.Raised)
        self.label_temp_umid.setObjectName("label_temp_umid")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.label_temp_umid)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_2 = QtWidgets.QLabel(self.label_temp_umid)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color: rgb(0, 128, 135);")
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.label_3 = QtWidgets.QLabel(self.label_temp_umid)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("color: rgb(0, 128, 135);")
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_2.addWidget(self.label_3)
        self.verticalLayout.addWidget(self.label_temp_umid)
        self.cont_principal = QtWidgets.QFrame(self.principal)
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.cont_principal.setFont(font)
        self.cont_principal.setStyleSheet("background-color: rgb(0, 22, 26);")
        self.cont_principal.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.cont_principal.setFrameShadow(QtWidgets.QFrame.Plain)
        self.cont_principal.setObjectName("cont_principal")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.cont_principal)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.lb_umi = QtWidgets.QLabel(self.cont_principal)
        font = QtGui.QFont()
        font.setFamily("MV Boli")
        font.setPointSize(72)
        self.lb_umi.setFont(font)
        self.lb_umi.setStyleSheet("color: rgb(170, 255, 255);")
        self.lb_umi.setTextFormat(QtCore.Qt.PlainText)
        self.lb_umi.setScaledContents(False)
        self.lb_umi.setAlignment(QtCore.Qt.AlignCenter)
        self.lb_umi.setObjectName("lb_umi")
        self.horizontalLayout_3.addWidget(self.lb_umi)
        self.lb_temp = QtWidgets.QLabel(self.cont_principal)
        font = QtGui.QFont()
        font.setFamily("MV Boli")
        font.setPointSize(72)
        self.lb_temp.setFont(font)
        self.lb_temp.setStyleSheet("color: rgb(170, 255, 255);")
        self.lb_temp.setAlignment(QtCore.Qt.AlignCenter)
        self.lb_temp.setObjectName("lb_temp")
        self.horizontalLayout_3.addWidget(self.lb_temp)
        self.verticalLayout.addWidget(self.cont_principal)
        self.iniciar = QtWidgets.QPushButton(self.principal)
        self.iniciar.setMaximumSize(QtCore.QSize(16777215, 50))
        self.iniciar.setStyleSheet("background-color: rgb(3, 160, 168);")
        self.iniciar.setObjectName("iniciar")
        self.verticalLayout.addWidget(self.iniciar)
        self.stop = QtWidgets.QPushButton(self.principal)
        self.stop.setMaximumSize(QtCore.QSize(16777215, 50))
        self.stop.setStyleSheet("background-color: rgb(113, 0, 0);")
        self.stop.setObjectName("stop")
        self.verticalLayout.addWidget(self.stop)
        MainWindow.setCentralWidget(self.principal)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1118, 26))
        self.menubar.setDefaultUp(False)
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "UT- IoT"))
        self.label_2.setText(_translate("MainWindow", "Umidade em %"))
        self.label_3.setText(_translate("MainWindow", "Temperatura em °C"))
        self.lb_umi.setText(_translate("MainWindow", "45"))
        self.lb_temp.setText(_translate("MainWindow", "35"))
        self.iniciar.setText(_translate("MainWindow", "Iniciar"))
        self.stop.setText(_translate("MainWindow", "stop"))
        self.iniciar.clicked.connect(self.teste)
        self.stop.clicked.connect(self.stopS)
        
    def teste(self):
        def inicar():
            for contagem in range(0,10):
                x = random.randrange(1,52)
                y = random.randrange(1,40)
                sleep(1)
                print('numero',contagem)
                self.lb_umi.setText(str(x))
                self.lb_temp.setText(str(y))
        threading.Thread(target=inicar).start()
    
    
    def stopS(self):
        self.lb_umi.setText("0")
        self.lb_temp.setText("0")
          
#import projeto_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

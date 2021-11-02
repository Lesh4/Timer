from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QCursor
import sys
import subprocess
import time


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        # инициализация окна интерфейса
        MainWindow.setObjectName("MainWindow")

        MainWindow.setFixedSize(716, 463)
        MainWindow.setAutoFillBackground(False)
        MainWindow.setStyleSheet("background-color: rgb(79, 79, 79);")
        MainWindow.setWindowTitle("Таймер автовыключения")

        # инициализация центрального виджета
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.centralwidget.setObjectName("centralwidget")

        # инициализация вертикального лейаута, где будут часы и крутилки
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(180, 100, 361, 231))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.interface_layout = QtWidgets.QVBoxLayout(
            self.verticalLayoutWidget)
        self.interface_layout.setContentsMargins(0, 0, 0, 0)
        self.interface_layout.setObjectName("interface_layout")

        # инициализация горизонтального лейаута, где будут часы
        self.clock_layout = QtWidgets.QHBoxLayout()
        self.clock_layout.setObjectName("clock_layout")

        # инициализация метки 'часы'
        self.h_lab = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Noto Serif")
        font.setPointSize(48)
        self.h_lab.setFont(font)
        self.h_lab.setStyleSheet("color: rgb(255, 255, 255);")
        self.h_lab.setObjectName("h_lab")
        self.h_lab.setText("00")
        self.clock_layout.addWidget(self.h_lab)

        self.line_2 = QtWidgets.QFrame(self.verticalLayoutWidget)
        self.line_2.setStyleSheet("")
        self.line_2.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.clock_layout.addWidget(self.line_2)

        # инициализация метки 'минуты'
        self.m_lab = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Noto Serif")
        font.setPointSize(48)
        self.m_lab.setFont(font)
        self.m_lab.setStyleSheet("color: rgb(255, 255, 255);")
        self.m_lab.setObjectName("m_lab")
        self.m_lab.setText("00")
        self.clock_layout.addWidget(self.m_lab)

        self.line = QtWidgets.QFrame(self.verticalLayoutWidget)
        self.line.setStyleSheet("color: rgb(255, 255, 255);")
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.clock_layout.addWidget(self.line)

        # инициализация метки 'секунды'
        self.s_lab = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Noto Serif")
        font.setPointSize(48)
        self.s_lab.setFont(font)
        self.s_lab.setStyleSheet("color: rgb(255, 255, 255);")
        self.s_lab.setObjectName("s_lab")
        self.s_lab.setText("00")
        self.clock_layout.addWidget(self.s_lab)

        self.interface_layout.addLayout(self.clock_layout)

        # инициализация горизонтального лейаута, где будут крутилки
        self.dial_layout = QtWidgets.QHBoxLayout()
        self.dial_layout.setObjectName("dial_layout")

        # инициализация крутилки 'часы'
        self.h_dial = QtWidgets.QDial(self.verticalLayoutWidget)
        self.h_dial.setStyleSheet("background-color: rgb(85, 170, 0);")
        self.h_dial.setObjectName("h_dial")
        self.h_dial.setMaximum(59)
        self.h_dial.valueChanged.connect(
            lambda x: self.dial_moved(self.h_dial))
        self.dial_layout.addWidget(self.h_dial)

        # инициализация крутилки 'минуты'
        self.m_dial = QtWidgets.QDial(self.verticalLayoutWidget)
        self.m_dial.setStyleSheet("background-color: rgb(85, 170, 0);")
        self.m_dial.setObjectName("m_dial")
        self.m_dial.setMaximum(59)
        self.m_dial.valueChanged.connect(
            lambda x: self.dial_moved(self.m_dial))
        self.dial_layout.addWidget(self.m_dial)

        # инициализация крутилки 'секунды'
        self.s_dial = QtWidgets.QDial(self.verticalLayoutWidget)
        self.s_dial.setStyleSheet("background-color: rgb(85, 170, 0);")
        self.s_dial.setObjectName("s_dial")
        self.s_dial.setMaximum(59)
        self.s_dial.valueChanged.connect(
            lambda x: self.dial_moved(self.s_dial))
        self.dial_layout.addWidget(self.s_dial)

        self.interface_layout.addLayout(self.dial_layout)

        # инициализация кнопки ОК
        self.ok_b = QtWidgets.QPushButton(self.centralwidget)
        self.ok_b.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
        self.ok_b.setGeometry(QtCore.QRect(600, 390, 81, 41))
        self.ok_b.setStyleSheet(
            "*{border: 4px solid rgb(85, 170, 0);" +
            "border-radius: 15px;" +
            "color: white;" +
            "font: Noto Serif;}" +
            "*:hover{background-color: rgb(85, 170, 0);}"
        )
        self.ok_b.setObjectName("ok_b")
        self.ok_b.setText("Ок")
        self.ok_b.clicked.connect(lambda x: self.btn_clicked(self.ok_b))

        # инициализация кнопки Отмена
        self.cancel_b = QtWidgets.QPushButton(self.centralwidget)
        self.cancel_b.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
        self.cancel_b.setGeometry(QtCore.QRect(500, 390, 81, 41))
        self.cancel_b.setStyleSheet("color: rgb(255, 255, 255);")
        self.cancel_b.setStyleSheet(
            "*{border: 4px solid rgb(85, 170, 0);" +
            "border-radius: 15px;" +
            "color: white;" +
            "font: Noto Serif;}" +
            "*:hover{background-color: rgb(85, 170, 0);}"
        )
        self.cancel_b.setObjectName("cancel_b")
        self.cancel_b.setText("Отмена")
        self.cancel_b.clicked.connect(
            lambda x: self.btn_clicked(self.cancel_b))

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def dial_moved(self, dial):
        name = dial.objectName()
        value = dial.value()
        if name == 'h_dial':
            self.h_lab.setText(str(value).zfill(2))
        elif name == 'm_dial':
            self.m_lab.setText(str(value).zfill(2))
        elif name == 's_dial':
            self.s_lab.setText(str(value).zfill(2))

    def time_convert(self):
        hours = int(self.h_lab.text())
        minutes = int(self.m_lab.text())
        seconds = int(self.s_lab.text())
        return seconds + minutes*60 + hours*3600

    def countdown(self):
        self.myTimer = QtCore.QTimer(MainWindow)
        self.myTimer.timeout.connect(self.timerTimeout)
        self.myTimer.start(1000)

    def timerTimeout(self):
        self.time -= 1
        self.update_gui()

    def update_gui(self):
        hours, minutes = divmod(self.time, 3600)
        minutes, seconds = divmod(minutes, 60)
        self.h_lab.setText(str(hours).zfill(2))
        self.m_lab.setText(str(minutes).zfill(2))
        self.s_lab.setText(str(seconds).zfill(2))

    def btn_clicked(self, btn):
        name = btn.objectName()
        if name == 'ok_b':
            self.time = self.time_convert()
            _ = subprocess.run(['shutdown', '-s', '-t', str(self.time)])
            self.countdown()
        elif name == 'cancel_b':
            _ = subprocess.run(['shutdown', '-a'])
            self.myTimer.stop()
            self.h_lab.setText("00")
            self.m_lab.setText("00")
            self.s_lab.setText("00")

            self.h_dial.setValue(0)
            self.m_dial.setValue(0)
            self.s_dial.setValue(0)



if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    app.setWindowIcon(QtGui.QIcon('clock.ico'))
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())

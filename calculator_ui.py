from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtGui import QShortcut


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(300, 500)
        MainWindow.setMinimumSize(QtCore.QSize(300, 500))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/icons/calculator.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet("QWidget {\n""color: white;\n""background-color: #121212;\n"
        "font-family: Rubik;\n""font-size: 16pt;\n""font-weight: 600;\n""}\n""\n""QPushButton {\n"
        "background-color: transparent;\n""border: none;\n""}\n""\n""QPushButton:hover {\n"
        "background-color: #666;\n""}\n""\n""QPushButton:pressed {\n""background-color: #888;\n""}")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.labels_layout = QtWidgets.QVBoxLayout()
        self.labels_layout.setObjectName("labels_layout")
        self.exp_label = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.exp_label.sizePolicy().hasHeightForWidth())
        self.exp_label.setSizePolicy(sizePolicy)
        self.exp_label.setStyleSheet("color: #888;border: none;font-weight: 400;")
        self.exp_label.setText("")
        self.exp_label.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight | QtCore.Qt.AlignmentFlag.AlignTrailing | QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.exp_label.setObjectName("exp_label")
        self.labels_layout.addWidget(self.exp_label)
        self.num_label = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.num_label.sizePolicy().hasHeightForWidth())
        self.num_label.setSizePolicy(sizePolicy)
        self.num_label.setStyleSheet("font-size: 40pt;border: none;")
        self.num_label.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight | QtCore.Qt.AlignmentFlag.AlignTrailing | QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.num_label.setObjectName("num_label")
        self.labels_layout.addWidget(self.num_label)
        self.verticalLayout.addLayout(self.labels_layout)
        self.buttons_layout = QtWidgets.QGridLayout()
        self.buttons_layout.setObjectName("buttons_layout")
        self.btn_3 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_3.sizePolicy().hasHeightForWidth())
        self.btn_3.setSizePolicy(sizePolicy)
        self.btn_3.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.btn_3.setObjectName("btn_3")
        self.buttons_layout.addWidget(self.btn_3, 3, 2, 1, 1)
        self.btn_clear_num = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_clear_num.sizePolicy().hasHeightForWidth())
        self.btn_clear_num.setSizePolicy(sizePolicy)
        self.btn_clear_num.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.btn_clear_num.setObjectName("btn_clear_num")
        self.buttons_layout.addWidget(self.btn_clear_num, 0, 0, 1, 1)
        self.btn_1 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_1.sizePolicy().hasHeightForWidth())
        self.btn_1.setSizePolicy(sizePolicy)
        self.btn_1.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.btn_1.setObjectName("btn_1")
        self.buttons_layout.addWidget(self.btn_1, 3, 0, 1, 1)
        self.btn_4 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_4.sizePolicy().hasHeightForWidth())
        self.btn_4.setSizePolicy(sizePolicy)
        self.btn_4.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.btn_4.setObjectName("btn_4")
        self.buttons_layout.addWidget(self.btn_4, 2, 0, 1, 1)
        self.btn_multiplication = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_multiplication.sizePolicy().hasHeightForWidth())
        self.btn_multiplication.setSizePolicy(sizePolicy)
        self.btn_multiplication.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.btn_multiplication.setObjectName("btn_multiplication")
        self.buttons_layout.addWidget(self.btn_multiplication, 1, 3, 1, 1)
        self.btn_point = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_point.sizePolicy().hasHeightForWidth())
        self.btn_point.setSizePolicy(sizePolicy)
        self.btn_point.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.btn_point.setObjectName("btn_point")
        self.buttons_layout.addWidget(self.btn_point, 4, 2, 1, 1)
        self.btn_7 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_7.sizePolicy().hasHeightForWidth())
        self.btn_7.setSizePolicy(sizePolicy)
        self.btn_7.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.btn_7.setObjectName("btn_7")
        self.buttons_layout.addWidget(self.btn_7, 1, 0, 1, 1)
        self.btn_0 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_0.sizePolicy().hasHeightForWidth())
        self.btn_0.setSizePolicy(sizePolicy)
        self.btn_0.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.btn_0.setObjectName("btn_0")
        self.buttons_layout.addWidget(self.btn_0, 4, 1, 1, 1)
        self.btn_negate = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_negate.sizePolicy().hasHeightForWidth())
        self.btn_negate.setSizePolicy(sizePolicy)
        self.btn_negate.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.btn_negate.setObjectName("btn_negate")
        self.buttons_layout.addWidget(self.btn_negate, 4, 0, 1, 1)
        self.btn_equals = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_equals.sizePolicy().hasHeightForWidth())
        self.btn_equals.setSizePolicy(sizePolicy)
        self.btn_equals.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.btn_equals.setObjectName("btn_equals")
        self.buttons_layout.addWidget(self.btn_equals, 4, 3, 1, 1)
        self.btn_addition = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_addition.sizePolicy().hasHeightForWidth())
        self.btn_addition.setSizePolicy(sizePolicy)
        self.btn_addition.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.btn_addition.setObjectName("btn_addition")
        self.buttons_layout.addWidget(self.btn_addition, 3, 3, 1, 1)
        self.btn_subtraction = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_subtraction.sizePolicy().hasHeightForWidth())
        self.btn_subtraction.setSizePolicy(sizePolicy)
        self.btn_subtraction.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.btn_subtraction.setObjectName("btn_subtraction")
        self.buttons_layout.addWidget(self.btn_subtraction, 2, 3, 1, 1)
        self.btn_division = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_division.sizePolicy().hasHeightForWidth())
        self.btn_division.setSizePolicy(sizePolicy)
        self.btn_division.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.btn_division.setObjectName("btn_division")
        self.buttons_layout.addWidget(self.btn_division, 0, 3, 1, 1)
        self.btn_2 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_2.sizePolicy().hasHeightForWidth())
        self.btn_2.setSizePolicy(sizePolicy)
        self.btn_2.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.btn_2.setObjectName("btn_2")
        self.buttons_layout.addWidget(self.btn_2, 3, 1, 1, 1)
        self.btn_backspace = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_backspace.sizePolicy().hasHeightForWidth())
        self.btn_backspace.setSizePolicy(sizePolicy)
        self.btn_backspace.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.btn_backspace.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/icons/icons/backspace.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.btn_backspace.setIcon(icon1)
        self.btn_backspace.setIconSize(QtCore.QSize(24, 24))
        self.btn_backspace.setObjectName("btn_backspace")
        self.buttons_layout.addWidget(self.btn_backspace, 0, 2, 1, 1)
        self.btn_5 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_5.sizePolicy().hasHeightForWidth())
        self.btn_5.setSizePolicy(sizePolicy)
        self.btn_5.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.btn_5.setObjectName("btn_5")
        self.buttons_layout.addWidget(self.btn_5, 2, 1, 1, 1)
        self.btn_9 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_9.sizePolicy().hasHeightForWidth())
        self.btn_9.setSizePolicy(sizePolicy)
        self.btn_9.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.btn_9.setShortcut("")
        self.btn_9.setObjectName("btn_9")
        self.buttons_layout.addWidget(self.btn_9, 1, 2, 1, 1)
        self.btn_8 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_8.sizePolicy().hasHeightForWidth())
        self.btn_8.setSizePolicy(sizePolicy)
        self.btn_8.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.btn_8.setShortcut("")
        self.btn_8.setObjectName("btn_8")
        self.buttons_layout.addWidget(self.btn_8, 1, 1, 1, 1)
        self.btn_clear_all = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_clear_all.sizePolicy().hasHeightForWidth())
        self.btn_clear_all.setSizePolicy(sizePolicy)
        self.btn_clear_all.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.btn_clear_all.setShortcut("")
        self.btn_clear_all.setObjectName("btn_clear_all")
        self.buttons_layout.addWidget(self.btn_clear_all, 0, 1, 1, 1)
        self.btn_6 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_6.sizePolicy().hasHeightForWidth())
        self.btn_6.setSizePolicy(sizePolicy)
        self.btn_6.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.btn_6.setObjectName("btn_6")
        self.buttons_layout.addWidget(self.btn_6, 2, 2, 1, 1)
        self.verticalLayout.addLayout(self.buttons_layout)
        self.verticalLayout.setStretch(0, 1)
        self.verticalLayout.setStretch(1, 3)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Culculator"))
        self.num_label.setText(_translate("MainWindow", "0"))
        self.btn_3.setText(_translate("MainWindow", "3"))
        self.btn_clear_num.setText(_translate("MainWindow", "CE"))
        self.btn_1.setText(_translate("MainWindow", "1"))
        self.btn_1.setShortcut(_translate("MainWindow", "1"))
        self.btn_4.setText(_translate("MainWindow", "4"))
        self.btn_4.setShortcut(_translate("MainWindow", "4"))
        self.btn_multiplication.setText(_translate("MainWindow", "x"))
        self.btn_multiplication.setShortcut(_translate("MainWindow", "*"))
        self.btn_point.setText(_translate("MainWindow", "."))

        for sc in (',', '.'):
            QShortcut(sc, self.btn_point).activated.connect(self.btn_point.animateClick)

        self.btn_7.setText(_translate("MainWindow", "7"))
        self.btn_0.setText(_translate("MainWindow", "0"))
        self.btn_0.setShortcut(_translate("MainWindow", "0"))
        self.btn_negate.setText(_translate("MainWindow", "+/-"))
        self.btn_equals.setText(_translate("MainWindow", "="))

        for sc in ('=', 'Enter', 'Return'):
            QShortcut(sc, self.btn_equals).activated.connect(self.btn_equals.animateClick)

        self.btn_addition.setText(_translate("MainWindow", "+"))
        self.btn_addition.setShortcut(_translate("MainWindow", "+"))
        self.btn_subtraction.setText(_translate("MainWindow", "-"))
        self.btn_subtraction.setShortcut(_translate("MainWindow", "-"))
        self.btn_division.setText(_translate("MainWindow", "/"))
        self.btn_division.setShortcut(_translate("MainWindow", "/"))
        self.btn_2.setText(_translate("MainWindow", "2"))
        self.btn_2.setShortcut(_translate("MainWindow", "2"))
        self.btn_backspace.setShortcut(_translate("MainWindow", "Backspace"))
        self.btn_5.setText(_translate("MainWindow", "5"))
        self.btn_9.setText(_translate("MainWindow", "9"))
        self.btn_8.setText(_translate("MainWindow", "8"))
        self.btn_clear_all.setText(_translate("MainWindow", "C"))
        self.btn_6.setText(_translate("MainWindow", "6"))
        self.btn_6.setShortcut(_translate("MainWindow", "6"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())

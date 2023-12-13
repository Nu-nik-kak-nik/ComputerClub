# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_login.ui'
##
## Created by: Qt User Interface Compiler version 6.5.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QLineEdit,
    QMainWindow, QPushButton, QSizePolicy, QVBoxLayout,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(322, 328)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.l_entry = QLabel(self.centralwidget)
        self.l_entry.setObjectName(u"l_entry")

        self.verticalLayout.addWidget(self.l_entry)

        self.l_info = QLabel(self.centralwidget)
        self.l_info.setObjectName(u"l_info")

        self.verticalLayout.addWidget(self.l_info)

        self.l_login = QLabel(self.centralwidget)
        self.l_login.setObjectName(u"l_login")

        self.verticalLayout.addWidget(self.l_login)

        self.le_login = QLineEdit(self.centralwidget)
        self.le_login.setObjectName(u"le_login")

        self.verticalLayout.addWidget(self.le_login)

        self.l_password = QLabel(self.centralwidget)
        self.l_password.setObjectName(u"l_password")

        self.verticalLayout.addWidget(self.l_password)

        self.layout_password = QHBoxLayout()
        self.layout_password.setObjectName(u"layout_password")
        self.le_password = QLineEdit(self.centralwidget)
        self.le_password.setObjectName(u"le_password")

        self.layout_password.addWidget(self.le_password)

        self.btn_visibility = QPushButton(self.centralwidget)
        self.btn_visibility.setObjectName(u"btn_visibility")
        self.btn_visibility.setCheckable(True)

        self.layout_password.addWidget(self.btn_visibility)


        self.verticalLayout.addLayout(self.layout_password)

        self.btn_login = QPushButton(self.centralwidget)
        self.btn_login.setObjectName(u"btn_login")

        self.verticalLayout.addWidget(self.btn_login)

        self.btn_registration = QPushButton(self.centralwidget)
        self.btn_registration.setObjectName(u"btn_registration")

        self.verticalLayout.addWidget(self.btn_registration)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.l_entry.setText(QCoreApplication.translate("MainWindow", u"\u0412\u0445\u043e\u0434", None))
        self.l_info.setText("")
        self.l_login.setText(QCoreApplication.translate("MainWindow", u"\u041b\u043e\u0433\u0438\u043d", None))
        self.l_password.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0430\u0440\u043e\u043b\u044c", None))
        self.btn_visibility.setText(QCoreApplication.translate("MainWindow", u"V", None))
        self.btn_login.setText(QCoreApplication.translate("MainWindow", u"\u0412\u0445\u043e\u0434", None))
        self.btn_registration.setText(QCoreApplication.translate("MainWindow", u"\u0420\u0435\u0433\u0438\u0441\u0442\u0440\u0430\u0446\u0438\u044f", None))
    # retranslateUi


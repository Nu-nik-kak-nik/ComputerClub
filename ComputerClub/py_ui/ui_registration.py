# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_registration.ui'
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
from PySide6.QtWidgets import (QApplication, QDateEdit, QGridLayout, QHBoxLayout,
    QLabel, QLineEdit, QMainWindow, QPushButton,
    QSizePolicy, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(322, 386)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.l_registration = QLabel(self.centralwidget)
        self.l_registration.setObjectName(u"l_registration")

        self.verticalLayout.addWidget(self.l_registration)

        self.layout_names = QGridLayout()
        self.layout_names.setObjectName(u"layout_names")
        self.le_firstname = QLineEdit(self.centralwidget)
        self.le_firstname.setObjectName(u"le_firstname")

        self.layout_names.addWidget(self.le_firstname, 1, 0, 1, 1)

        self.le_firstname_2 = QLabel(self.centralwidget)
        self.le_firstname_2.setObjectName(u"le_firstname_2")

        self.layout_names.addWidget(self.le_firstname_2, 0, 0, 1, 1)

        self.le_surname = QLineEdit(self.centralwidget)
        self.le_surname.setObjectName(u"le_surname")

        self.layout_names.addWidget(self.le_surname, 1, 1, 1, 1)

        self.le_surname_2 = QLabel(self.centralwidget)
        self.le_surname_2.setObjectName(u"le_surname_2")

        self.layout_names.addWidget(self.le_surname_2, 0, 1, 1, 1)

        self.le_midlename = QLineEdit(self.centralwidget)
        self.le_midlename.setObjectName(u"le_midlename")

        self.layout_names.addWidget(self.le_midlename, 1, 2, 1, 1)

        self.l_midlename = QLabel(self.centralwidget)
        self.l_midlename.setObjectName(u"l_midlename")

        self.layout_names.addWidget(self.l_midlename, 0, 2, 1, 1)


        self.verticalLayout.addLayout(self.layout_names)

        self.layout_email_birth = QGridLayout()
        self.layout_email_birth.setObjectName(u"layout_email_birth")
        self.l_birth = QLabel(self.centralwidget)
        self.l_birth.setObjectName(u"l_birth")

        self.layout_email_birth.addWidget(self.l_birth, 0, 1, 1, 1)

        self.de_birth = QDateEdit(self.centralwidget)
        self.de_birth.setObjectName(u"de_birth")

        self.layout_email_birth.addWidget(self.de_birth, 1, 1, 1, 1)

        self.le_email = QLineEdit(self.centralwidget)
        self.le_email.setObjectName(u"le_email")

        self.layout_email_birth.addWidget(self.le_email, 1, 0, 1, 1)

        self.l_email = QLabel(self.centralwidget)
        self.l_email.setObjectName(u"l_email")

        self.layout_email_birth.addWidget(self.l_email, 0, 0, 1, 1)


        self.verticalLayout.addLayout(self.layout_email_birth)

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

        self.layout_password.addWidget(self.btn_visibility)


        self.verticalLayout.addLayout(self.layout_password)

        self.l_repeat_password = QLabel(self.centralwidget)
        self.l_repeat_password.setObjectName(u"l_repeat_password")

        self.verticalLayout.addWidget(self.l_repeat_password)

        self.layout_repeat_password = QHBoxLayout()
        self.layout_repeat_password.setObjectName(u"layout_repeat_password")
        self.le_repeat_password = QLineEdit(self.centralwidget)
        self.le_repeat_password.setObjectName(u"le_repeat_password")

        self.layout_repeat_password.addWidget(self.le_repeat_password)

        self.btn_visibility2 = QPushButton(self.centralwidget)
        self.btn_visibility2.setObjectName(u"btn_visibility2")

        self.layout_repeat_password.addWidget(self.btn_visibility2)


        self.verticalLayout.addLayout(self.layout_repeat_password)

        self.btn_registration = QPushButton(self.centralwidget)
        self.btn_registration.setObjectName(u"btn_registration")

        self.verticalLayout.addWidget(self.btn_registration)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.l_registration.setText(QCoreApplication.translate("MainWindow", u"\u0420\u0435\u0433\u0438\u0441\u0442\u0440\u0430\u0446\u0438\u044f", None))
        self.le_firstname_2.setText(QCoreApplication.translate("MainWindow", u"\u0418\u043c\u044f", None))
        self.le_surname_2.setText(QCoreApplication.translate("MainWindow", u"\u0424\u0430\u043c\u0438\u043b\u0438\u044f", None))
        self.l_midlename.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0442\u0447\u0435\u0441\u0442\u0432\u043e", None))
        self.l_birth.setText(QCoreApplication.translate("MainWindow", u"\u0414\u0430\u0442\u0430 \u0440\u043e\u0436\u0434\u0435\u043d\u0438\u044f", None))
        self.l_email.setText(QCoreApplication.translate("MainWindow", u"\u041f\u043e\u0447\u0442\u0430", None))
        self.l_login.setText(QCoreApplication.translate("MainWindow", u"\u041b\u043e\u0433\u0438\u043d", None))
        self.l_password.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0430\u0440\u043e\u043b\u044c", None))
        self.btn_visibility.setText(QCoreApplication.translate("MainWindow", u"V", None))
        self.l_repeat_password.setText(QCoreApplication.translate("MainWindow", u"\u041f\u043e\u0432\u0442\u043e\u0440\u0438\u0442\u0435 \u043f\u0430\u0440\u043e\u043b\u044c", None))
        self.btn_visibility2.setText(QCoreApplication.translate("MainWindow", u"V", None))
        self.btn_registration.setText(QCoreApplication.translate("MainWindow", u"\u0417\u0430\u0440\u0435\u0433\u0438\u0441\u0442\u0440\u0438\u0440\u043e\u0432\u0430\u0442\u044c\u0441\u044f", None))
    # retranslateUi


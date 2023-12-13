# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_main_admin.ui'
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QHBoxLayout, QHeaderView,
    QLabel, QMainWindow, QPushButton, QSizePolicy,
    QSpacerItem, QTableWidget, QTableWidgetItem, QVBoxLayout,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(538, 390)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout_2 = QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.layout_display_table = QVBoxLayout()
        self.layout_display_table.setObjectName(u"layout_display_table")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")

        self.layout_display_table.addWidget(self.label)

        self.table_bd = QTableWidget(self.centralwidget)
        self.table_bd.setObjectName(u"table_bd")

        self.layout_display_table.addWidget(self.table_bd)


        self.gridLayout.addLayout(self.layout_display_table, 1, 0, 1, 1)

        self.layout_functionality = QVBoxLayout()
        self.layout_functionality.setObjectName(u"layout_functionality")
        self.btn_logout = QPushButton(self.centralwidget)
        self.btn_logout.setObjectName(u"btn_logout")
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_logout.sizePolicy().hasHeightForWidth())
        self.btn_logout.setSizePolicy(sizePolicy)
        self.btn_logout.setMinimumSize(QSize(35, 35))
        self.btn_logout.setMaximumSize(QSize(35, 35))
        self.btn_logout.setSizeIncrement(QSize(0, 0))
        self.btn_logout.setBaseSize(QSize(0, 0))
        self.btn_logout.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_logout.setLayoutDirection(Qt.LeftToRight)
        self.btn_logout.setInputMethodHints(Qt.ImhNone)
        self.btn_logout.setAutoRepeat(False)
        self.btn_logout.setAutoRepeatDelay(300)
        self.btn_logout.setAutoRepeatInterval(100)

        self.layout_functionality.addWidget(self.btn_logout)

        self.btn_save = QPushButton(self.centralwidget)
        self.btn_save.setObjectName(u"btn_save")
        sizePolicy.setHeightForWidth(self.btn_save.sizePolicy().hasHeightForWidth())
        self.btn_save.setSizePolicy(sizePolicy)
        self.btn_save.setMinimumSize(QSize(35, 35))
        self.btn_save.setMaximumSize(QSize(35, 35))
        self.btn_save.setSizeIncrement(QSize(0, 0))
        self.btn_save.setBaseSize(QSize(0, 0))
        self.btn_save.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_save.setLayoutDirection(Qt.LeftToRight)
        self.btn_save.setInputMethodHints(Qt.ImhNone)
        self.btn_save.setAutoRepeat(False)
        self.btn_save.setAutoRepeatDelay(300)
        self.btn_save.setAutoRepeatInterval(100)

        self.layout_functionality.addWidget(self.btn_save)

        self.btn_create = QPushButton(self.centralwidget)
        self.btn_create.setObjectName(u"btn_create")
        sizePolicy.setHeightForWidth(self.btn_create.sizePolicy().hasHeightForWidth())
        self.btn_create.setSizePolicy(sizePolicy)
        self.btn_create.setMinimumSize(QSize(35, 35))
        self.btn_create.setMaximumSize(QSize(35, 35))
        self.btn_create.setSizeIncrement(QSize(0, 0))
        self.btn_create.setBaseSize(QSize(0, 0))
        self.btn_create.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_create.setLayoutDirection(Qt.LeftToRight)
        self.btn_create.setInputMethodHints(Qt.ImhNone)
        self.btn_create.setAutoRepeat(False)
        self.btn_create.setAutoRepeatDelay(300)
        self.btn_create.setAutoRepeatInterval(100)

        self.layout_functionality.addWidget(self.btn_create)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.layout_functionality.addItem(self.verticalSpacer)


        self.gridLayout.addLayout(self.layout_functionality, 0, 1, 2, 1)

        self.layout_table_buttons = QHBoxLayout()
        self.layout_table_buttons.setObjectName(u"layout_table_buttons")
        self.btn_reservation = QPushButton(self.centralwidget)
        self.btn_reservation.setObjectName(u"btn_reservation")
        self.btn_reservation.setMinimumSize(QSize(35, 35))
        self.btn_reservation.setCheckable(True)

        self.layout_table_buttons.addWidget(self.btn_reservation)

        self.btn_users = QPushButton(self.centralwidget)
        self.btn_users.setObjectName(u"btn_users")
        self.btn_users.setMinimumSize(QSize(35, 35))
        self.btn_users.setCheckable(True)

        self.layout_table_buttons.addWidget(self.btn_users)

        self.btn_computer = QPushButton(self.centralwidget)
        self.btn_computer.setObjectName(u"btn_computer")
        self.btn_computer.setMinimumSize(QSize(35, 35))
        self.btn_computer.setCheckable(True)

        self.layout_table_buttons.addWidget(self.btn_computer)

        self.btn_tariff = QPushButton(self.centralwidget)
        self.btn_tariff.setObjectName(u"btn_tariff")
        self.btn_tariff.setMinimumSize(QSize(35, 35))
        self.btn_tariff.setCheckable(True)

        self.layout_table_buttons.addWidget(self.btn_tariff)


        self.gridLayout.addLayout(self.layout_table_buttons, 0, 0, 1, 1)


        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"\u0424\u0438\u043b\u044c\u0442\u0440\u0430\u0446\u0438\u044f", None))
        self.btn_logout.setText(QCoreApplication.translate("MainWindow", u"L", None))
        self.btn_save.setText(QCoreApplication.translate("MainWindow", u"S", None))
        self.btn_create.setText(QCoreApplication.translate("MainWindow", u"C", None))
        self.btn_reservation.setText(QCoreApplication.translate("MainWindow", u"\u0411\u0440\u043e\u043d\u0438", None))
        self.btn_users.setText(QCoreApplication.translate("MainWindow", u"\u041f\u043e\u043b\u044c\u0437\u043e\u0432\u0430\u0442\u0435\u043b\u0438", None))
        self.btn_computer.setText(QCoreApplication.translate("MainWindow", u"\u041a\u043e\u043c\u043f\u044c\u044e\u0442\u0435\u0440\u044b", None))
        self.btn_tariff.setText(QCoreApplication.translate("MainWindow", u"\u0422\u0430\u0440\u0438\u0444\u044b", None))
    # retranslateUi


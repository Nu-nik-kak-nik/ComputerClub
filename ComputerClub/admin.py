from PySide6.QtWidgets import QMainWindow, QTableWidgetItem
from py_ui.ui_main_admin import Ui_MainWindow
from database_utils import LIST_BUTTON_TABLE, BUTTONS_TABLES, con
# import psycopg2


class Admin_window(QMainWindow):
    def __init__(self):
        super(Admin_window, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # Установка первой таблицы
        getattr(self.ui, LIST_BUTTON_TABLE[0]).setChecked(True)
        self.table_from_database(LIST_BUTTON_TABLE[0])

        # кнопки отвечающие за вывод таблиц из бд
        for btn in LIST_BUTTON_TABLE:
            getattr(self.ui, btn).clicked.connect(self.open_table)

        # выход
        self.ui.btn_logout.clicked.connect(self.logout)

    def table_from_database(self, sender_btn) -> None:
        connection = con()
        cursor = connection.cursor()
        # Извлечение названия таблицы
        table = BUTTONS_TABLES[str(sender_btn)]
        # Выполните SQL-запрос для получения данных из таблицы
        cursor.execute(f"SELECT * FROM {table}")
        data = cursor.fetchall()
        # Получение заголовков столбцов
        column_names = [desc[0] for desc in cursor.description]
        # Установка заголовков в QTableWidget
        self.ui.table_bd.setColumnCount(len(column_names))
        self.ui.table_bd.setHorizontalHeaderLabels(column_names)
        # Отобразите данные в таблице
        self.ui.table_bd.setRowCount(len(data))
        self.ui.table_bd.setColumnCount(len(data[0]))
        for i, row in enumerate(data):
            for j, value in enumerate(row):
                item = QTableWidgetItem(str(value))
                self.ui.table_bd.setItem(i, j, item)
        # Устанавливаем ширину таблицы равной ширине родительского виджета (QMainWindow)
        # Устанавливаем таблицу в центр основного виджета
        # self.setCentralWidget(self.ui.tableWidget)
        # Устанавливаем горизонтальные заголовки
        # self.ui.tableWidget.horizontalHeader().setCascadingSectionResizes(True)
        # self.ui.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        # self.ui.table_bd.resizeColumnsToContents()
        cursor.close()
        connection.close()
        self.ui.table_bd.sortItems(0)

    def open_table(self) -> None:
        sender_button = self.sender()
        for button in LIST_BUTTON_TABLE:
            btn = getattr(self.ui, button)
            if btn == sender_button:
                btn.setChecked(True)
                self.table_from_database(button)
            else:
                btn.setChecked(False)

    # не работает открытие старого окна!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    # def logout(self):
    #     self.close()
    #     self.window.show()

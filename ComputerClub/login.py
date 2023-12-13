import psycopg2 as psycopg2
from PySide6.QtWidgets import QMainWindow, QLineEdit
from py_ui.ui_login import Ui_MainWindow
from admin import Admin_window


class Log_in(QMainWindow):
    def __init__(self):
        super(Log_in, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # Создаем атрибут класса для нового окна
        self.new_window = None

        # Проверка подключения к БД
        # if not con_bul:
        #     self.ui.label_error.setText('Сбой подключения к базе данных')

        # видимость пароля
        self.ui.btn_visibility.clicked.connect(self.visibility_password)
        # при загрузке скрыть пароль
        self.ui.le_password.setEchoMode(QLineEdit.Password)

        # вход в базу
        self.ui.btn_login.clicked.connect(self.open_new_window)

    def visibility_password(self) -> None:
        if self.ui.btn_visibility.isChecked():
            self.ui.le_password.setEchoMode(QLineEdit.Normal)
        else:
            self.ui.le_password.setEchoMode(QLineEdit.Password)

    def open_new_window(self) -> None:
        login = self.ui.le_login.text()
        password = self.ui.le_password.text()
        if login and password:
            connection = self.con()
            if connection:
                cursor = connection.cursor()
                query = f"SELECT privileges FROM users WHERE login = '{login}' AND password = '{password}'"
                cursor.execute(query)
                user = cursor.fetchone()
                # Проверяем, есть ли пользователь с указанным логином и паролем
                if user:
                    if user[0]:
                        self.new_window = Admin_window()
                        self.new_window.show()
                        self.hide()
                    # else:
                    #     self.new_window = librarian_window()
                    #     self.new_window.show()
                    #     self.hide()
                    self.ui.le_login.setText('')
                    self.ui.l_info.setText('')
                else:
                    self.ui.l_info.setText('Неверный логин или пароль')
                self.ui.le_password.setText('')
                connection.close()
                cursor.close()
        # self.new_window = Admin_window()
        # self.new_window.show()
        # self.hide()

    def con(self):
        try:
            connection = psycopg2.connect(
                user="admin",
                password="admin!",
                host="localhost",
                port="5432",
                database="ComputerClub"
            )
            if not connection:
                self.ui.l_info.setText('Сбой подключения к базе данных')
                return None
        except psycopg2.OperationalError:
            self.ui.l_info.setText('Сбой подключения к базе данных')
            return None
        return connection

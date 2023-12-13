from PySide6.QtCore import Qt
from PySide6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QPushButton, QLabel, QStackedWidget, \
    QTableWidget


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # Создаем главный виджет и вертикальное размещение
        main_widget = QWidget()
        layout = QVBoxLayout(main_widget)

        # Создаем виджет стека и добавляем его в размещение
        self.stacked_widget = QStackedWidget()
        layout.addWidget(self.stacked_widget)

        # Создаем кнопки меню и добавляем их в размещение
        button_layout = QVBoxLayout()
        layout.addLayout(button_layout)

        button1 = QPushButton("Страница 1")
        button1.clicked.connect(self.show_page1)
        button_layout.addWidget(button1)

        button2 = QPushButton("Страница 2")
        button2.clicked.connect(self.show_page2)
        button_layout.addWidget(button2)

        button3 = QPushButton("Страница 3")
        button3.clicked.connect(self.show_page3)
        button_layout.addWidget(button3)

        # Создаем страницы содержимого и добавляем их в стек виджет
        page1 = QWidget()
        page1_layout = QVBoxLayout(page1)
        label1 = QLabel("Содержимое страницы 1")
        page1_layout.addWidget(label1)
        self.stacked_widget.addWidget(page1)

        page2 = QWidget()
        page2_layout = QVBoxLayout(page2)
        label2 = QLabel("Содержимое страницы 2")
        page2_layout.addWidget(label2)
        self.stacked_widget.addWidget(page2)

        page3 = QWidget()
        page3_layout = QVBoxLayout(page3)
        # label3 = QLabel("Содержимое страницы 3")
        table = QTableWidget()
        page3_layout.addWidget(table)
        self.stacked_widget.addWidget(page3)

        self.setCentralWidget(main_widget)

    def show_page1(self):
        self.stacked_widget.setCurrentIndex(0)

    def show_page2(self):
        self.stacked_widget.setCurrentIndex(1)

    def show_page3(self):
        self.stacked_widget.setCurrentIndex(2)


if __name__ == "__main__":
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec()

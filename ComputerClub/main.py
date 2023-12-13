from PySide6.QtWidgets import QApplication
from login import Log_in

if __name__ == "__main__":
    app = QApplication([])
    window = Log_in()
    window.show()
    app.exec()

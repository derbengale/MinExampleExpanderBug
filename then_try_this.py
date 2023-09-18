from PySide6.QtWidgets import QApplication, QWidget
from open_in_Designer_first_ui import Ui_Form
import sys
import os

class MainWindow(QWidget):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.ui = Ui_Form()
        self.ui.setupUi(self)

if __name__ == '__main__':
    app = QApplication(sys.argv)

    ui_file_path = os.path.join(os.path.dirname(__file__), 'open_in_Designer_first_ui.py')
    if not os.path.exists(ui_file_path):
        raise FileNotFoundError(f"UI file not found at {ui_file_path}")

    main_window = MainWindow()
    main_window.show()

    sys.exit(app.exec())

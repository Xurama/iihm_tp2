from PyQt5.QtWidgets import QTextEdit, QWidget, QApplication, QMainWindow


class FileDisplayWidget(QWidget):
    def __init__(self, filename):
        super().__init__()
        self.filename = filename
        self.textEdit = QTextEdit(self)
        self.textEdit.setReadOnly(True)

        with open(self.filename, 'r') as f:
            self.textEdit.setPlainText(f.read())

    def resizeEvent(self, event):
        self.textEdit.setGeometry(0, 0, self.width(), self.height())

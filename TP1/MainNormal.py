import sys

from PyQt5.QtWidgets import QApplication, QMainWindow
from NormalWidget import NormalWidget

file_name = "data/src_tp_bubble.csv"
def main():
    app = QApplication([])
    window = QMainWindow()
    window.resize(1024, 800)
    normalWidget = NormalWidget(file_name)
    window.setCentralWidget(normalWidget)
    window.show()
    app.exec_()

if __name__ == "__main__":
    if len(sys.argv) == 2:
        file_name = sys.argv[1]
    main()

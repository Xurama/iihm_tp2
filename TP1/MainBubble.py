import sys

from PyQt5.QtGui import QPainter
from PyQt5.QtWidgets import QApplication, QMainWindow
from BubbleWidget import BubbleWidget

file_name = "data/src_tp_bubble.csv"
def main():
    app = QApplication(sys.argv)
    main_window = QMainWindow()
    main_window.resize(1024, 800)
    bubble_widget = BubbleWidget(file_name)
    main_window.setCentralWidget(bubble_widget)
    main_window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    if len(sys.argv) == 2:
        file_name = sys.argv[1]
    main()

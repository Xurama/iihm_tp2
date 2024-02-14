from PyQt5.QtWidgets import QApplication, QMainWindow
from RopeWidget import RopeWidget

file_name = "data/src_tp_bubble.csv"
def main():
    app = QApplication([])
    window = QMainWindow()
    window.resize(1024, 800)
    bubble_widget = RopeWidget(file_name)
    window.setCentralWidget(bubble_widget)
    window.show()
    app.exec_()


if __name__ == "__main__":
    main()

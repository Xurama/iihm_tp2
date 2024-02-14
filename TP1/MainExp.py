from PyQt5.QtWidgets import QApplication, QMainWindow

from ExpSetup import ExpSetup

def main():
    app = QApplication([])
    window = QMainWindow()
    exp_widget = ExpSetup(window)
    window.setCentralWidget(exp_widget)
    window.show()
    app.exec_()


if __name__ == "__main__":
    main()

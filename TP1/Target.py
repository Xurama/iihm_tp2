from PyQt5.QtGui import QColor, QBrush, QPen


class Target:
    defaultCol = QColor("green")
    highlightCol = QColor("red")
    toSelectCol = QColor("blue")

    def __init__(self, x, y, size):
        self.x = x
        self.y = y
        self.size = size
        self.toSelect = False
        self.highlighted = False

    def paint(self, painter):
        color = self.defaultCol

        if self.toSelect:
            color = self.toSelectCol
        elif self.highlighted:
            color = self.highlightCol

        painter.setBrush(QBrush(color))
        painter.setPen(QPen(color))
        painter.drawEllipse(int(self.x - self.size / 2), int(self.y - self.size / 2), int(self.size), int(self.size))

    def click_cible(self):
        if self.toSelect:
            self.toSelect = False
            return True
        return False


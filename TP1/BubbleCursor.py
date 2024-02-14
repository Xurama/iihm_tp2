from PyQt5.QtGui import QColor

class BubbleCursor:
    defaultCol=QColor("blue")

    def __init__(self, targets):
        self.x = 0
        self.y = 0
        self.size = 50
        self.targets = targets
        self.closest = None
    def paint(self, painter):
        painter.setBrush(self.defaultCol)
        painter.drawEllipse(int(self.x - self.size), int(self.y - self.size), int(self.size * 2), int(self.size * 2))

    def move(self, x, y):
        self.x = x
        self.y = y
        min_distance = float("inf")
        previous_closest = self.closest

        for target in self.targets:
            distance = ((self.x - target.x) ** 2 + (self.y - target.y) ** 2) ** 0.5  # cf. Theoreme de Pythagore
            distance = distance - target.size/2  # Prendre la distance avec le contour du cercle et pas le centre
            if distance < min_distance:
                min_distance = distance
                self.closest = target
            self.size = min_distance

        if previous_closest != self.closest:
            if previous_closest:
                previous_closest.highlighted = False
            self.closest.highlighted = True
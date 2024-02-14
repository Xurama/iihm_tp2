from BubbleCursor import BubbleCursor

class RopeCursor(BubbleCursor):
    def paint(self, painter):
        if self.closest is not None:
            painter.setBrush(self.defaultCol)
            painter.drawLine(self.x, self.y, self.closest.x, self.closest.y)

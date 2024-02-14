from PyQt5.QtGui import QColor

class NormalCursor:
    defaultCol=QColor("blue")

    def __init__(self, targets):
        self.x = 0
        self.y = 0
        self.targets = targets
        self.closest = None
    def move(self, x, y):
        self.x = x
        self.y = y
        closest_target = None
        min_distance = float('inf')

        for target in self.targets:
            distance = ((self.x - target.x) ** 2 + (self.y - target.y) ** 2) ** 0.5
            if distance < min_distance:
                min_distance = distance
                closest_target = target

        if closest_target and min_distance < closest_target.size / 2:
            closest_target.highlighted = True
        else:
            if self.closest and self.closest != closest_target:
                self.closest.highlighted = False

        self.closest = closest_target
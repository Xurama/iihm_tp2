import csv
import random

import time
from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtWidgets import QWidget

from BubbleCursor import BubbleCursor
from Target import Target


class BubbleWidget(QWidget):
    def __init__(self, file_name, exp_setup, number_of_targets, technique_name):
        super().__init__()
        self.exp_setup = exp_setup
        self.targets = []
        self.setMouseTracking(True)
        self.start_time = None
        self.errors = 0
        self.technique_name = technique_name

        # Chargement du fichier csv
        with open(file_name) as csvfile:
            reader = csv.reader(csvfile)
            for row in reader:
                x = int(row[0])
                y = int(row[1])
                size = int(row[2])
                target = Target(x, y, size)
                self.targets.append(target)

        self.target_to_select = self.targets[:number_of_targets]
        self.cursor = BubbleCursor(self.targets)
        self.selectRandomTarget()

    def paintEvent(self, event):
        painter = QPainter(self)
        self.cursor.paint(painter)
        for target in self.targets:
            target.paint(painter)
        painter.setPen(QColor("black"))
        status_text = f"Technique: {self.technique_name}, Cible: {self.target_number}/15, Configuration: {self.config_number}/9, Répétition: {self.repeat_number}/{self.total_repeats}"
        painter.drawText(10, 20, status_text)

    def mouseMoveEvent(self, event):
        self.cursor.move(event.x(), event.y())
        self.update()

    def selectRandomTarget(self):
        if self.start_time == None:
            self.start_time = time.time()
        target = self.target_to_select.pop()
        target.toSelect = True
        self.update()

    def printLog(self):
        current_time = (time.time() - self.start_time)*1000
        self.exp_setup.add_line_to_response(current_time, self.errors)
        self.errors = 0
        self.start_time = None

    def set_status(self, target_number, config_number, repeat_number, total_repeats):
        self.target_number = target_number
        self.config_number = config_number
        self.repeat_number = repeat_number
        self.total_repeats = total_repeats

    def mousePressEvent(self, event):
        if self.cursor.closest is not None:
            if self.cursor.closest.click_cible():
                self.errors = 0
                self.target_number += 1
                self.printLog()
                if len(self.target_to_select) > 0:
                    self.selectRandomTarget()
                else:
                    self.exp_setup.next_experience()
            else:
                self.errors += 1
        self.set_status(self.target_number, self.config_number, self.repeat_number,
                        self.total_repeats)
        self.update()

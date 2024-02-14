from enum import Enum

from BubbleWidget import BubbleWidget
from RopeWidget import RopeWidget
from NormalWidget import NormalWidget

class Experience(Enum):
    BUBBLE = 1
    ROPE = 2
    NORMAL = 3

    def create_widget(self, file_path, exp_setup, number_of_targets, technique_name):
        if self.value == Experience.BUBBLE.value:
            widget = BubbleWidget(file_path, exp_setup, number_of_targets, technique_name)
        elif self.value == Experience.ROPE.value:
            widget = RopeWidget(file_path, exp_setup, number_of_targets, technique_name)
        elif self.value == Experience.NORMAL.value:
            widget = NormalWidget(file_path, exp_setup, number_of_targets, technique_name)
        else:
            print('Aucune expérience selectionnée')
            widget = None
        return widget
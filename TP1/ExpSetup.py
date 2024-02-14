import os
import sys

from PyQt5.QtGui import QIntValidator
from PyQt5.QtWidgets import QDialog, QLabel, QLineEdit, QComboBox, QGridLayout, QPushButton, QHBoxLayout, QVBoxLayout

from Experience import Experience
from FileDisplayWidget import FileDisplayWidget

DIR_PATH = "generated_exp/"
TARGETS_PER_EXPERIENCE = 15

class ExpSetup(QDialog):
    def __init__(self, window):
        super().__init__()

        self.file_name = 'data/response.csv'
        self.current_ordonnance = None
        self.ordonnance = None
        self.window = window

        self.user_number = None
        self.technique = None
        self.repeats = None

        self.current_repeat_series = 0
        self.current_target_number = 1

        user_label = QLabel("Numéro d'utilisateur :")
        self.user_edit = QLineEdit()
        self.user_edit.setValidator(QIntValidator())

        tech_label = QLabel("Technique :")
        self.tech_combo = QComboBox()
        self.tech_combo.addItems(["Bubble", "Rope", "Normal"])
        repeats_label = QLabel("Nombre de répétitions :")
        self.repeats_edit = QLineEdit()
        self.repeats_edit.setValidator(QIntValidator())

        layout = QGridLayout()
        layout.addWidget(user_label, 0, 0)
        layout.addWidget(self.user_edit, 0, 1)
        layout.addWidget(tech_label, 1, 0)
        layout.addWidget(self.tech_combo, 1, 1)
        layout.addWidget(repeats_label, 4, 0)
        layout.addWidget(self.repeats_edit, 4, 1)

        self.validate_button = QPushButton("Valider")
        self.validate_button.clicked.connect(self.verify_entry)

        h_layout = QHBoxLayout()
        h_layout.addStretch()
        h_layout.addWidget(self.validate_button)
        h_layout.addStretch()
        v_layout = QVBoxLayout()
        v_layout.addLayout(layout)
        v_layout.addLayout(h_layout)

        self.setLayout(v_layout)

    def verify_entry(self):
        self.user_number = self.user_edit.text()
        self.technique = self.tech_combo.currentIndex()
        self.repeats = int(self.repeats_edit.text())
        if self.repeats <= 1:
            print('Répétition doit être strictement supérieur à 1')
        else:
            self.init_ordonnance()
            self.next_experience()

    def create_experience(self, experience, density, target_size, technique_name):
        if experience not in Experience:
            print('Aucune expérience selectionné')
            return None

        density = str(density)
        target_size = str(target_size)
        file_name = "src_d_" + density + "_s_" + target_size + ".csv"

        file_path = DIR_PATH + file_name
        return experience.create_widget(file_path, self, TARGETS_PER_EXPERIENCE, technique_name)

    def start_experience(self, widget):
        if widget is not None:
            self.window.resize(1024, 800)
            self.window.setCentralWidget(widget)
            self.window.show()

    def init_ordonnance(self):
        self.ordonnance = []
        self.current_ordonnance = -1
        experience_list = [Experience.BUBBLE, Experience.ROPE, Experience.NORMAL]
        experience_ordered = experience_list[self.technique:] + experience_list[:self.technique]
        density_list = [30, 60, 90]
        size_list = [9, 12, 18]

        for _ in range(self.repeats):
            for experience in experience_ordered:
                for density in density_list:
                    for size in size_list:
                        widget = self.create_experience(experience, density, size, experience.name)
                        self.ordonnance.append((widget, experience, density, size))

    def next_experience(self):
        self.current_target_number = 1
        self.current_ordonnance += 1

        total_experiences_per_repeat = len(Experience) * len([30, 60, 90]) * len([9, 12, 18])

        if self.current_ordonnance >= len(self.ordonnance):
            self.display_data()
            return

        if self.current_ordonnance % total_experiences_per_repeat == 0 and self.current_ordonnance != 0:
            self.current_repeat_series += 1

        self.current_configuration_number = (self.current_ordonnance % 9) + 1
        self.current_repeat_number = (self.current_ordonnance // total_experiences_per_repeat) + 1

        widget, experience, density, size = self.ordonnance[self.current_ordonnance]
        widget.set_status(self.current_repeat_series, self.current_configuration_number, self.current_repeat_number,
                          self.repeats)
        self.start_experience(widget)

    def add_line_to_response(self, time, error):
        line = f"{self.user_number}, {self.current_repeat_series}, {self.current_target_number}, {self.ordonnance[self.current_ordonnance][2]}, {self.ordonnance[self.current_ordonnance][3]}, {self.ordonnance[self.current_ordonnance][1].name}, {time}, {error}"
        with open(self.file_name, "a") as file:
            file.write(line + '\n')
        self.current_target_number += 1

    def display_data(self):
        widget = FileDisplayWidget(self.file_name)
        self.start_experience(widget)

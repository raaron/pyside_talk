from PySide.QtGui import *


class View(QWidget):
    """Main view of the app."""

    def __init__(self, person, parent=None):
        super(View, self).__init__(parent)
        self.person = person
        self.layout = QGridLayout(self)
        self.grid = QGridLayout()
        self.layout.addLayout(self.grid, 1, 1)
        self.lb_name = QLabel(self.person.name)
        self.lb_age = QLabel(str(self.person.age))
        self.lb_weight = QLabel(str(self.person.weight))
        self.pb_eat = QPushButton("Eat")
        self.grid.addWidget(QLabel("Name:"), 0, 0)
        self.grid.addWidget(self.lb_name, 0, 1)
        self.grid.addWidget(QLabel("Age:"), 1, 0)
        self.grid.addWidget(self.lb_age, 1, 1)
        self.grid.addWidget(QLabel("Weight:"), 2, 0)
        self.grid.addWidget(self.lb_weight, 2, 1)
        self.grid.addWidget(self.pb_eat, 3, 0)

    def update_label_weight(self):
        """Update the label for the weight to the current value."""
        self.lb_weight.setText(str(self.person.weight))

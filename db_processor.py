import generator
import library
from PyQt5.QtWidgets import (QWidget, QScrollArea, QVBoxLayout)


class Insert:
    def insert(self, area: QScrollArea):
        self.db = library.Library()
        self.g = generator.Generator()
        self.widget = QWidget()
        self.vbox = QVBoxLayout()
        data = self.db.show()

        for record in data:
            badge = self.g.g_badge(record)
            self.vbox.addWidget(badge)

        self.widget.setLayout(self.vbox)
        area.setWidgetResizable(True)
        area.setWidget(self.widget)


import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from decimal import Decimal
from datetime import datetime
import connect       as conn
import config_loader as cl
import logwriter     as lw
import ui_entry      as ue
import data          as data


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self, parent = None):
        super().__init__(parent)
        self.log = lw.logwriter()
        self.config = cl.config_loader(self.log.write).val
        self.log.construct(".log", self.config.win_title, "1.1.1", None, 3)
        self.dh = conn.data_handler(self.config, self.log.write)
        self.init_gui()

    def init_gui(self):
        self.window = QtWidgets.QWidget()
        self.window.resize(int(self.config.win_width), int(self.config.win_height))
        self.setFixedWidth(int(self.config.win_width))
        self.setFixedHeight(int(self.config.win_height))
        self.layout = QtWidgets.QHBoxLayout()
        self.setCentralWidget(self.window)
        self.window.setLayout(self.layout)
        self.title = QtWidgets.QLabel(self.window)
        self.title.setGeometry(QtCore.QRect(10, 10, 400, 40))
        self.title.setText(self.config.win_title)
        font = QtGui.QFont('Cursive', 25)
        self.title.setFont(font)

        self.widgets = []
        variable_inputs = self.dh.pull(0, 0, True)
        for item in variable_inputs:
            td = data.title_data()
            td.title = item[2]
            td.budgeted = item[1]
            td.variable_input_id = item[0]
            widget = ue.variable_input_widget(0, 60, self.dh, td, self.config)
            self.layout.addWidget(widget)
            self.widgets.append(widget)

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    win = MainWindow()
    win.show()

    sys.exit(app.exec_())

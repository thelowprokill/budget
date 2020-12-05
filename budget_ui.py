import sys
from PyQt5 import QtCore, QtGui, QtWidgets, Qt
from decimal import Decimal
from datetime import datetime
import connect       as conn
import config_loader as cl
import logwriter     as lw
import ui_entry      as ue
import data          as data
import config_ui     as c_ui

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self, parent = None):
        super().__init__(parent)
        self.log = lw.logwriter()
        self.config_loader = cl.config_loader(self.log.write)
        self.connect()
        self.log.construct(".log", self.config.win_title, "1.1.1", None, 3)
        self.init_gui()

    def config_window(self):
        try:
            if self.config == None:
                self.config = cl.config_storage()
        except:
            self.config = cl.config_storage()
        self.conf_win = c_ui.config_window(self.log.write, self.config, self.update_config)
        self.conf_win.show()

    def update_config(self, val, default = False):
        if not default:
            self.config_loader.write(val)
        else:
            self.config_loader.write(self.config_loader.defaults)

        try:
            self.setFixedWidth(int(self.config.win_width))
            self.setFixedHeight(int(self.config.win_height))
            self.ui_text()
        except:
            pass
        self.refresh()

    def refresh(self):
        self.connect()
        self.add_widgets()

    def connect(self):
        if not self.config_loader.read():
            self.config_window()
        self.config = self.config_loader.val
        self.dh = conn.data_handler(self.config, self.log.write)

    def add_widgets(self):
        for w in reversed(range(self.body_layout.count())):
            self.body_layout.itemAt(w).widget().deleteLater()

        self.widgets = []
        variable_inputs = self.dh.pull(2020, 12, 0, True)
        for item in variable_inputs:
            td = data.title_data()
            td.title = item[2]
            td.budgeted = item[1]
            td.variable_input_id = item[0]
            td.year = self.year_box.currentIndex() + 2020
            td.month = self.month_box.currentIndex() + 1
            widget = ue.variable_input_widget(0, 60, self.dh, td, self.config)
            self.body_layout.addWidget(widget)
            self.widgets.append(widget)

    def ui_text(self):
        self.title.setText(self.config.win_title)
        self.accept_date_button.setText("Submit")
        self.config_button.setText("Config")

    def init_gui(self):

        ##########################################
        ### Window                             ###
        ##########################################

        self.window = QtWidgets.QWidget()
        self.window.resize(int(self.config.win_width), int(self.config.win_height))
        self.setFixedWidth(int(self.config.win_width))
        self.setFixedHeight(int(self.config.win_height))
        self.layout = QtWidgets.QVBoxLayout()
        self.setCentralWidget(self.window)
        self.window.setLayout(self.layout)

        ##########################################
        ### /Window                            ###
        ##########################################

        ##########################################
        ### Header                             ###
        ##########################################

        self.header_layout = QtWidgets.QHBoxLayout()

        # Spacer
        self.spacer = QtWidgets.QSpacerItem(150, 10, QtWidgets.QSizePolicy.Expanding)
        self.header_layout.addSpacerItem(self.spacer)

        # Title
        self.title = QtWidgets.QLabel()
        self.title.setGeometry(QtCore.QRect(10, 10, 400, 40))
        self.title.setAlignment(Qt.Qt.AlignCenter)
        font = QtGui.QFont('Cursive', 50)
        self.title.setFont(font)

        self.header_layout.addWidget(self.title)

        # Spacer
        self.spacer2 = QtWidgets.QSpacerItem(150, 10, QtWidgets.QSizePolicy.Expanding)
        self.header_layout.addSpacerItem(self.spacer2)

        # Date
        self.date_layout = QtWidgets.QVBoxLayout()
        self.year_box = QtWidgets.QComboBox()
        self.year_box.addItem("2020")
        self.year_box.addItem("2021")
        self.date_layout.addWidget(self.year_box)

        self.month_box = QtWidgets.QComboBox()
        self.month_box.addItem("Jan")
        self.month_box.addItem("Feb")
        self.month_box.addItem("Mar")
        self.month_box.addItem("Apr")
        self.month_box.addItem("May")
        self.month_box.addItem("Jun")
        self.month_box.addItem("Jul")
        self.month_box.addItem("Aug")
        self.month_box.addItem("Sep")
        self.month_box.addItem("Oct")
        self.month_box.addItem("Nov")
        self.month_box.addItem("Dec")
        self.date_layout.addWidget(self.month_box)

        now = datetime.now()
        self.year_box.setCurrentIndex(now.year - 2020)
        self.month_box.setCurrentIndex(now.month - 1)

        self.accept_date_button = QtWidgets.QPushButton()
        self.date_layout.addWidget(self.accept_date_button)

        # Config
        self.config_button = QtWidgets.QPushButton()

        self.date_layout.addWidget(self.config_button)

        self.header_layout.addLayout(self.date_layout)
        self.layout.addLayout(self.header_layout)


        ##########################################
        ### /Header                            ###
        ##########################################

        ##########################################
        ### Buttons                            ###
        ##########################################

        self.config_button.clicked.connect(self.config_window)
        self.accept_date_button.clicked.connect(self.refresh)

        ##########################################
        ### /Buttons                           ###
        ##########################################

        ##########################################
        ### Body                               ###
        ##########################################

        self.body_layout = QtWidgets.QHBoxLayout()
        self.widgets = []
        variable_inputs = self.dh.pull(2020, 12, 0, True)
        for item in variable_inputs:
            td = data.title_data()
            td.title = item[2]
            td.budgeted = item[1]
            td.variable_input_id = item[0]
            td.year = self.year_box.currentIndex() + 2020
            td.month = self.month_box.currentIndex() + 1
            widget = ue.variable_input_widget(0, 60, self.dh, td, self.config)
            self.body_layout.addWidget(widget)
            self.widgets.append(widget)

        self.layout.addLayout(self.body_layout)

        ##########################################
        ### /Body                              ###
        ##########################################

        self.ui_text()

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    win = MainWindow()
    win.show()

    sys.exit(app.exec_())

import sys
from PyQt5 import QtCore, QtGui, QtWidgets

window_width = 800
window_height = 500
widget_width = 150
widget_height = 400
class variable_input_widget(QtWidgets.QWidget):
    def __init__(self, x, y, *args, **kwargs):
        self.x = x
        self.y = y
        super().__init__(*args, **kwargs)
        self.setupUi()

    def setupUi(self):
        self.setObjectName("self")
        self.resize(widget_width, widget_height)
        self.verticalLayoutWidget = QtWidgets.QWidget(self)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(self.x, self.y, widget_width, widget_height))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_variable_input_type = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_variable_input_type.setObjectName("label_variable_input_type")
        self.verticalLayout.addWidget(self.label_variable_input_type)
        self.label_budgeted_amount = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_budgeted_amount.setObjectName("label_budgeted_amount")
        self.verticalLayout.addWidget(self.label_budgeted_amount)
        self.label_total_spent = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_total_spent.setObjectName("label_total_spent")
        self.verticalLayout.addWidget(self.label_total_spent)
        self.label_remaining_balance = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_remaining_balance.setObjectName("label_remaining_balance")
        self.verticalLayout.addWidget(self.label_remaining_balance)
        self.list_widget = QtWidgets.QListWidget(self.verticalLayoutWidget)
        self.list_widget.setObjectName("list_widget")
        self.verticalLayout.addWidget(self.list_widget)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.button_view = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.button_view.setObjectName("button_view")
        self.horizontalLayout.addWidget(self.button_view)
        self.button_add = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.button_add.setObjectName("button_add")
        self.horizontalLayout.addWidget(self.button_add)
        self.verticalLayout.addLayout(self.horizontalLayout)

        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)

    def add_text(self, s):
        item = self.list_widget.insertItem(0, s)

    def retranslateUi(self):
        self.setWindowTitle("Variable Input Type")
        self.label_variable_input_type.setText("variable_input_type")
        self.label_budgeted_amount.setText("budgeted")
        self.label_total_spent.setText("spent")
        self.label_remaining_balance.setText("remaining")
        self.button_view.setText("View")
        self.button_add.setText("Add")

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self, parent = None):
        super().__init__(parent)
        self.init_gui()

    def init_gui(self):
        self.window = QtWidgets.QWidget()
        self.window.resize(window_width, window_height)
        self.setFixedWidth(window_width)
        self.setFixedHeight(window_height)
        self.layout = QtWidgets.QHBoxLayout()
        self.setCentralWidget(self.window)
        self.window.setLayout(self.layout)

        self.widgets = []
        for i in range(5):
            widget = variable_input_widget(0, 0)
            self.layout.addWidget(widget)
            self.widgets.append(widget)

        text = ["Rent", "Groceries", "Car", "Misc", "House"]
        for (widget, t) in zip(self.widgets, text):
            widget.add_text(t)

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    win = MainWindow()
    win.show()

    sys.exit(app.exec_())

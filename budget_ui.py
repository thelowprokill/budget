import sys
from PyQt5 import QtCore, QtGui, QtWidgets

window_width = 1600
window_height = 600
widget_width = 300
widget_height = 500
class variable_input_widget(QtWidgets.QWidget):
    def __init__(self, x, y, *args, **kwargs):
        self.variable_input_type = "Rent"
        self.pull_data()
        self.x = x
        self.y = y
        super().__init__(*args, **kwargs)
        self.setupUi()

    def pull_data(self):
        self.amount_spent = 0
        self.amount_budgeted = 950

    def setupUi(self):
        self.setObjectName("self")
        self.setStyleSheet('self { border: 1px solid black; }')

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


        font = QtGui.QFont()
        font.setPointSize(10)
        self.list_layout = QtWidgets.QHBoxLayout()
        self.list_layout.setObjectName("list_layout")
        self.list_layout.setContentsMargins(0,0,0,0)
        self.list_layout.setSpacing(0)
        self.comment_list_widget = QtWidgets.QListWidget(self.verticalLayoutWidget)
        self.comment_list_widget.setObjectName("comment_list_widget")
        self.comment_list_widget.setFont(font)
        self.list_layout.addWidget(self.comment_list_widget)
        self.date_list_widget = QtWidgets.QListWidget(self.verticalLayoutWidget)
        self.date_list_widget.setObjectName("date_list_widget")
        self.date_list_widget.setFont(font)
        self.list_layout.addWidget(self.date_list_widget)
        self.amount_list_widget = QtWidgets.QListWidget(self.verticalLayoutWidget)
        self.amount_list_widget.setObjectName("amount_list_widget")
        self.amount_list_widget.setFont(font)
        self.list_layout.addWidget(self.amount_list_widget)
        self.verticalLayout.addLayout(self.list_layout)


        self.button_layout = QtWidgets.QHBoxLayout()
        self.button_layout.setObjectName("button_layout")
        self.button_view = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.button_view.setObjectName("button_view")
        self.button_layout.addWidget(self.button_view)
        self.button_add = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.button_add.setObjectName("button_add")
        self.button_layout.addWidget(self.button_add)
        self.verticalLayout.addLayout(self.button_layout)

        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)

    def add_text(self, c, d, a):
        item = self.comment_list_widget.insertItem(0, c)
        item = self.date_list_widget.insertItem(0, d)
        item = self.amount_list_widget.insertItem(0, "${:.2f}".format(a))
        self.amount_spent = self.amount_spent + a
        self.retranslateUi()

    def retranslateUi(self):
        self.label_variable_input_type.setText(self.variable_input_type)
        self.label_budgeted_amount.setText("Budgeted: {:.2f}".format(self.amount_budgeted))
        self.label_total_spent.setText("Spent: {:.2f}".format(self.amount_spent))
        self.label_remaining_balance.setText("Remaining: {:.2f}".format(self.amount_budgeted - self.amount_spent))
        self.button_view.setText("View")
        self.button_add.setText("Add")

    def add_entry(self):
        pass

    def view(self):
        pass

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
        self.title = QtWidgets.QLabel(self.window)
        self.title.setGeometry(QtCore.QRect(10, 10, 400, 40))
        self.title.setText("Hull Family Budget")
        font = QtGui.QFont('Cursive', 25)
        self.title.setFont(font)

        self.widgets = []
        for i in range(5):
            widget = variable_input_widget(0, 60)
            self.layout.addWidget(widget)
            self.widgets.append(widget)

        text = ["Rent", "Groceries", "Car", "Misc", "House"]
        date = ["2020-11-25", "2020-11-15", "2020-11-13", "2020-11-15", "2020-11-25"]
        amount = [950, 223.56, 14.34, 438.99, 11.21]
        budget = [950, 200, 50, 100, 200]
        for (widget, t, d, a, b) in zip(self.widgets, text, date, amount, budget):
            widget.variable_input_type = t
            widget.amount_budgeted = b
            widget.add_text(t, d, a)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    win = MainWindow()
    win.show()

    sys.exit(app.exec_())

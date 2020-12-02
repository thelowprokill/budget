from PyQt5 import QtCore, QtGui, QtWidgets
from decimal import Decimal
from datetime import datetime
import data          as data

class variable_input_widget(QtWidgets.QWidget):
    def __init__(self, x, y, dh, td, config, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.dh = dh
        self.td = td
        self.td.remaining = self.td.budgeted - self.td.spent
        self.config = config
        self.x = x
        self.y = y
        self.cue = []
        self.setupUi()
        self.pull_data()

    def pull_data(self):
        results = self.dh.pull(self.td.month, self.td.variable_input_id, False)
        for item in results:
            self.add_text(item[3], item[4], item[5])

    def setupUi(self):
        self.setObjectName("self")
        self.setStyleSheet('self { border: 1px solid black; }')

        ##########################################
        ### Main Widgets                       ###
        ##########################################

        self.resize(int(self.config.cell_width), int(self.config.cell_height))
        self.verticalLayoutWidget = QtWidgets.QWidget(self)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(self.x, self.y, int(self.config.cell_width), int(self.config.cell_height)))
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

        ##########################################
        ### /Main Widgets                      ###
        ##########################################

        ##########################################
        ### List Widget                        ###
        ##########################################

        font = QtGui.QFont()
        font.setPointSize(10)
        self.list_layout = QtWidgets.QHBoxLayout()
        self.list_layout.setObjectName("list_layout")
        self.list_layout.setContentsMargins(0,0,0,0)
        self.list_layout.setSpacing(0)

        ################################
        ### Comments                 ###
        ################################

        self.v_layout_comments = QtWidgets.QVBoxLayout()
        self.v_layout_comments.setObjectName("v_layout_comments")
        self.v_layout_comments.setContentsMargins(0,0,0,0)
        self.v_layout_comments.setSpacing(0)
        self.comment_list_widget = QtWidgets.QListWidget(self.verticalLayoutWidget)
        self.comment_list_widget.setObjectName("comment_list_widget")
        self.comment_list_widget.setFont(font)
        self.comment_text = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.v_layout_comments.addWidget(self.comment_text)
        self.v_layout_comments.addWidget(self.comment_list_widget)
        self.v_box_comments = QtWidgets.QWidget(self)
        self.v_box_comments.setLayout(self.v_layout_comments)
        self.list_layout.addWidget(self.v_box_comments)

        ################################
        ### /Comments                ###
        ################################

        ################################
        ### Date                     ###
        ################################

        self.v_layout_date = QtWidgets.QVBoxLayout()
        self.v_layout_date.setObjectName("v_layout_date")
        self.v_layout_date.setContentsMargins(0,0,0,0)
        self.v_layout_date.setSpacing(0)
        self.date_list_widget = QtWidgets.QListWidget(self.verticalLayoutWidget)
        self.date_list_widget.setObjectName("date_list_widget")
        self.date_list_widget.setFont(font)
        self.date_text = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.v_layout_date.addWidget(self.date_text)
        self.v_layout_date.addWidget(self.date_list_widget)
        self.v_box_date = QtWidgets.QWidget(self)
        self.v_box_date.setLayout(self.v_layout_date)
        self.list_layout.addWidget(self.v_box_date)

        ################################
        ### /Date                    ###
        ################################

        ################################
        ### Value                    ###
        ################################

        self.v_layout_amount = QtWidgets.QVBoxLayout()
        self.v_layout_amount.setObjectName("v_layout_amount")
        self.v_layout_amount.setContentsMargins(0,0,0,0)
        self.v_layout_amount.setSpacing(0)
        self.amount_list_widget = QtWidgets.QListWidget(self.verticalLayoutWidget)
        self.amount_list_widget.setObjectName("amount_list_widget")
        self.amount_list_widget.setFont(font)
        self.amount_text = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.v_layout_amount.addWidget(self.amount_text)
        self.v_layout_amount.addWidget(self.amount_list_widget)
        self.v_box_amount = QtWidgets.QWidget(self)
        self.v_box_amount.setLayout(self.v_layout_amount)
        self.list_layout.addWidget(self.v_box_amount)

        ################################
        ### /Value                   ###
        ################################

        self.verticalLayout.addLayout(self.list_layout)

        ##########################################
        ### /List Widget                       ###
        ##########################################

        ##########################################
        ### Text Fields                        ###
        ##########################################

        self.add_v_layout = QtWidgets.QVBoxLayout()
        self.add_v_layout.setObjectName("add_v_layout")
        self.add_v_layout.setContentsMargins(0,0,0,0)
        self.add_v_layout.setSpacing(0)

        self.comment_text_add = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.date_text_add = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.amount_text_add = QtWidgets.QLineEdit(self.verticalLayoutWidget)

        self.date_text_add.setText(datetime.now().date().strftime("%Y %b %d"))
        self.add_h_layout = QtWidgets.QHBoxLayout()
        self.add_h_layout.setObjectName("v_layout_amount")
        self.add_h_layout.setContentsMargins(0,0,0,0)
        self.add_h_layout.setSpacing(0)

        self.add_h_layout.addWidget(self.comment_text_add)
        self.add_h_layout.addWidget(self.date_text_add)
        self.add_h_layout.addWidget(self.amount_text_add)

        self.add_h_box = QtWidgets.QWidget(self)
        self.add_h_box.setLayout(self.add_h_layout)

        self.add_entry_text = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.add_v_layout.addWidget(self.add_entry_text)
        self.add_v_layout.addWidget(self.add_h_box)

        self.verticalLayout.addLayout(self.add_v_layout)

        ##########################################
        ### /Text Fields                       ###
        ##########################################

        ##########################################
        ### Buttons                            ###
        ##########################################

        self.button_layout = QtWidgets.QHBoxLayout()
        self.button_layout.setObjectName("button_layout")
        self.button_commit = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.button_commit.setObjectName("button_commit")
        self.button_layout.addWidget(self.button_commit)
        self.button_add = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.button_add.setObjectName("button_add")
        self.button_layout.addWidget(self.button_add)
        self.verticalLayout.addLayout(self.button_layout)

        self.button_add.clicked.connect(self.add_entry)
        self.button_commit.clicked.connect(self.commit)

        ##########################################
        ### /Buttons                           ###
        ##########################################

        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self):
        ##########################################
        ### Static Text                        ###
        ##########################################

        self.comment_text.setText("Comment")
        self.date_text.setText("Date")
        self.amount_text.setText("Amount")
        self.button_commit.setText("Commit")
        self.button_add.setText("Add")
        self.add_entry_text.setText("New Entry")

        ##########################################
        ### /Static Text                       ###
        ##########################################

        ##########################################
        ### Dynamic Text                       ###
        ##########################################

        self.label_variable_input_type.setText(self.td.title) #self.variable_input_type)
        self.label_budgeted_amount.setText("Budgeted: {}".format(self.td.budgeted))
        self.label_total_spent.setText("Spent: {}".format(self.td.spent))
        self.label_remaining_balance.setText("Remaining: {}".format(self.td.remaining))

        ##########################################
        ### /Dynamic Text                      ###
        ##########################################

    def keyPressEvent(self, event):
        if event.key() == QtCore.Qt.Key_Return:
            self.add_entry()

    def add_text(self, c, d, a):
        item = self.comment_list_widget.insertItem(0, c)
        item = self.date_list_widget.insertItem(0, d.strftime('%Y %b %d'))
        item = self.amount_list_widget.insertItem(0, "${}".format(a))
        self.td.spent = self.td.spent + a
        self.td.remaining = self.td.budgeted - self.td.spent
        self.retranslateUi()

    def add_entry(self):
        e = data.entry()
        e.c = self.comment_text_add.text()
        e.d = datetime.strptime(self.date_text_add.text(), '%Y %b %d')
        e.a = Decimal(self.amount_text_add.text())
        self.comment_text_add.setText("")
        self.amount_text_add.setText("")
        self.add_text(e.c, e.d, e.a)
        self.cue.append(e)
        self.comment_text_add.setFocus()

    def commit(self):
        for e in self.cue:
            self.dh.push(self.td.month, self.td.variable_input_id, e.c, e.d, e.a)


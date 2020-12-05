from PyQt5 import QtCore, QtGui, QtWidgets
import sys
import config_loader as cl
import logwriter as lw

class config_window(QtWidgets.QMainWindow):
    def __init__(self, message, config, callback):
        super().__init__(None)
        self.message = message
        self.config = config
        self.callback = callback
        self.init_gui()

    def init_gui(self):
        self.window = QtWidgets.QWidget()
        self.window.resize(400, 550)
        self.window.setFixedWidth(400)
        self.window.setFixedHeight(550)
        self.setCentralWidget(self.window)

        self.main_layout = QtWidgets.QVBoxLayout()

        self.window.setLayout(self.main_layout)

        ##########################################
        ### sql_host                           ###
        ##########################################

        self.sql_host_text = QtWidgets.QLabel()
        self.sql_host_line_edit = QtWidgets.QLineEdit()

        self.h_layout_sql_host = QtWidgets.QHBoxLayout()
        self.h_layout_sql_host.addWidget(self.sql_host_text)
        self.h_layout_sql_host.addWidget(self.sql_host_line_edit)

        self.h_box_sql_host = QtWidgets.QWidget(self)
        self.h_box_sql_host.setLayout(self.h_layout_sql_host)

        self.main_layout.addWidget(self.h_box_sql_host)

        ##########################################
        ### /sql_host                          ###
        ##########################################

        ##########################################
        ### sql_port                           ###
        ##########################################

        self.sql_port_text = QtWidgets.QLabel()
        self.sql_port_line_edit = QtWidgets.QLineEdit()

        self.h_layout_sql_port = QtWidgets.QHBoxLayout()
        self.h_layout_sql_port.addWidget(self.sql_port_text)
        self.h_layout_sql_port.addWidget(self.sql_port_line_edit)

        self.h_box_sql_port = QtWidgets.QWidget(self)
        self.h_box_sql_port.setLayout(self.h_layout_sql_port)

        self.main_layout.addWidget(self.h_box_sql_port)

        ##########################################
        ### /sql_port                          ###
        ##########################################

        ##########################################
        ### sql_user                           ###
        ##########################################

        self.sql_user_text = QtWidgets.QLabel()
        self.sql_user_line_edit = QtWidgets.QLineEdit()

        self.h_layout_sql_user = QtWidgets.QHBoxLayout()
        self.h_layout_sql_user.addWidget(self.sql_user_text)
        self.h_layout_sql_user.addWidget(self.sql_user_line_edit)

        self.h_box_sql_user = QtWidgets.QWidget(self)
        self.h_box_sql_user.setLayout(self.h_layout_sql_user)

        self.main_layout.addWidget(self.h_box_sql_user)

        ##########################################
        ### /sql_user                          ###
        ##########################################

        ##########################################
        ### sql_pass                           ###
        ##########################################

        self.sql_pass_text = QtWidgets.QLabel()
        self.sql_pass_line_edit = QtWidgets.QLineEdit()
        self.sql_pass_line_edit.setEchoMode(QtWidgets.QLineEdit.Password)

        self.h_layout_sql_pass = QtWidgets.QHBoxLayout()
        self.h_layout_sql_pass.addWidget(self.sql_pass_text)
        self.h_layout_sql_pass.addWidget(self.sql_pass_line_edit)

        self.h_box_sql_pass = QtWidgets.QWidget(self)
        self.h_box_sql_pass.setLayout(self.h_layout_sql_pass)

        self.main_layout.addWidget(self.h_box_sql_pass)

        ##########################################
        ### /sql_pass                          ###
        ##########################################

        ##########################################
        ### sql_data                           ###
        ##########################################

        self.sql_data_text = QtWidgets.QLabel()
        self.sql_data_line_edit = QtWidgets.QLineEdit()

        self.h_layout_sql_data = QtWidgets.QHBoxLayout()
        self.h_layout_sql_data.addWidget(self.sql_data_text)
        self.h_layout_sql_data.addWidget(self.sql_data_line_edit)

        self.h_box_sql_data = QtWidgets.QWidget(self)
        self.h_box_sql_data.setLayout(self.h_layout_sql_data)

        self.main_layout.addWidget(self.h_box_sql_data)

        ##########################################
        ### /sql_data                          ###
        ##########################################

        ##########################################
        ### win_title                          ###
        ##########################################

        self.win_title_text = QtWidgets.QLabel()
        self.win_title_line_edit = QtWidgets.QLineEdit()

        self.h_layout_win_title = QtWidgets.QHBoxLayout()
        self.h_layout_win_title.addWidget(self.win_title_text)
        self.h_layout_win_title.addWidget(self.win_title_line_edit)

        self.h_box_win_title = QtWidgets.QWidget(self)
        self.h_box_win_title.setLayout(self.h_layout_win_title)

        self.main_layout.addWidget(self.h_box_win_title)

        ##########################################
        ### /win_title                         ###
        ##########################################

        ##########################################
        ### win_width                          ###
        ##########################################

        self.win_width_text = QtWidgets.QLabel()
        self.win_width_line_edit = QtWidgets.QLineEdit()

        self.h_layout_win_width = QtWidgets.QHBoxLayout()
        self.h_layout_win_width.addWidget(self.win_width_text)
        self.h_layout_win_width.addWidget(self.win_width_line_edit)

        self.h_box_win_width = QtWidgets.QWidget(self)
        self.h_box_win_width.setLayout(self.h_layout_win_width)

        self.main_layout.addWidget(self.h_box_win_width)

        ##########################################
        ### /win_width                         ###
        ##########################################

        ##########################################
        ### win_height                         ###
        ##########################################

        self.win_height_text = QtWidgets.QLabel()
        self.win_height_line_edit = QtWidgets.QLineEdit()

        self.h_layout_win_height = QtWidgets.QHBoxLayout()
        self.h_layout_win_height.addWidget(self.win_height_text)
        self.h_layout_win_height.addWidget(self.win_height_line_edit)

        self.h_box_win_height = QtWidgets.QWidget(self)
        self.h_box_win_height.setLayout(self.h_layout_win_height)

        self.main_layout.addWidget(self.h_box_win_height)

        ##########################################
        ### /win_height                        ###
        ##########################################

        ##########################################
        ### cell_width                         ###
        ##########################################

        self.cell_width_text = QtWidgets.QLabel()
        self.cell_width_line_edit = QtWidgets.QLineEdit()

        self.h_layout_cell_width = QtWidgets.QHBoxLayout()
        self.h_layout_cell_width.addWidget(self.cell_width_text)
        self.h_layout_cell_width.addWidget(self.cell_width_line_edit)

        self.h_box_cell_width = QtWidgets.QWidget(self)
        self.h_box_cell_width.setLayout(self.h_layout_cell_width)

        self.main_layout.addWidget(self.h_box_cell_width)

        ##########################################
        ### /cell_width                        ###
        ##########################################

        ##########################################
        ### cell_height                        ###
        ##########################################

        self.cell_height_text = QtWidgets.QLabel()
        self.cell_height_line_edit = QtWidgets.QLineEdit()

        self.h_layout_cell_height = QtWidgets.QHBoxLayout()
        self.h_layout_cell_height.addWidget(self.cell_height_text)
        self.h_layout_cell_height.addWidget(self.cell_height_line_edit)

        self.h_box_cell_height = QtWidgets.QWidget(self)
        self.h_box_cell_height.setLayout(self.h_layout_cell_height)

        self.main_layout.addWidget(self.h_box_cell_height)

        ##########################################
        ### /cell_height                       ###
        ##########################################

        ##########################################
        ### font_size                          ###
        ##########################################

        self.font_size_text = QtWidgets.QLabel()
        self.font_size_line_edit = QtWidgets.QLineEdit()

        self.h_layout_font_size = QtWidgets.QHBoxLayout()
        self.h_layout_font_size.addWidget(self.font_size_text)
        self.h_layout_font_size.addWidget(self.font_size_line_edit)

        self.h_box_font_size = QtWidgets.QWidget(self)
        self.h_box_font_size.setLayout(self.h_layout_font_size)

        self.main_layout.addWidget(self.h_box_font_size)

        ##########################################
        ### /font_size                         ###
        ##########################################

        ##########################################
        ### button setup                       ###
        ##########################################

        self.default_button = QtWidgets.QPushButton()
        self.default_button.setObjectName("button_default")
        self.submit_button = QtWidgets.QPushButton()
        self.submit_button.setObjectName("button_submit")

        self.button_layout = QtWidgets.QHBoxLayout()
        self.button_layout.setObjectName("button_layout")
        self.button_layout.addWidget(self.default_button)
        self.button_layout.addWidget(self.submit_button)
        self.main_layout.addLayout(self.button_layout)

        self.default_button.clicked.connect(self.default)
        self.submit_button.clicked.connect(self.submit)

        ##########################################
        ### /button setup                      ###
        ##########################################

        ##########################################
        ### text setup                         ###
        ##########################################

        # prompts
        self.sql_host_text.setText("mysql host")
        self.sql_port_text.setText("mysql port")
        self.sql_user_text.setText("mysql user")
        self.sql_pass_text.setText("mysql pass")
        self.sql_data_text.setText("mysql data")
        self.win_title_text.setText("win title")
        self.win_width_text.setText("win width")
        self.win_height_text.setText("win height")
        self.cell_width_text.setText("cell width")
        self.cell_height_text.setText("cell height")
        self.font_size_text.setText("font size")

        # default values
        self.sql_host_line_edit.setText(self.config.mysql_host)
        self.sql_port_line_edit.setText(self.config.mysql_port)
        self.sql_user_line_edit.setText(self.config.mysql_user)
        self.sql_pass_line_edit.setText(self.config.mysql_pass)
        self.sql_data_line_edit.setText(self.config.mysql_data)
        self.win_title_line_edit.setText(self.config.win_title)
        self.win_width_line_edit.setText(self.config.win_width)
        self.win_height_line_edit.setText(self.config.win_height)
        self.cell_width_line_edit.setText(self.config.cell_width)
        self.cell_height_line_edit.setText(self.config.cell_height)
        self.font_size_line_edit.setText(self.config.font_size)

        # buttons
        self.default_button.setText("Defaults")
        self.submit_button.setText("Submit")

        ##########################################
        ### text setup                         ###
        ##########################################

    def keyPressEvent(self, event):
        if event.key() == QtCore.Qt.Key_Return:
            self.submit()

    def submit(self):
        data = cl.config_storage()
        data.mysql_host  = self.sql_host_line_edit.text()
        data.mysql_port  = self.sql_port_line_edit.text()
        data.mysql_user  = self.sql_user_line_edit.text()
        data.mysql_pass  = self.sql_pass_line_edit.text()
        data.mysql_data  = self.sql_data_line_edit.text()
        data.win_title   = self.win_title_line_edit.text()
        data.win_width   = self.win_width_line_edit.text()
        data.win_height  = self.win_height_line_edit.text()
        data.cell_width  = self.cell_width_line_edit.text()
        data.cell_height = self.cell_height_line_edit.text()
        data.font_size   = self.font_size_line_edit.text()
        self.close()
        self.callback(data)

    def default(self):
        self.close()
        self.callback(None, True)

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    log = lw.logwriter()
    config = cl.config_loader(log.write).val
    log.construct(".log", config.win_title, "1.1.1", None, 3)
    win = config_window(log.write, config, None, None)
    win.show()

    sys.exit(app.exec_())

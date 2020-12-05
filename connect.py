from mysql.connector import connect, Error, errorcode
from decimal import Decimal
import config_loader as cl

class data_handler:
    def __init__(self, config, message):
        self.message = message
        self.config = config
        self.connected = False
        try:
            self.connection = connect(host=config.mysql_host, port=config.mysql_port, database=config.mysql_data, user=config.mysql_user, password=config.mysql_pass, auth_plugin='mysql_native_password')
            self.message(2, "Connection Established")
            self.connected = True
        except:
            self.message(0, "Error, Failed to establish connection to {}@{}:{} on {}".format(self.config.mysql_user, self.config.mysql_host, self.config.mysql_port, self.config.mysql_data))

    def pull(self, year, month, val, root):
        if self.connected:
            if root:
                sql_text = "select a.variable_input_id, a.value, b.name from budget a join variable_input_types b on a.variable_input_id = b.id"
            else:
                sql_text = "select * from variable_inputs where year(date) = {} and month(date) = {} and variable_input_id = {} order by date;".format(year, month, val)
            cursor = self.connection.cursor()
            cursor.execute(sql_text)
            results = cursor.fetchall()
            cursor.close()
            return results
        else:
            self.message(0, "Error, Not connected")
            return []

    def push(self, val, comment, date, value):
        if self.connected:
            sql_text = "insert into variable_inputs (variable_input_id, comment, date, value) values ({}, \"{}\", \"{}\", {});".format(val, comment, date, value)
            cursor = self.connection.cursor()
            cursor.execute(sql_text)
            self.connection.commit()
            cursor.close()
        else:
            self.message(0, "Error, Not connected")

if __name__ == "__main__":
    config_loader = cl.config_loader(message)
    config_loader.read()
    config = config_loader.val
    dh = data_handler(config, message)
    #print(dh.pull(0, 1))
    #dh.push(0, 1, "Upload_test", "2020-02-12", 74.89)
    print(dh.pull(0, 1, False))
    res = dh.pull(0, 1, True)
    print(res)
    print(res[0][2])
    # decimal arithmetic
    print(res[0][1] + Decimal(1))

from mysql.connector import connect, Error, errorcode
from decimal import Decimal
import config_loader as cl

def message(num, s):
    print(s)
#config = cl.config_loader(message).val
#connection = connect(host=config.mysql_host, database=config.mysql_data, user=config.mysql_user, password=config.mysql_pass)

#cursor = connection.cursor()
#cursor.execute("select * from variable_input")
#results = cursor.fetchall()
#print(results)

class data_handler:
    def __init__(self, config, message):
        self.message = message
        self.config = config
        try:
            self.connection = connect(host=config.mysql_host, database=config.mysql_data, user=config.mysql_user, password=config.mysql_pass)
            self.message(2, "Connection Established")
        except:
            self.message(0, "Error, Failed to establish connection")

    def pull(self, month, val, root):
        if root:
            sql_text = "select a.variable_input_id, a.value, b.name from budget a join variable_input_types b on a.variable_input_id = b.id"
        else:
            sql_text = "select * from variable_inputs where month = {} and variable_input_id = {};".format(month, val)
        cursor = self.connection.cursor()
        cursor.execute(sql_text)
        results = cursor.fetchall()
        cursor.close()
        return results

    def push(self, month, val, comment, date, value):
        sql_text = "insert into variable_inputs (month, variable_input_id, comment, date, value) values ({}, {}, \"{}\", \"{}\", {});".format(month, val, comment, date, value)
        cursor = self.connection.cursor()
        cursor.execute(sql_text)
        self.connection.commit()
        cursor.close()

if __name__ == "__main__":
    config = cl.config_loader(message).val
    dh = data_handler(config, message)
    #print(dh.pull(0, 1))
    #dh.push(0, 1, "Upload_test", "2020-02-12", 74.89)
    print(dh.pull(0, 1, False))
    res = dh.pull(0, 1, True)
    print(res)
    print(res[0][2])
    # decimal arithmetic
    print(res[0][1] + Decimal(1))

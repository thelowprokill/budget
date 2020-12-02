from mysql.connector import connect, Error, errorcode
import config_loader as cl

def message(num, s):
    print(s)

config = cl.config_loader(message).val
connection = connect(host=config.mysql_host, database=config.mysql_data, user=config.mysql_user, password=config.mysql_pass)

cursor = connection.cursor()
cursor.execute("select * from variable_input")
results = cursor.fetchall()
print(results)

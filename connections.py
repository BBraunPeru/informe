import mysql.connector
from mysql.connector import errorcode
import pandas as pd
cnx = mysql.connector.connect(user='root',
                            password ="Bbraunperu7",
                            host="localhost",
                            database='bombas')

cursor = cnx.cursor()
print("Coneccion exitosa")


def upload_to_database_masive(data):
  print(data)
  try:
    sql = 'INSERT INTO bombas_salida (modelo,servicio,serie,qr,estado) VALUES(%s,%s,%s,%s,%s)'
    cursor.executemany(sql,data)
    cnx.commit()

  except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
      print("Something is wrong with your user name or password")
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
      print("Database does not exist")
    else:
      print(err)
  else:
    cnx.close()


def upload_to_database(data:tuple):
  try:
    sql = 'INSERT INTO bombas_salida (modelo,servicio,serie,qr,estado) VALUES(%s,%s,%s,%s,%s)'
    cursor.execute(sql,data)
    cnx.commit()

  except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
      print("Something is wrong with your user name or password")
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
      print("Database does not exist")
    else:
      print(err)
  else:
    cnx.close()



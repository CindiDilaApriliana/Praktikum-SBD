#MODUL_12
#CINDI DILA APRILIANA_L200200106

from datetime import date, datetime, timedelta
import mysql.connector

cnx = mysql.connector.connect(user='root',database='perhotelan')
cursor = cnx.cursor()
update_kamar = ("DELETE FROM kamar WHERE id_tamuFK = 1009")
cursor.execute(update_kamar)

cnx.commit()
cursor.close()
cnx.close()

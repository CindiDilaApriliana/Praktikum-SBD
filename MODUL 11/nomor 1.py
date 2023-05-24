#MODUL_12
#CINDI DILA APRILIANA_L200200106

#INSERT Tamu
from datetime import date, datetime, timedelta
import mysql.connector

cnx = mysql.connector.connect(user='root',database='perhotelan')
cursor = cnx.cursor()
data_tamu = ("INSERT INTO tamu(id_tamu, nama, alamat, no_hp) VALUES(%s, %s, %s, %s)")
tambah_tamu = ('1010','Diana','Jl. Mawar 14','087903752763')
cursor.execute(data_tamu, tambah_tamu)

cnx.commit()
cursor.close()
cnx.close()


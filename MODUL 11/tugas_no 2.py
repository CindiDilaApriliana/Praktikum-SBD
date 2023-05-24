#PRAKTIKUM SBD_MODUL 11 
#CINDI DILA APRILIANA_L200200106

from datetime import date, datetime, timedelta
import mysql.connector

cnx = mysql.connector.connect(user='root',database='dbperbankan')
cursor = cnx.cursor()
query = ("SELECT*FROM nasabah")
cursor.execute(query)
for(id_nasabah, nama_nasabah, alamat_nasabah) in cursor:
    print("nasabah dengan ID {} bernama {} dengan alamat {}".format(id_nasabah,nama_nasabah,alamat_nasabah))
cursor.close()
cnx.close()

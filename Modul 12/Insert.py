#MODUL_12
#CINDI DILA APRILIANA_L200200106

#INSERT Transaksi
from datetime import date, datetime, timedelta
import mysql.connector

cnx = mysql.connector.connect(user='root',database='perhotelan')
cursor = cnx.cursor()
tanggal = datetime.now().date()
data_transaksi = ("INSERT INTO transaksi(id_transaksi, id_tamuFK, check_in, check_out) VALUES(%s, %s, %s, %s)")
tambah_transaksi = ('12311','1011','2022-04-01','2022-04-02')
cursor.execute(data_transaksi, tambah_transaksi)

cnx.commit()
cursor.close()
cnx.close()


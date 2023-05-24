#PRAKTIKUM SBD_MODUL 11 
#CINDI DILA APRILIANA_L200200106

from datetime import date, datetime, timedelta
import mysql.connector

cnx = mysql.connector.connect(user='root',database='dbperbankan')
cursor = cnx.cursor()
tanggal = datetime.now().date()
tambah_transaksi = ("DELETE FROM transaksi WHERE no_transaksi= '32'")
cursor.execute(tambah_transaksi)

cnx.commit()
cursor.close()
cnx.close()

##from datetime import date, datetime, timedelta
##import mysql.connector
##
##cnx = mysql.connector.connect(user='root',database='dbperbankan')
##cursor = cnx.cursor()
##tanggal = datetime.now().date()
##tambah_transaksi = ("INSERT INTO transaksi (id_nasabahFK, no_rekeningFK, jenis_transaksi, tanggal, jumlah) VALUES(%s,%s,%s,%s,%s)")
##data_transaksi = ('102','120','kredit',tanggal,'100000')
##cursor.execute(tambah_transaksi, data_transaksi)
##
##cnx.commit()
##cursor.close()
##cnx.close()

##from datetime import date, datetime, timedelta
##import mysql.connector
##
##cnx = mysql.connector.connect(user='root',database='dbperbankan')
##cursor = cnx.cursor()
##tanggal = datetime.now().date()
##tambah_transaksi = ("UPDATE transaksi SET jenis_transaksi = 'debit' WHERE no_transaksi= '32'")
##cursor.execute(tambah_transaksi)
##
##cnx.commit()
##cursor.close()
##cnx.close()

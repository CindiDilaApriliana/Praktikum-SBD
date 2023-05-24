#PRAKTIKUM SBD_MODUL 11 
#CINDI DILA APRILIANA_L200200106

from datetime import date, datetime, timedelta
import mysql.connector

cnx = mysql.connector.connect(user='root', database='dbperbankan')
cursor = cnx.cursor()
query = ('select `id_nasabahFK`, `jenis_transaksi`, `tanggal`, `jumlah` from transaksi where month (tanggal)between 10 and 12')

cursor.execute(query)
for(id_nasabahFK, jenis_transaksi, tanggal, jumlah) in cursor:
   print("Berikut data nasabah dengan ID {} melakukan transaksi {} pada {:%d %b %Y} sejumlah {}".format(id_nasabahFK, jenis_transaksi, tanggal, jumlah))
cursor.close()
cnx.close()

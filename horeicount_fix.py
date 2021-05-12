import sqlite3
import csv

dbname = 'horei.db'
conn = sqlite3.connect(dbname)
cur = conn.cursor()

cur.execute('SELECT COUNT(detail_url) from download_status')
print("取得URL数は " + str(cur.fetchall()) + "個です。")

cur.execute('SELECT COUNT(status) from download_status WHERE status != 1')
print("ステータスが1ではないデータは" + str(cur.fetchall()) + "個あります。")

print("ステータスが1ではないデータの一覧はこちらです。")
cur.execute('SELECT * from download_status where status != 1')
print(cur.fetchall())

cur.execute('SELECT * FROM download_status')
datanum = cur.fetchall()


csvhorei = open('1newcsvhorei.csv', 'w')
w = csv.writer(csvhorei)
w.writerows(datanum)
csvhorei.close()

cur.close()
conn.close()
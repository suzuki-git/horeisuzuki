import sqlite3


dbname = 'horeisuzuki.db'
conn = sqlite3.connect(dbname)
cur = conn.cursor()

cur.execute('SELECT * FROM download_status')
datanum = cur.fetchall()
datastr = str(datanum)
#print(cur.fetchall())
print(datanum)
print(datastr.count('lawId='))
print(datastr.count('lawId_'))
print(datastr.count(' 1,'))
print(datastr.count('5,'))

cur.close()
conn.close()
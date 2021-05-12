import sqlite3


dbname = 'horei.db'
conn = sqlite3.connect(dbname)
cur = conn.cursor()

cur.execute('SELECT * FROM download_status')
datanum = cur.fetchall()
datastr = str(datanum)
# print(cur.fetchall())
print(datanum)
print(datastr.count('lawId='))
print(datastr.count('lawId_'))

statuscheck = datastr.count('0,')
if statuscheck == 0:
    print("status is safe")
else:
    cur.execute('SELECT * FROM download_status where status = 0')
    print("status Error is " + str(statuscheck))


print(datastr.count(' 1,'))
print(datastr.count('5,'))

cur.close()
conn.close()
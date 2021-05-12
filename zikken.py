import sqlite3


dbname = 'horei.db'
conn = sqlite3.connect(dbname)
cur = conn.cursor()

cur.execute('SELECT * FROM download_status where status = 0')
cur.execute('SELECT * FROM download_status where status = 1')
cur.execute('SELECT * FROM download_status where status = 0')
cur.execute('SELECT * FROM download_status where status = 1')
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
    cur.execute('SELECT * FROM download_status where status != 1')
    statusdata = cur.fetchall()
    statusstr = str(statusdata)
    print("status Error is " + str(statuscheck))

cur.close()
conn.close()
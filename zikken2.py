import sqlite3


dbname = 'horei.db'
conn = sqlite3.connect(dbname)
cur = conn.cursor()

cur.execute('SELECT COUNT(detail_url) from download_status')
print(cur.fetchall())


cur.close()
conn.close()
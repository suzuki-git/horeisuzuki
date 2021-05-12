import sqlite3
import traceback

def main():
    return


class HoreiDatabase:

    def __init__(self):

        self.conn = sqlite3.connect('horei.db')
        self.c = self.conn.cursor()
        self.c.execute('CREATE TABLE IF NOT EXISTS detail_urls (detail_url text PRIMARY KEY)')
        self.c.execute('CREATE TABLE IF NOT EXISTS download_status (detail_url text PRIMARY KEY, status int)')
        self.conn.commit()

    def insert_detail_url(self, detail_url):
        try:
            self.c.execute('INSERT INTO detail_urls VALUES ("' + detail_url + '")')
            self.conn.commit()
            print('Store success : ', detail_url)
        except sqlite3.IntegrityError:
            print('Already exist : ', detail_url)

        return

    def select_detail_urls(self):
        detail_urls = []
        try:
            self.c.execute('SELECT detail_url FROM detail_urls')
        except:
            print('SELECT Error.')
            return
        for temp_url in self.c.fetchall():
            detail_urls.append(temp_url[0])
        return detail_urls

    def is_exists_download_status(self, detail_url):
        try:
            self.c.execute('SELECT COUNT(*) FROM download_status WHERE detail_url="' + detail_url + '"')
        except:
            traceback.print_exc()
            print('SELECT error on is_exists_download_status.')
            return False
        return int(self.c.fetchone()[0])

    def insert_download_status(self, detail_url, status):
        if status:
            status_str = '1'
        else:
            status_str = '0'
        if self.is_exists_download_status(detail_url):
            sql = 'UPDATE download_status SET status=' + status_str + ' WHERE detail_url="' + detail_url + '"'
        else:
            sql = 'INSERT INTO download_status VALUES ("' + detail_url + '", ' + status_str + ')'

        try:
            self.c.execute(sql)
            self.conn.commit()
        except:
            traceback.print_exc()
            print('INSERT error on download_status.')
            return False

        return True

    def check_download_status(self, detail_url):
        sql = 'SELECT status FROM download_status WHERE detail_url="' + detail_url + '"'
        try:
            self.c.execute(sql)
        except:
            traceback.print_exc()
            print('SELECT download_status Error')
            return False
        result = self.c.fetchone()
        if result:
            return result[0]
        return False


if __name__ == '__main__':
    main()

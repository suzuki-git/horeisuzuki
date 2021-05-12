import re
import time
import requests
from bs4 import BeautifulSoup
import os


def main():
    return


class HoreiWeb:

    def __init__(self):
        self.session = requests.session()
        self.base_url = 'https://hourei.ndl.go.jp'
        self.search_url = self.base_url + '/simple/?searchCross'
        self.pager_url = self.base_url + '/simple/result?pager&page='

        return

    def get_last_page_num(self, start):
        # 最初の検索結果画面を取得
        if start:
            payload = {
                'epp1_01': 'range',
                'epef_01': '',
                'epyf_01': start[0],
                'epmf_01': start[1],
                'epdf_01': start[2]
            }
        else:
            payload = {}
        print(payload)
        response = self.session.post(self.search_url, data=payload)
        soup = BeautifulSoup(response.text, 'html.parser')
        print(soup.find_all('h3'))
        last_page = 0
        for a in soup.find_all('a'):
            if 'onclick' in a.attrs:
                match = re.search(r'\d+', a.attrs['onclick'])
                page = int(match.group())
                if last_page < page:
                    last_page = page

        return last_page

    def get_page(self, page):
        # ページ送り
        response = self.session.get(self.pager_url + str(page))
        soup = BeautifulSoup(response.text, 'html.parser')
        return soup

    def get_list(self, soup):
        detail_urls = []
        for a in soup.find_all('a'):
            if 'href' in a.attrs:
                url = a.attrs['href']
                if '/simple/detail' in url:
                    m = re.search(r'(/simple/detail\?.*)&', url)
                    detail_urls.append(m.groups()[0])
        return detail_urls

    def store_detail_urls(self, last_page, horei_db):
        count = 1
        for page in range(1, last_page + 1):
            soup = self.get_page(page)
            detail_urls = self.get_list(soup)
            for detail_url in detail_urls:
                print(count)
                horei_db.insert_detail_url(detail_url)
                count = count + 1
            time.sleep(0.1)
        return

    def fetch_detail_page(self, detail_url):

        def make_dirs():
            if not os.path.exists(download_dir):
                os.mkdir(download_dir)
            if not os.path.exists(sub_dir):
                os.mkdir(sub_dir)

            return

        try:
            response = self.session.get(self.base_url + detail_url)
        except:
            print('Can not fetch detail page. ', detail_url)
            return False

        download_dir = './detail_pages/'
        sub_dir = download_dir + detail_url[-2:] + '/'
        m = re.search(r'/simple/detail\?(.*)', detail_url)
        filename = m.groups()[0].replace('=', '_')
        path = sub_dir + filename

        make_dirs()

        try:
            with open(path, mode='w') as f:
                f.write(response.text)
        except:
            print('Can not write detail page. ', detail_url)
            return False

        return True


if __name__ == '__main__':
    main()

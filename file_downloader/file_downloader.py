import os

import requests
from bs4 import BeautifulSoup


class FileDownloader:
    def __init__(self, url, log_file=None, use_url=True):
        self.log = log_file

        if use_url:
            print('[+]Starting...')
            if not url.endswith('/'):
                self.url = url + '/'
            self.url = url

            print('[.]Getting data')
            self.req = requests.get(url).text
            print('[+]Got all data')

            print('[.]Analyzing data\n')
            self.files = self.bs4()
            print('\n[+]Data analyzed')

            if self.log:
                print('[.]Logging data')
                with open(self.log, 'w') as f:
                    f.write('\n'.join(self.files))
                print('[+]Data loged')
        else:
            self.url = url
            if not self.log:
                print('[-]Please use log or URL')

            print('[+]Loading data')
            with open(self.log, 'r') as f:
                self.files = [i.replace('\n', '') for i in f.readlines()]
            print('[+]Data loaded')

    def bs4(self):
        l = []
        bs = BeautifulSoup(self.req, 'html.parser')
        for a in bs.findAll('tr'):
            for b in a.findAll('td'):
                if b.find('a'):
                    obj = b.find('a').get('href')
                    if not obj in ['/', '?', '#']:
                        l.append(obj)
                        print(f'[+]File found: {obj}')
        return l

    def download(self, type_=None):
        if not os.path.exists('Dowloads'):
            os.mkdir('Dowloads')
        for file in self.files:
            if type_ and not file.endswith(type_):
                continue
            print(f'[.]Downloading: {file}')
            self.download_m(file)
            print(f'[+]Downloaded: {file}')
        print(f'[+]All {type_ + " " if type_ else ""}files downloaded')

    def download_m(self, f):
        url = self.url + f
        with open('Dowloads/' + f, 'wb')as file:
            file.write(requests.get(url).content)


if __name__ == '__main__':
    f = FileDownloader('http://localhost/img/', 'log.txt', True)
    f.download('epub')

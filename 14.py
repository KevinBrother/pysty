# requests库
import requests, json
from threading import Thread
from multiprocessing import Process

class DwonPic(Thread):
    def __init__(self, url):
        super().__init__()
        self._url = url
    
    def run(self):
        fileName = self._url[self._url.rfind('/') + 1:]
        originPic = requests.get(self._url)
        with open('/home/brother/图片/downPic/%s' % fileName, 'wb') as pic:
            pic.write(originPic.content)


def main():

    req = requests.get('http://api.tianapi.com/meinv/?key=16508bc4c0816c304c76d16246a8e3d3&num=10')
    data_model = req.json()

    for mm_dict in data_model['newslist']:
        url = mm_dict['picUrl']
        # Process(target=DwonPic, args=(url, )).start()
        DwonPic(url).start()


if __name__ == "__main__":
    main()
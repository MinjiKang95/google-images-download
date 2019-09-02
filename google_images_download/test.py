# -*- coding: utf-8 -*-
from google_images_download import googleimagesdownload

import sys
reload(sys)
sys.setdefaultencoding('utf-8')

import ssl
ssl._create_default_https_context = ssl._create_unverified_context

def imageCrawling(keyword, dir):
    response = googleimagesdownload()

    arguments = {"keywords": keyword,
                 "format": "jpg",
                 "limit": 200, #크롤링 이미지수
                 "print_urls":True, #이미지 url 출력
                 "no_directory": True,
                 'output_directory': dir} #크롤링 이미지 저장 폴더

    paths = response.download(arguments)
    print paths

imageCrawling('강남길', 'D:/datahdd/face/AnotherMissOh/add/Kang_namgil')
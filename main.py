# -*- coding : utf-8 -*-

from bs4 import BeautifulSoup
from datetime import date, datetime
import requests
import pickle
import os

url = 'https://play.google.com/store/apps/details?id=com.eg.android.AlipayGphone'
filename = 'alipay.version'
botURL = ''
response = requests.get(url)
soup = BeautifulSoup(response.text, 'lxml')
version_element = soup.find('div', string='Current Version').next_sibling
version_number = version_element.find('span').text
saved_version = None
if os.path.exists(filename):
    with open(filename, 'rt') as f:
        saved_version = f.readline()
    if saved_version != version_number
        botBody = {
                    'chat_id': ,
                    'text': 'alipay updated'
            }
        requests.post(botURL + 'sendMessage', data=botBody)
    else:
        print('not updated yet: {} vs {}'.format(saved_version, version_number))
with open(filename, 'wt') as f:
    f.write(version_number)

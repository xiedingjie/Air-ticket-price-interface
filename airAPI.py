#-*- coding: UTF-8 -*-

import requests
import sys
import time
import json

reload(sys)
sys.setdefaultencoding('utf8')

class airAPI(object):
    def __init__(self):
        self.url = 'https://jipiao.jd.com/search/queryFlight.action'
        self.host = 'https://jipiao.jd.com/'
        self.headers = {
            'Host': "jipiao.jd.com",
            'Accept-Language': "zh-CN,zh;q=0.8,en;q=0.6",
            'Accept-Encoding': "gzip, deflate, br",
            'X-Requested-With' : 'XMLHttpRequest',
            'Connection': "keep-alive",
            'User-Agent': "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36"
        }
        self.depCity = ''
        self.arrCity = ''
        self.dateTime = ''

    def setDepCity(self,depCity):
        self.depCity = depCity


    def setArrCity(self,arrCity):
        self.arrCity = arrCity

    def setDate(self,dateTime):
        self.dateTime = dateTime

    def getAirInfo(self):
        depCity = self.depCity
        arrCity = self.arrCity
        dateTime = self.dateTime
        url = self.url
        host = self.host
        headers = self.headers

        payload = {'depCity': depCity, 'arrCity': arrCity, 'depDate': dateTime, 'arrDate': dateTime,
                   'queryModule': '1',
                   'lineType': 'OW', 'queryType': 'jipiaoindexquery'}
        req = requests.session()
        req.get(host,headers=headers)
        time.sleep(1)
        airInfo = req.get(url, headers=headers, params=payload).json()

        return airInfo

if __name__ == "__main__":

    api = airAPI()
    api.setDepCity('广州')
    api.setArrCity('海口')
    api.setDate('2018-11-20')
    airInfo = api.getAirInfo()

    for i in airInfo['data']['flights']:
        print json.dumps(i,ensure_ascii=False)


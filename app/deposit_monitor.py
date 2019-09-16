# _*_ coding: UTF-8 _*_
import json

import requests
from config import *


class DepositMonitor:

    def __init__(self, account='eosdeposit11'):
        self.monitor_account = account

    @property
    def headers(self):
        return {
            'accept': 'application/json;charset=UTF-8',
            'content-type': 'application/json',
            'apikey': '5b4added-e80c-41fb-b5a9-16269d2de79b'
        }

    def req_body(self, page_no=1, page_size=100):
        return {
            'account_name': self.monitor_account,
            'sort': 2,
            'size': page_size,
            'page': page_no
        }

    def get_transfer_total(self):
        resp = requests.post(url=API['GET_ACCOUNT_TRANSFER'], json=self.req_body(), headers=self.headers)
        print('获取监控账户转账总数返回:{}'.format(resp.text))
        return json.loads(resp.text)['total']

    def page_transfer_list(self, page_no):
        req = self.req_body(page_no=page_no)
        resp = requests.post(url=API['GET_ACCOUNT_TRANSFER'], json=req, headers=self.headers)
        print('获取第{}页数据返回:{}'.format(page_no, resp.text))
        return json.loads(resp.text)['list']


if __name__ == '__main__':
    monitor = DepositMonitor()
    print(monitor.get_transfer_total())

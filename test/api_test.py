# _*_ coding: UTF-8 _*_

import json

import requests
from config import *


def test():
    req_body = {
        # 交易的发起者或接收者
        'account_name': 'eosdeposit11',
        # 代币合约账号
        # 'code': 'eosio',
        # 'symbol': 'EOS',
        # 'type': '2',
        # 'from': '',
        # 'to': 'eosdeposit11',
        # 'start_block_num': '78045886',
        # 'end_block_num': '78045888',
        'size': '100',
        'page': '1'
    }
    headers = {
        'accept': 'application/json;charset=UTF-8',
        'content-type': 'application/json',
        'apikey': '5b4added-e80c-41fb-b5a9-16269d2de79b'
    }
    resp = requests.post(url=API['GET_ACCOUNT_TRANSFER'], json=req_body, headers=headers)
    result = json.loads(resp.text)
    total = result['total']
    data_list = result['list']
    print('返回账户数据列表总数:', total)
    for item in data_list:
        print('循环输出转账记录:', item)


if __name__ == '__main__':
    test()
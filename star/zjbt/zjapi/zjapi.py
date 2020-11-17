#! /usr/bin/env python3
# coding: utf-8

import json
import hashlib

if __name__ == '__main__':

    jsonStr = '''
        {
            "request_head": {
                "version": "1.0",
                "token": "163a14ab-cfe5-450a-bda8-c064304c8ead",
                "timestamp": 1605601382000,
                "sign": "6D78C94CEE4C484C13E6229951C5D8FA"
            },
            "request_body": {
                "vehicleNo": "京B21838",
                "vehicleColor": "2"
            }
        }
    '''

    # jsonStr = '''
    #     {
    #         "request_head": {
    #             "version": "1.0",
    #             "token": "c63fd532ee4e11eaa73edb9cebfddf38",
    #             "timestamp": 1599183222000
    #         },
    #         "request_body": {
    #             "user_name": "username",
    #             "passwd": "passwd"
    #         }
    #     }
    # '''
    jsonObj = json.loads(jsonStr)
    requestHead = jsonObj['request_head']
    requestBody = jsonObj['request_body']
    requestHead.update(requestBody)
    print(requestHead)
    del requestHead['sign']
    print(requestHead)
    requestMsg = sorted(requestHead.items(), key=lambda item: item[0])
    requestStr = ''
    for value in requestMsg:
        requestStr += str(value[0]) + '=' + str(value[1]) + '&'
    requestStr += 'signSecret=e0fbab1c403b40568c5fec91fe45a577'
    print(requestStr)
    sign = hashlib.md5(requestStr.encode()).hexdigest().upper()
    print(sign)
    requestHead['sign'] = sign
    print(requestHead)




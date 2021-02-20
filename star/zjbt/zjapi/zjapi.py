#! /usr/bin/env python3
# coding: utf-8

import json
import hashlib

if __name__ == '__main__':

    jsonStr = '''
{
    "request_head": {
        "version": "1.0",
        "token": "592df0dc-0e62-44c5-9533-85c4a6c124c4",
        "timestamp": 1612686199000,
 		  "sign": "E01B02740BA0C1553E95B635091941CC"

    },
    "request_body": {
        "vehicleNo": "京AEE635",
        "vehicleColor": "2"
    }
}
    '''
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




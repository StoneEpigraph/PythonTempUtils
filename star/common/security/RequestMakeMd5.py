#!/usr/bin/env python3
import hashlib
import json

if __name__ == '__main__':

    requestStr = '''
{
    "request_head": {
        "timestamp": 1623391030086,
        "version": "V1.0",
        "token": "EF1FC153-4350-440F-99B2-81DF4021D098",
        "sign": "340BFBA6FB7AD954AAC7453948106629"

    },
    "request_body": {
        "order_no": "310421060220222590"
    }
}
    '''
    requestJson = json.loads(requestStr)
    print(requestJson)
    requestHead = requestJson['request_head']
    requestBody = requestJson['request_body']
    if "sign" in requestHead:
        del requestHead['sign']
    requestHead.update(requestBody)
    print(requestHead)
    sortedReqKey = sorted(requestHead)
    print(sortedReqKey)
    sortedRequestStr = "";
    for key in sortedReqKey:
        sortedRequestStr += (key + "=" + str(requestHead[key]) + "&")
    sortedRequestStr += "signSecret=e0fbab1c403b40568c5fec91fe45a577"
    md5 = hashlib.md5()
    print(sortedRequestStr)
    print(sortedRequestStr.encode("utf-8"))
    md5.update(sortedRequestStr.encode("utf-8"))
    sign = md5.hexdigest().upper()
    print(sign)

    '''
    password=E3ak35Yju*Wd0&timestamp=1608797843000&username=shenpi&version=V1.0&signSecret=e0fbab1c403b40568c5fec91fe45a577
    password=E3ak35Yju*Wd0&timestamp=1608797843000&token=B6427C27-666E-445C-A8A7-BCEDB5A760CE&username=shenpi&version=V1.0&signSecret=e0fbab1c403b40568c5fec91fe45a577
    '''






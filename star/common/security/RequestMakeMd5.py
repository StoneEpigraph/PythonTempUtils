#!/usr/bin/env python3
import hashlib
import json

if __name__ == '__main__':

    requestStr = '''
{
    "request_head": {
        "timestamp": 1608798505000,
        "version": "V1.0",
        "token": "0f224c54-6d9d-485f-b011-00d83f8d8ce2",
        "sign": "D916D9FCB663AB4A419B62D20A2513AE"

    },
    "request_body": {
        "vehicle_no": "京B25306",
        "plate_color": "2"
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






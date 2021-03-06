#! /usr/bin/env python3


import re
import json

def writefile(filename, data, args = 'w'):
    f = open(filename, args)
    f.write(json.dumps(data, separators=(',', ':'), ensure_ascii=False))
    f.close()

if __name__ == '__main__':
    file = open('./region.txt')
    line = file.readline()
    res = []                    # regionList
    provinceCodeArr = []        # 省CodeList
    cityCodeArr = []            # 市CodeList
    areaSqlList = []            # insertSQL
    num = 0                     # 总计添加到结果对象数
    count = 0                   # 总计遍历行数
    while line:
        count += 1
        if len(line) < 1:
            break
        strArr = list(filter(lambda x : x, re.split("\s", line)))
        code = strArr[0].strip()
        name = strArr[1].strip()
        regionObj = {
            "value": code,
            "label": name,
            "children": []
        }
        if (int(code) % 10000 == 0):
            # province
            provinceCodeArr.append(code)
            res.append(regionObj)
            areaSqlList.append("insert into tbcc_area(code, name, level, parent_code, short_name, all_name, status) values({value}, '{label}', 0, 0, '{label}', '{label}', 1);".format(**regionObj))
            num += 1
        else:
            if (int(code) % 100 == 0):
                # city
                for province in res:
                    provinceCode = province['value']
                    provinceName = province['label']
                    if str(provinceCode) == str(int(code) // 10000 * 10000):
                        cityList = province['children']
                        cityObj = {
                            "value": code,
                            "label": name,
                            "children": []
                        }

                        cityList.append(cityObj)
                        cityCodeArr.append(code)
                        num += 1
                        areaSqlList.append(
                            "insert into tbcc_area(code, name, level, parent_code, short_name, all_name, status) values({value}, '{label}', 1, {provinceCode}, '{label}', '{fullName}', 1);".format(
                                **{
                                    "value": code,
                                    "label": name,
                                    "provinceCode": provinceCode,
                                    "fullName": provinceName + "-" + name
                                }))
                        break
            else:
                for province in res:
                    provinceCode = province['value']
                    provinceName = province['label']
                    if str(provinceCode) == str(int(code) // 10000 * 10000):
                        cityCode = str(int(code) // 100 * 100)
                        cityList = province['children']
                        if cityCode not in cityCodeArr:
                            # 如果找不到父级直接找省级,将直辖县挂到省级下边
                            if name.endswith('区') and not name.endswith('地区'):
                                # 判断区县级是否有市区Code
                                for city in cityList:
                                    cityCode = city['value']
                                    if cityCode == provinceCode:
                                        break
                                else:
                                    cityList.append({
                                        "value": provinceCode,
                                        "label": provinceName + "区"
                                    })
                            else:
                                cityList.append(
                                    {
                                        "value": code,  # 省直辖县
                                        "label": name
                                    }
                                )
                            num += 1
                            areaSqlList.append(
                            "insert into tbcc_area(code, name, level, parent_code, short_name, all_name, status) values({value}, '{label}', 1, {provinceCode}, '{label}', '{fullName}', 1);".format(
                                **{
                                    "value": code,
                                    "label": name,
                                    "provinceCode": provinceCode,
                                    "fullName": provinceName + "-" + name
                                }))
                            break
                        for city in cityList:
                            cityCode = city['value']
                            cityName = city['label']
                            if str(int(code) // 100 * 100) == str(cityCode):
                                countyObj = {
                                    "value": code,
                                    "label": name,
                                }
                                countyList = city['children']
                                if (name.endswith('区') and not name.endswith('地区')):
                                    # 判断区县级是否有市区
                                    for county in countyList:
                                        countyCode = county['value']
                                        if countyCode == cityCode:

                                            break
                                    else:
                                        countyList.append({
                                            "value": cityCode,
                                            "label": cityName + "区"
                                        })
                                else:
                                    countyList.append(countyObj)
                                num += 1

                                areaSqlList.append(
                                    "insert into tbcc_area(code, name, level, parent_code, short_name, all_name, status) values({value}, '{label}', 2, {provinceCode}, '{label}', '{fullName}', 1);".format(
                                        **{
                                            "value": code,
                                            "label": name,
                                            "provinceCode": cityCode,
                                            "fullName": provinceName + "-" + cityName + "-" + name
                                        }))
                                break
        if num != count:
            print("not add : ", line)
            num += 1
        line = file.readline()
    file.close()

    # 去除空的children
    for province in res:
        # 去掉空的省
        provinceChildrenList = province['children']
        if len(provinceChildrenList) < 1:
            del province['children']
        else:
            for city in provinceChildrenList:
                if 'children' in city.keys():
                    cityChildrenList = city['children']
                    if len(cityChildrenList) < 1:
                        del city['children']

    print({"region": res})
    print(num)
    print(count)
    print(len(areaSqlList))
    writefile("regionsThreeLevel.json", res)

    # 写sql
    f = open("tbccArea.sql", "w+")
    for sql in areaSqlList:
        f.writelines(sql + "\n")
    f.close()

#!/usr/bin/env python3
# coding: utf-8

import requests
from bs4 import BeautifulSoup

def parseUrl(url):

    req = requests.get(url);
    soup = BeautifulSoup(req.content, 'lxml', from_encoding='utf-8')
    content = soup.find('div', class_='content').get_text()
    file = open('file.md', 'a+')
    file.write(content)
    file.close()

if __name__ == '__main__':
    url = "https://www.kancloud.cn/alex_wsc/java_thinking/";
    title_link = (1921117,
                  1921118,
                  1921119,
                  1921120,
                  1921227,
                  1921228,
                  1921283,
                  1921284,
                  1921285,
                  1921286,
                  1921302,
                  1921287,
                  1921288,
                  1921289,
                  1921298,
                  1921299,
                  1934225,
                  1921121,
                  1921303,
                  1922795,
                  1922796,
                  1922797,
                  1922798,
                  1921122,
                  1922799,
                  1922800,
                  1922801,
                  1922803,
                  1922804,
                  1922805,
                  1922806,
                  1922807,
                  1922808,
                  1922809,
                  1922810,
                  1922811,
                  1922812,
                  1922827,
                  1922828,
                  1922829,
                  1922830,
                  1922831,
                  1922836,
                  1922837,
                  1922841,
                  1922842,
                  1922850,
                  1922851,
                  1922856,
                  1921125,
                  1922862,
                  1922863,
                  1922865,
                  1922866,
                  1922947,
                  1922948,
                  1922949,
                  1922950,
                  1922951,
                  1922952,
                  1922953,
                  1922958,
                  1922961,
                  1922978,
                  1922993,
                  1922994,
                  1922995,
                  1922996,
                  1922997,
                  1923001,
                  1923002,
                  1923003,
                  1923004,
                  1923005,
                  1923013,
                  1921127,
                  1923014,
                  1923029,
                  1923031,
                  1923032,
                  1923033,
                  1923034,
                  1923035,
                  1923046,
                  1923047,
                  1923048,
                  1923049,
                  1923050,
                  1923105,
                  1923106,
                  1921128,
                  1923107,
                  1923175,
                  1923176,
                  1923177,
                  1923192,
                  1923193,
                  1923196,
                  1923197,
                  1923205,
                  1923218,
                  1923234,
                  1923235,
                  1923236,
                  1923237,
                  1923238,
                  1923239,
                  1923240,
                  1923325,
                  1923327,
                  1923328,
                  1923329,
                  1923342,
                  1923343,
                  1923359,
                  1923360,
                  1923361,
                  1921129,
                  1923376,
                  1923377,
                  1923378,
                  1923381,
                  1923382,
                  1923383,
                  1923490,
                  1923505,
                  1923506,
                  1923507,
                  1923508,
                  1923509,
                  1923510,
                  1923511,
                  1923512,
                  1923513,
                  1923514,
                  1921130,
                  1923520,
                  1923527,
                  1923632,
                  1923633,
                  1923634,
                  1923635,
                  1923636,
                  1923637,
                  1923638,
                  1923639,
                  1923640,
                  1923641,
                  1923643,
                  1923647,
                  1923662,
                  1923663,
                  1923664,
                  1923665,
                  1923666,
                  1923667,
                  1923644,
                  1923646,
                  1923645,
                  1921131,
                  1923675,
                  1923676,
                  1923677,
                  1923682,
                  1923683,
                  1923684,
                  1923685,
                  1923686,
                  1923678,
                  1923688,
                  1923689,
                  1923690,
                  1923679,
                  1923680,
                  1923691,
                  1923692,
                  1923681,
                  1921132,
                  1923772,
                  1923773,
                  1923786,
                  1923787,
                  1923788,
                  1923789,
                  1923774,
                  1923775,
                  1923776,
                  1923777,
                  1923778,
                  1923779,
                  1923780,
                  1923781,
                  1923782,
                  1923783,
                  1923784,
                  1921133,
                  1923790,
                  1923791,
                  1923792,
                  1923793,
                  1923794,
                  1923795,
                  1923796,
                  1923797,
                  1923798,
                  1923799,
                  1923800,
                  1923801,
                  1923802,
                  1923803,
                  1923804,
                  1923805,
                  1923806,
                  1921137,
                  1924099,
                  1924100,
                  1924101,
                  1924106,
                  1924108,
                  1924109,
                  1924110,
                  1924111,
                  1924112,
                  1924113,
                  1924115,
                  1924116,
                  1924117,
                  1924118,
                  1924119,
                  1924121,
                  1924122,
                  1921138,
                  1924123,
                  1924124,
                  1924125,
                  1924126,
                  1924127,
                  1924129,
                  1924130,
                  1924131,
                  1924138,
                  1924139,
                  1924140,
                  1924141,
                  1924142,
                  1924143,
                  1924144,
                  1924145,
                  1924146,
                  1921139,
                  1924147,
                  1924148,
                  1924149,
                  1924150,
                  1924151,
                  1924152,
                  1924153,
                  1924154,
                  1924155,
                  1924156,
                  1924160,
                  1924161,
                  1924162,
                  1924163,
                  1924164,
                  1924157,
                  1924165,
                  1924166,
                  1924167,
                  1924168,
                  1924158,
                  1924169,
                  1924170,
                  1924171,
                  1924172,
                  1924173,
                  1924174,
                  1924175,
                  1924159,
                  1921140,
                  1926686,
                  1926687,
                  1926688,
                  1926689,
                  1926714,
                  1926715,
                  1926716,
                  1926690,
                  1926691,
                  1926692,
                  1926694,
                  1926717,
                  1926718,
                  1926719,
                  1926720,
                  1926721,
                  1926695,
                  1926722,
                  1926698,
                  1926723,
                  1926724,
                  1926725,
                  1926699,
                  1926700,
                  1926708,
                  1926726,
                  1926709,
                  1926710,
                  1926730,
                  1926731,
                  1926732,
                  1926733,
                  1926711,
                  1926712,
                  1926713,
                  1921142,
                  1927145,
                  1927147,
                  1927148,
                  1927149,
                  1927150,
                  1927151,
                  1927152,
                  1927153,
                  1927154,
                  1927155,
                  1927156,
                  1927157,
                  1927158,
                  1927159,
                  1927160,
                  1927161,
                  1927162,
                  1927163,
                  1927164,
                  1927165,
                  1927166,
                  1927167,
                  1927169,
                  1927170,
                  1927171,
                  1927172,
                  1927173,
                  1927174,
                  1927175,
                  1927176,
                  1927177,
                  1927178,
                  1927179,
                  1927180,
                  1927181,
                  1927182,
                  1927183,
                  1927184,
                  1921143,
                  1929993,
                  1929995,
                  1929996,
                  1929997,
                  1929998,
                  1929999,
                  1930022,
                  1930023,
                  1930024,
                  1930025,
                  1921144,
                  1930028,
                  1930132,
                  1930133,
                  1930134,
                  1930135,
                  1930137,
                  1930138,
                  1930139,
                  1930140,
                  1930141,
                  1930142,
                  1930143,
                  1930136,
                  1930144,
                  1930145,
                  1930146,
                  1930168,
                  1930169,
                  1930170,
                  1930171,
                  1930172,
                  1930173,
                  1930174,
                  1930175,
                  1930176,
                  1930177,
                  1930178,
                  1930179,
                  1930180,
                  1930181,
                  1921145,
                  1930182,
                  1930183,
                  1930184,
                  1930186,
                  1930187,
                  1930188,
                  1930189,
                  1930190,
                  1930195,
                  1930198,
                  1930199,
                  1930200,
                  1930201,
                  1930202,
                  1930203,
                  1930204,
                  1930205,
                  1930206,
                  1930207,
                  1921146,
                  1921147,
                  1921148,
                  1921149,
                  1921150,
                  1921151,
                  1921152,
                  1921153,
                  1921154,
                  1921155,
                  1921156,
                  1921157,
                  1921158,
                  1921159,
                  1921160,
                  1921161,
                  1921162,
                  1921163,
                  1921164,
                  1921180,
                  1921181,
                  1921182,
                  1921184,
                  1921185,
                  1921186,
                  1921187,
                  1921188,
                  1921189,
                  1921190,
                  1921191,
                  1921192,
                  1921193,
                  1921194,
                  1921195,
                  1921196,
                  1921197,
                  1921198,
                  1921199,
                  1921200,
                  1921201,
                  1921202,
                  1921203,
                  1921204,
                  1930208,
                  1930209,
                  1930210,
                  1930211,
                  1930212,
                  1930213,
                  1930214,
                  1930215,
                  1930216,
                  1930217,
                  1930218,
                  1930219,
                  1930223,
                  1930224,
                  1930225,
                  1930227,
                  1930228,
                  1930229,
                  1930230,
                  1930226,
                  1921205,
                  1930231,
                  1930232,
                  1930233,
                  1930234,
                  1930242,
                  1930243,
                  1930253,
                  1930254,
                  1930255,
                  1930235,
                  1930240,
                  1930241,
                  1930236,
                  1930238,
                  1930239,
                  1930237,
                  1921206,
                  1930258,
                  1930259,
                  1930261,
                  1930262,
                  1930264,
                  1930265,
                  1930266,
                  1930267,
                  1930268,
                  1930269,
                  1930270,
                  1930271,
                  1930272,
                  1930273,
                  1930274,
                  1930275,
                  1930276,
                  1930277,
                  1930278,
                  1930279,
                  1930280,
                  1930281,
                  1930282,
                  1930283,
                  1930284,
                  1930285,
                  1930286,
                  1930287,
                  1930288,
                  1930289,
                  1930290,
                  1921207,
                  1930291,
                  1930292,
                  1930293,
                  1930294,
                  1930295,
                  1930296,
                  1930298,
                  1930299,
                  1930300,
                  1930301,
                  1930302,
                  1930316,
                  1930317,
                  1930318,
                  1930319,
                  1930320,
                  1930321,
                  1930322,
                  1930323,
                  1930399,
                  1930400,
                  1930401,
                  1930402,
                  1930403,
                  1930404,
                  1930405,
                  1921208,
                  1921209,
                  1921210,
                  1921212,
                  1921214,
                  1934194,
                  1934195,
                  1934196,
                  1934202,
                  1934203,
                  1934197,
                  1934204,
                  1934205,
                  1934206,
                  1934199,
                  1934200,
                  1934207,
                  1934208,
                  1934209,
                  1934210,
                  1934211,
                  1934212,
                  1934213,
                  1934201,
                  1921215,
                  1921216,
                  1934214,
                  1934215,
                  1934216,
                  1934217,
                  1934221,
                  1934218,
                  1934222,
                  1934219,
                  1934223,
                  1934220,
                  1934224,
                  1921218,
                  1921219,
                  1921220,
                  1921221,
                  1921222,
                  1921223,
                  1921224,
                  1921225)
    for title in title_link:
        parseUrl(url + str(title))

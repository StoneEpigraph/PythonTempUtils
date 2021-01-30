#! /usr/bin/env python3

import json

if __name__ == '__main__':
    json_str = '''
    {
    "result": true,
    "msg": null,
    "repairDictTypeModels": [
        {
            "id": "3da24cb2e5824ce1b6a45d83573d8277",
            "dictType": "ENTERPRISE_ECONOMY_TYPE",
            "value": "股份有限公司"
        },
        {
            "id": "165d4e4021b641859b8d624262a6abcb",
            "dictType": "ENTERPRISE_ECONOMY_TYPE",
            "value": "集体与私人联营企业"
        },
        {
            "id": "3c2d66e1f9f9427498b2f3ef259568bd",
            "dictType": "ENTERPRISE_ECONOMY_TYPE",
            "value": "国有集体与私人联营企业"
        },
        {
            "id": "861ca036a2ad4c31bd0bd048e884c2b8",
            "dictType": "ENTERPRISE_ECONOMY_TYPE",
            "value": "有限责任公司"
        },
        {
            "id": "a3ee85fa9cf9480e9a8926a1ed5638e0",
            "dictType": "ENTERPRISE_ECONOMY_TYPE",
            "value": "外资企业"
        },
        {
            "id": "958c7f746a5445e0bf120624f6662935",
            "dictType": "ENTERPRISE_ECONOMY_TYPE",
            "value": "中外合资经营企业"
        },
        {
            "id": "35e753484625477ba3f17b83d4d80bb2",
            "dictType": "ENTERPRISE_ECONOMY_TYPE",
            "value": "中外合作经营企业"
        },
        {
            "id": "bb092d4772904230bec11f7bd38fdcd6",
            "dictType": "ENTERPRISE_ECONOMY_TYPE",
            "value": "与大陆合作经营企业"
        },
        {
            "id": "9c7790efae9e4c109b48262a227f88e8",
            "dictType": "ENTERPRISE_ECONOMY_TYPE",
            "value": "与大陆合资经营企业"
        },
        {
            "id": "b6df801ef7ab4d7ebb4cd5e086cadad1",
            "dictType": "ENTERPRISE_ECONOMY_TYPE",
            "value": "港澳台独资企业"
        },
        {
            "id": "27b0f65e73b54e58a425b90e58fef1e9",
            "dictType": "ENTERPRISE_ECONOMY_TYPE",
            "value": "国有经济"
        },
        {
            "id": "642ce080ae4845f5b2e97683c3b3013f",
            "dictType": "ENTERPRISE_ECONOMY_TYPE",
            "value": "私营经济"
        },
        {
            "id": "c0891d47aad74a17a68daa1041441897",
            "dictType": "ENTERPRISE_ECONOMY_TYPE",
            "value": "集体经济"
        },
        {
            "id": "21a26fad6d8447e2b6209affe9279f7a",
            "dictType": "ENTERPRISE_ECONOMY_TYPE",
            "value": "个体经济"
        },
        {
            "id": "c0707bcf0b8b4eda8852a3f606fe27ea",
            "dictType": "ENTERPRISE_ECONOMY_TYPE",
            "value": "联营经济"
        },
        {
            "id": "6cb4a90d640e4290b7977bb2b9e432f8",
            "dictType": "ENTERPRISE_ECONOMY_TYPE",
            "value": "股份制经济"
        },
        {
            "id": "f50816d7871c4933b390d722f2928666",
            "dictType": "ENTERPRISE_ECONOMY_TYPE",
            "value": "外商投资经济"
        },
        {
            "id": "1df420d38120436bb2020f78efce5075",
            "dictType": "ENTERPRISE_ECONOMY_TYPE",
            "value": "港澳台投资经济"
        },
        {
            "id": "cefcacbd838f4d7dac6827ab10a67c6f",
            "dictType": "ENTERPRISE_ECONOMY_TYPE",
            "value": "其他经济"
        },
        {
            "id": "0206704e6f6e47e1895502f3a42e86e6",
            "dictType": "ENTERPRISE_ECONOMY_TYPE",
            "value": "国有企业"
        },
        {
            "id": "ab5fbab856a74a55b89628bb9c9a746f",
            "dictType": "ENTERPRISE_ECONOMY_TYPE",
            "value": "国有联营企业"
        },
        {
            "id": "e4cc90f764ef4b1cbb607675c60768a3",
            "dictType": "ENTERPRISE_ECONOMY_TYPE",
            "value": "集体企业"
        },
        {
            "id": "f34943a34a4241e68a8c26d22c995273",
            "dictType": "ENTERPRISE_ECONOMY_TYPE",
            "value": "集体联营企业"
        },
        {
            "id": "5bf7877f92b349b1af6471c67d6ce177",
            "dictType": "ENTERPRISE_ECONOMY_TYPE",
            "value": "私营独资企业"
        },
        {
            "id": "76c9ea169e6047e2968122673400b490",
            "dictType": "ENTERPRISE_ECONOMY_TYPE",
            "value": "私人合伙企业"
        },
        {
            "id": "fac3b491739c4b37aaec4b25ff0bdbf7",
            "dictType": "ENTERPRISE_ECONOMY_TYPE",
            "value": "私营有限责任公司"
        },
        {
            "id": "9b173e32e86f411a87fd8c38f34f49d2",
            "dictType": "ENTERPRISE_ECONOMY_TYPE",
            "value": "个体工商户"
        },
        {
            "id": "e17b41e7cc99497e9db4354f1f1cdb7d",
            "dictType": "ENTERPRISE_ECONOMY_TYPE",
            "value": "个人合伙"
        },
        {
            "id": "79937389b3764a73954601d3c44b408c",
            "dictType": "ENTERPRISE_ECONOMY_TYPE",
            "value": "国有与集体联营企业"
        },
        {
            "id": "5e2f04c1f2eb48ac9e33040db001f3c8",
            "dictType": "ENTERPRISE_ECONOMY_TYPE",
            "value": "国有与私人联营企业"
        },
        {
            "id": "d291916004644949b595df16d2d9d716",
            "dictType": "VOCATIONAL_SKILLS_EDUCATION_TYPE",
            "value": "无"
        },
        {
            "id": "f20bca1df8964223b227ef839eb5e6a7",
            "dictType": "VOCATIONAL_SKILLS_EDUCATION_TYPE",
            "value": "一级教练员"
        },
        {
            "id": "e31a16f302514862b05d9f074aaafcfd",
            "dictType": "VOCATIONAL_SKILLS_EDUCATION_TYPE",
            "value": "二级教练员"
        },
        {
            "id": "3082e5ef34f84848bf33b60088426338",
            "dictType": "VOCATIONAL_SKILLS_EDUCATION_TYPE",
            "value": "三级教练员"
        },
        {
            "id": "d4c5c441e11346b2959adac0b81db6b3",
            "dictType": "VOCATIONAL_SKILLS_EDUCATION_TYPE",
            "value": "四级教练员"
        },
        {
            "id": "437fe132c63e4938aa320cd0e9169790",
            "dictType": "VOCATIONAL_SKILLS_EDUCATION_TYPE",
            "value": "五级教练员"
        },
        {
            "id": "03480bb3fa974803b5c6197d5a0860e7",
            "dictType": "EDUCATION",
            "value": "研究生"
        },
        {
            "id": "6b05f3de175548c88bcdf9cb859f30fe",
            "dictType": "EDUCATION",
            "value": "博士后"
        },
        {
            "id": "d98b636f05194edc9950ff44356314d0",
            "dictType": "EDUCATION",
            "value": "小学"
        },
        {
            "id": "dadd3e6bd6d546eeb1f3404c06455047",
            "dictType": "EDUCATION",
            "value": "初中"
        },
        {
            "id": "99d14be2de494dfeb849304068ec1092",
            "dictType": "EDUCATION",
            "value": "高中"
        },
        {
            "id": "15f32877b0ab4681af5a221a0ff04332",
            "dictType": "EDUCATION",
            "value": "大专"
        },
        {
            "id": "4e00fd06954f4f9eb076fd74e9e58a38",
            "dictType": "EDUCATION",
            "value": "本科"
        },
        {
            "id": "360905347d91430a8e0b8ae99fa57f1a",
            "dictType": "EDUCATION",
            "value": "博士"
        },
        {
            "id": "bbb42d361bd34cd0b564c4ff45313a14",
            "dictType": "EDUCATION",
            "value": "其他"
        },
        {
            "id": "a337ae9d1ae14a128665ec82a4e3d068",
            "dictType": "EDUCATION",
            "value": "中专"
        },
        {
            "id": "37dee433f3124278bbc681f3b62890db",
            "dictType": "EDUCATION",
            "value": "职高"
        },
        {
            "id": "edbb7d0bd98143c789e4b8a1a76ab8bb",
            "dictType": "EDUCATION",
            "value": "职业技校"
        },
        {
            "id": "4700ee0524cf47868483628cce6a822c",
            "dictType": "TEACHING_VEHICLE_TYPE",
            "value": "大型客车A1"
        },
        {
            "id": "6caadcfd229d47f6971bcd253508d6d1",
            "dictType": "TEACHING_VEHICLE_TYPE",
            "value": "牵引车A2"
        },
        {
            "id": "0040fa0f8cbb48aba0c9e9dffb3c82c9",
            "dictType": "TEACHING_VEHICLE_TYPE",
            "value": "城市公交车A3"
        },
        {
            "id": "609dd3ff8ae44cf19d1e0a415384f617",
            "dictType": "TEACHING_VEHICLE_TYPE",
            "value": "中型客车B1"
        },
        {
            "id": "5f0a3fba24af4d9e982667f88e6ae328",
            "dictType": "TEACHING_VEHICLE_TYPE",
            "value": "大型货车B2"
        },
        {
            "id": "95523488f54c4d34a4f01ab15a4d93bb",
            "dictType": "TEACHING_VEHICLE_TYPE",
            "value": "小型汽车C1"
        },
        {
            "id": "f7b8bf48148d48e18f41fc8599e8d805",
            "dictType": "TEACHING_VEHICLE_TYPE",
            "value": "小型自动挡汽车C2"
        },
        {
            "id": "b34cec6aa6eb4cad96793d9049b8620f",
            "dictType": "TEACHING_VEHICLE_TYPE",
            "value": "低速载货汽车C3"
        },
        {
            "id": "5f21ee3316fd43d1bb7416b50813d3ea",
            "dictType": "TEACHING_VEHICLE_TYPE",
            "value": "三轮汽车C4"
        },
        {
            "id": "9966d33b6d1c48879920854b9fe0f9a2",
            "dictType": "TEACHING_VEHICLE_TYPE",
            "value": "残疾人专用小型自动挡载客汽车C5"
        },
        {
            "id": "0770098d24c248e1a67b2c0b613185d8",
            "dictType": "TEACHING_VEHICLE_TYPE",
            "value": "普通三轮摩托D"
        },
        {
            "id": "b9256f0dce674a77aba8d00e61c5eb94",
            "dictType": "TEACHING_VEHICLE_TYPE",
            "value": "普通两轮摩托车E"
        },
        {
            "id": "ba83154046a9425ba1e5f6592e9c212c",
            "dictType": "TEACHING_VEHICLE_TYPE",
            "value": "轻便摩托车F"
        },
        {
            "id": "05041056e50d4a168312b51267beb75d",
            "dictType": "TEACHING_VEHICLE_TYPE",
            "value": "轮式自行机械车M"
        },
        {
            "id": "5a2e0e20c9034d8c950794548c447355",
            "dictType": "TEACHING_VEHICLE_TYPE",
            "value": "无轨电车N"
        },
        {
            "id": "cfd6ee1ad5ff48c0acfac9faa32830c8",
            "dictType": "TEACHING_VEHICLE_TYPE",
            "value": "有轨电车P"
        },
        {
            "id": "1f875134b19748268ba212f9ab9a1433",
            "dictType": "TEACHING_TYPE",
            "value": "实操（兼理论）教练员"
        },
        {
            "id": "63777743802c420da1496ec1f4e5fbe9",
            "dictType": "TEACHING_TYPE",
            "value": "理论教练员"
        },
        {
            "id": "0dec6cf11d8c40d18c5c4d4d2aa11bb5",
            "dictType": "TEACHING_TYPE",
            "value": "实操教练员"
        },
        {
            "id": "ac23157c08ff49f68f5f3a07c0c03d16",
            "dictType": "TEACHING_TYPE",
            "value": "道路客货运输从业资格教练员"
        },
        {
            "id": "32970a0ea0bf4972b39a44f3f8824cc5",
            "dictType": "TEACHING_TYPE",
            "value": "危险货物运输从业资格教练员"
        }
    ]
}
    '''

    json_obj = json.loads(json_str)
    print(json_obj)
    repair_dict = json_obj['repairDictTypeModels']
    print(repair_dict)
    jd_type_arr = []
    jd_type_code_arr = []
    jd_type_name_arr = []
    for item in repair_dict:
        dict_type = item['dictType']
        if dict_type == 'ENTERPRISE_ECONOMY_TYPE':
            obj = {}
            obj['code'] = item['id']
            itemName = item['value']
            obj['name'] = itemName
            jd_type_arr.append(obj)
            jd_type_code_arr.append(item['id'])
            jd_type_name_arr.append(itemName)
            print(itemName)
    print(jd_type_arr)
    print(len(jd_type_arr))
    print(jd_type_code_arr)
    print(jd_type_name_arr)
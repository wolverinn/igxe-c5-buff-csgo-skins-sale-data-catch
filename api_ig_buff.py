import requests
import json

#################################### 筛选的皮肤及规则 #####################################
igxe_apis = ["3760","7089"]  #str
buff_apis = ["34066","34095"]  #str
price_restriction = [256,295]  #float
wear_restriction = [0.22,0.01]   # float
#####################################################################################

item_name = ""
def igxe_match(product_api,page,price,wear):
    ig_api = "https://www.igxe.cn/product/trade/730/" + product_api + "?page_no={}".format(str(page))
    api_request = requests.get(ig_api)
    if api_request.status_code is 200:
        data = api_request.json()
        try:
            page_count = data["page"]["page_count"]
        except:
            return 2
        item_list = data["d_list"]
        for item_detail in item_list:
            global item_name
            item_name = item_detail["name"]
            if float(item_detail["unit_price"]) > price:
                return 2
            try:
                item_float = float(item_detail["exterior_wear"])
            except:
                item_float = 1
            if item_float <= wear:
                print("{}   price:{}  wear:{}".format(item_name,item_detail["unit_price"],item_float))
    else:
        print("igxe api failed")
        return 0
    return 1

def buff_match(name,product_api,price,wear):
    buff_api = "https://buff.163.com/api/market/goods/sell_order?game=csgo&goods_id={}&page_num=1&page_size=100".format(product_api)
    api_request = requests.get(buff_api)
    if api_request.status_code is 200:
        data = api_request.json()
        item_list = data["data"]["items"]
        for item_detail in item_list:
            try:
                item_wear = item_detail["asset_info"]["paintwear"]
            except:
                item_wear = 1
            item_price = item_detail["price"]
            if float(item_price) > price:
                return 0
            if float(item_wear) <= wear:
                print("{}   price:{}  wear:{}".format(name,item_price,item_wear))
    else:
        print("buff api failed")
        return 0
    return 1


for i,ig_api in enumerate(igxe_apis):
    print("start checking igxe api:{} in igxe...".format(ig_api))
    for page in range(10):
        result = igxe_match(ig_api,int(page+1),price_restriction[i],wear_restriction[i])
        if result == 2:
            break
    print("start checking buff api:{} in buff...".format(buff_apis[i]))
    result = buff_match(item_name,buff_apis[i],price_restriction[i],wear_restriction[i])
    print("{} checked\n\n".format(item_name))
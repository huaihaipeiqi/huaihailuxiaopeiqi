import requests, app

# 获取验证码
response = requests.post(url='http://cjqa-docker.suanshubang.com/aduapp/v1/user/send/token',
                         headers={"Content-Type": "application/x-www-form-urlencoded"},
                         data={"os": "android", "saasClient": "1", "phone": "18235029151",
                               "productchannel": "2"})
print(response.text)
# 验证码登录
response = requests.post(url='http://cjqa-docker.suanshubang.com/aduapp/v1/user/login/smstoken',
                         headers={"Content-Type": "application/x-www-form-urlencoded"},
                         data={"os": "android", "saasClient": "1", "phone": "18235029151",
                               "code": "1111", "productchannel": "2"})
print(response.text)
# 获取cookie
dai = response.json().get("data").get("zybuss")
cookie = app.cookie + ";" + f'ZYBUSS={dai}'
app.HEaders["Cookie"] = cookie
print(app.HEaders)
# 获取用户信息
response = requests.post(url='http://cjqa-docker.suanshubang.com/aduapp/v1/user/info',
                         headers=app.HEaders)
print(response.text)
# 新手礼包
response = requests.post(url=app.URL + '/aduapp/v1/gift/newUser', headers=app.HEaders,)
print(response.text)
# 获取业务线
response = requests.post(url=app.URL + '/aduapp/v1/source/list', headers=app.HEaders)
print(response.text)
# 获取商品列表
response = requests.post(url=app.URL + '/aduapp/v1/goods/listnotype', headers=app.HEaders,
                         data={'productchannel': 3})  # 1 英语 2 财会 3 教资 4公考 5考研
# 请求体{’goodType‘：‘pval’}free 0元课 pval 系统课
print(response.text)
# 获取大纲信息
response = requests.post(url=app.URL + '/aduapp/v1/goods/outline', headers=app.HEaders,
                         data={'pruductchannel': 2, 'skuId': 10094934})
print(response.text)
# 获取商品详情
response = requests.post(url=app.URL + '/aduapp/v1/goods/detail', headers=app.HEaders,
                         data={'pruductchannel': 2, 'skuId': 10094934, 'spuId': 2018978})
print(response.text)
# 获取联报商品列表
response = requests.post(url=app.URL + '/aduapp/v1/goods/combination/list', headers=app.HEaders,
                         data={'productchannel': 1})
print(response.text)
# 获取联报商品详情
response = requests.post(url=app.URL + '/aduapp/v1/goods/combination/detail', headers=app.HEaders,
                         data={'productchannel': 1, 'goodsId': 202101076803})  # goodsId=商品id
print(response.text)
# 教师详情查询
response = requests.post(url=app.URL + '/aduapp/v1/teacher/getteachers', headers=app.HEaders,
                         data={'teacherUids': 2000170302, 'appId': 'chengrenjiaoyu', 'productchannel': 1})
print(response.text)
# 教师课程
response = requests.post(url=app.URL + '/aduapp/v1/teacher/courselist', headers=app.HEaders,
                         data={'teacherUid': 2000161807, 'productchannel': 4})
print(response.text)
# 获取sku状态
response = requests.post(url=app.URL + '/aduapp/v1/order/skustatus', headers=app.HEaders,
                         data={'productchannel': 1, 'skuId': 10101381, 'spuId': 2024812})
print(response.text)
# 订单详情
response = requests.post(url=app.URL + '/aduapp/v1/order/detail', headers=app.HEaders,
                         data={'orderId': 2101324412, 'productchannel': 1})
print(response.text)


# 预下单
response = requests.post(url='http://cjqa-docker.suanshubang.com/aduapp/v1/order/confirm', headers=app.HEaders,
                         data={'skuIdMap': '[{"skuId":10097274,"couponId":0}]', 'isRecommendCoupon': 1,
                               'productchannel': 1})
print(response.text)
# 提交订单
response = requests.post(url='http://cjqa-docker.suanshubang.com/aduapp/v1/order/submit', headers=app.HEaders,
                         data={'productchannel': 1, 'skuIdMap': '[{"skuId":10097274,"couponId":0}]',
                               'purchaseData': '{"skuList":{"10097274":{"skuId":10097274,"price":1,'
                                               '"prePrice":0,"discountPrice":0,"couponDiscountPrice":0,"costPrice":1,"couponId":null,"teamStId":0,"payTime":0}},'
                                               '"total":{"totalPrice":1,"totalOriginalPrice":1,"totalPrePrice":0,"totalDiscountPrice":0,"integralDiscountPrice":0},'
                                               '"useIntegralList":[],"bizInfo":{"bizVersion":201908,"giftInfoList":[],"discountBizMap":{}},"skuIdList":[10097274]}'})
print(response.text)
# 获取联报商品sku状态
response=requests.post(url='http://cjqa-docker.suanshubang.com/aduapp/v1/order/combination/skustatus',headers=app.HEaders,
                       data={'productchannel':1,'goodsList':'[{"spuId":2024812,"skuId":10101381},{"spuId":2024812,"skuId":10104848}]'})
print(response.text)
# 我的订单列表
response = requests.post(url=app.URL + '/aduapp/v2/order/list', headers=app.HEaders,
                         data={'page': 0, 'productchannel': 4, 'pageSize': 10, 'status': 0})
print(response.text)
# 每个订单的订单列表
response = requests.post(url=app.URL + '/aduapp/v2/order/onelist', headers=app.HEaders,
                         data={'orderChannel': 112, 'orderId': 2101343808, 'productchannel': 4})
print(response.text)
# 免费领取
response = requests.post(url=app.URL + '/aduapp/v1/order/free', headers=app.HEaders,
                         data={'skuId': 3010217, 'productchannel': 1})
print(response.text)

# 购买结果
response = requests.post(url=app.URL + '/aduapp/v1/order/result', headers=app.HEaders,
                         data={'orderId': 2101344139, 'productchannel': 1})
print(response.text)
# 取消订单
response = requests.post(url=app.URL + '/aduapp/v1/pay/status', headers=app.HEaders,
                         data={'orderId': 2101343980, 'productchannel': 4})
print(response.text)
# 支付参数
response = requests.post(url=app.URL + '/aduapp/v1/pay/sign', headers=app.HEaders,
                         data={'orderId': 2101344284, 'productchannel': 1, 'mode': 1, "source": 3})
print(response.text)
# 地址列表
response = requests.post(url=app.URL + '/aduapp/v1/address/list', headers=app.HEaders)
print(response.text)
# 更新保存地址
response = requests.post(url=app.URL + '/aduapp/v1/address/save', headers=app.HEaders,
                         data={'orderId': 2101344284, 'phone': 15542553565,'name':'阿萨大大',
                               'province': '北京', "city": '北京市', 'prefecture': '东城区', 'town': '景山街道',
                               'address': '复古风广告费', 'isDefault': 1, 'uid': 2135317188,
                               'addressId': 250})  # addressId更新地址时必传  新增时传0
print(response.text)
# 新增保存地址
response = requests.post(url=app.URL + '/aduapp/v1/address/save', headers=app.HEaders,
                         data={"addressId": 0, "name": "瑞福德发", "phone": "15542553565", "province": "北京", "city": "北京市",
                               "prefecture": "东城区", "town": "景山街道", "address": "复古风广告费权威", "isDefault": 1,
                               "uid": 2135317188,'productchannel':1})  # addressId更新地址时必传  新增时传0
print(response.text)
# 地址详情
response = requests.post(url=app.URL + '/aduapp/v1/address/detail', headers=app.HEaders,
                         data={"addressId": 250})
print(response.text)
#优惠券
response = requests.post(url=app.URL + '/aduapp/v1/coupon/list', headers=app.HEaders,
                         data={"status": 1,'page':0,'pageSize':10,'productchannel':4})
print(response.text)
#用户订单地址待办事项
response = requests.get(url=app.URL + '/aduapp/v1/order/addrlost', headers=app.HEaders)
print(response.text)
#退出
response = requests.post(url=app.URL + '/session/submit/logout', headers=app.HEaders)
print(response.text)

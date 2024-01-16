# flake8: noqa
PAYMENT_DOCS = """
一、支付系统用户信息查询，用户银行卡信息查询
支付系统用户信息查询是一个简单的HTTP接口，根据用户输入的身份证号identity_card或者姓名real_name，查询用户的详细信息和用户的银行卡信息

用户信息查询API服务地址：
URL : http://127.0.0.1:8080/aiapi/member/GetUserInfo?real_name=<姓名>
URL : http://127.0.0.1:8080/aiapi/member/GetUserInfo?identity_card=<身份证号>
请求方式:GET

请求参数说明
real_name：代表姓名。为字符串
identity_card：代表身份证号，一般为数字开头

返回结果是一个json字符串，参数说明如下：
"success": 状态说明，不为true说明请求失败
"data": 返回的数据json
    "id": 用户id
    "platform_id":用户平台id
    "realname": 姓名
    "identity_no": 身份证
    "mobile": 电话号码
    "address": 地址
    "gender": 性别，0代表男，1代表女，2代表未定义
    "id_indate": 身份证到期日期
    "bank_info":为银行信息数组
			{
				"bank_type": 银行类型
				"bank_card": 卡类型
				"bank_provinc":开户省
				"bank_city": 开户城市
				"bank_open": 开户行
				"bank_no": 银行卡号
				"binding_mobile":绑定手机号
				"bank_pic_a":银行卡正面图片地址 
				"bank_pic_b":银行卡反面图片地址
			},

请求示例
1、http://127.0.0.1:8080/aiapi/member/GetUserInfo?real_name=奥托夫斯基
1、http://127.0.0.1:8080/aiapi/member/GetUserInfo?identity_card=3522000198656542365

二、支付系统渠道信息列表
支付系统渠道信息列表是一个简单的HTTP接口，可以列出当前支付系统支持的所有渠道。

渠道信息列表API服务地址：
URL : http://127.0.0.1:8080/aiapi/member/GetPayterm
请求方式:GET

请求参数说明
不需要任何参数

返回结果参数说明
"success": true,  //状态说明，不为true说明请求失败
"data": 返回的渠道列表数据    

请求示例
1、http://127.0.0.1:8080/aiapi/member/GetPayterm
"""
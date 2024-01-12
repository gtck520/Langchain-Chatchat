# flake8: noqa
TEST_DOCS = """
天气查询
天气查询是一个简单的HTTP接口，根据用户输入的adcode，查询目标区域当前/未来的天气情况，数据来源是中国气象局。

天气查询API服务地址：
URL : https://restapi.amap.com/v3/weather/weatherInfo?parameters
请求方式:GET

parameters-代表的参数包括必填参数和可选参数。所有参数均使用和号字符(&)进行分隔。下面的列表枚举了这些参数及其使用规则。 

请求参数,参数名含义,规则说明,是否必须,缺省值
key,请求服务权限标识,用户在高德地图官网申请web服务API类型KEY,必填,无
city,城市编码,输入城市的adcode，adcode信息可参考城市编码表,必填,无
extensions,气象类型,可选值：base/all base:返回实况天气all:返回预报天气,可选,无
output,返回格式,可选值：JSON,XML,可选,JSON

返回结果参数说明
实况天气每小时更新多次，预报天气每天更新3次，分别在8、11、18点左右更新。由于天气数据的特殊性以及数据更新的持续性，无法确定精确的更新时间，请以接口返回数据的reporttime字段为准。天气结果对照表>>

名称,含义,规则说明
status,返回状态,值为0或1 1：成功；0：失败
count,返回结果总数目,info,返回的状态信息
infocode,返回状态说明,10000代表正确
lives,实况天气数据信息
province,省份名
city,城市名
adcode,区域编码
weather,天气现象（汉字描述）
temperature,实时气温，单位：摄氏度
winddirection,风向描述
windpower,风力级别，单位：级
humidity,空气湿度
reporttime,数据发布的时间
forecast,预报天气信息数据
city,城市名称
adcode,城市编码
province,省份名称
reporttime,预报发布时间
casts
预报数据list结构，元素cast,按顺序为当天、第二天、第三天的预报数据
date,日期
week,星期几
dayweather,白天天气现象
nightweather,晚上天气现象
daytemp,白天温度
nighttemp,晚上温度
daywind,白天风向
nightwind,晚上风向
daypower,白天风力
nightpower,晚上风力

请求示例
https://restapi.amap.com/v3/weather/weatherInfo?city=110101&key=56bb5fa893b59525765b9bd032dc646a
参数	值	  备注	     必选
city  110101 需要查询天气的城市编码。	否"""

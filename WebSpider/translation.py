import urllib.request
import urllib.parse
import json

#content = input("请输入需要翻译的内容：")
url = "http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule&sessionFrom="
data = {}
#data['i'] = content
data['i'] = 'I love FishC.com'
data['from'] = 'AUTO'
data['to'] = 'AUTO'
data['smartresult'] = 'dict'
data['client'] = 'fanyideskweb'
data['salt'] = '1511765483389'
data['sign'] = 'f06f61694cf40c88620f2a9ccc2c5f02'
data['doctype'] = 'json'
data['version'] = '2.1'
data['keyfrom'] = 'fanyi.web'
data['action'] = 'FY_BY_CLICKBUTTION'
data['typoResult']= 'false'

response = urllib.request.urlopen(url,data)
html = response.read().decode('utf-8')
print(html)
#target = json.load(html)
#print("翻译结果：%s" % (target['translateResult'][0][0]['tgt']))



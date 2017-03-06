import requests
import json
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36"}

url = "http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule&smartresult=ugc&sessionFrom=https://www.baidu.com/link"

content = input("Contnent : ")

data = {
        "type":"AUTO",
        "i":content,
        "doctype":"json",
        "xmlVers/ion":"1.8",
        "keyfrom":"fanyi.web",
        "ue":"UTF-8",
        "action":"FY_BY_ENTER",
        "typoResult":"true"
        }

req = requests.post(url,headers=headers,data=data)
jd = json.loads(req.text)
try:
        translateResult = jd["translateResult"][0][0]["tgt"]
        smartResult = jd["smartResult"]["entries"]
        print("translateResult : %s " % translateResult)
        print("smartResult : ")
        for i in smartResult[1:]:
                print(i)
        input("任意键继续...")
except KeyError:
        print("Error: 无法查询!")
        input("任意键继续...")

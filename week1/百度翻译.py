import requests
import json

response = requests.get("https://www.baidu.com")

response.encoding = 'utf8'
print(response.text)


print(response.content.decode())


r = requests.get('https://www.baidu.com/img/baidu_resultlogo@2.png')

f = open("baidu.png",'wb')
f.write(r.content)
f.close()





headers = {'User-Agent':'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Mobile Safari/537.36'}

res = requests.post(url = 'https://fanyi.baidu.com/basetrans',headers =headers,data={'query': '请问','from': 'zh','to': 'en','token': '8ad2df927d4fa7221ee6768c285d3734','sign': '347496.110169'})

json_str = res.content.decode()
print(json_str)
dicesr = json.loads(json_str)
print(dicesr)
result = dicesr["data"]['st_tag']
print(result)


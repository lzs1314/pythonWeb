import requests
from lxml import etree

url = 'http://www.stat-nba.com/query_award.php'

headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Cache-Control': 'max-age=0',
    'Connection': 'keep-alive',
    'Cookie': '__cfduid=d2b137a653986c37d5dd53e74ef76948c1551857064; Hm_lvt_102e5c22af038a553a8610096bcc8bd4=1551857065; yjs_id=f3f2b4573964610daf72b46cbe40d555; ctrl_time=1; Hm_lpvt_102e5c22af038a553a8610096bcc8bd4=1551857080',
    'Host': 'www.stat-nba.com',
    'Referer': 'http://www.stat-nba.com/',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36'
}

for i in range(0, 11):
    url = 'http://www.stat-nba.com/query_award.php?page=%d%#label_show_result'
    response = requests.get(url=url, headers=headers).content.decode('utf-8')
    tree = etree.HTML(response)
    tr_list = tree.xpath('//tbody/tr')
    for tr in tr_list:
        # 姓名
        name = tr.xpath('./td[2]/a/text()')
        time = tr.xpath('./td[5]/text()')
        lan = tr.xpath('./td[15]/text()')
        zhu = tr.xpath('./td[18]/text()')
        de = tr.xpath('./td[23]/text()')

        nba = name[0] + ',' + time[0] + ',' + lan[0] + ',' + zhu[0] + ',' + de[0] + '\n'
        # print(nba)
        with open('NBA数据.text', 'a', encoding='utf-8') as f:
            f.write(nba)

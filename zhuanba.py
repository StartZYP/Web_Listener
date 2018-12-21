import requests
from lxml import etree
import time


def GetZhuanbaNewTitle():
    response = requests.get('http://www.zuanke8.com/forum.php?mod=forumdisplay&fid=15&filter=author&orderby=dateline&typeid=14')
    etreeobj = etree.HTML(response.text)
    newUrl = etreeobj.xpath('/html[1]/body[1]/div[3]/div[5]/div[7]/div[1]/div[1]/div[4]/div[2]/form[1]/table[1]/tbody[3]/tr[1]/th[1]/a/@href')[0]
    newTitle = etreeobj.xpath('/html[1]/body[1]/div[3]/div[5]/div[7]/div[1]/div[1]/div[4]/div[2]/form[1]/table[1]/tbody[3]/tr[1]/th[1]/a/text()')[0]
    newUrl = newUrl.replace('&extra=page%3D1%26filter%3Dauthor%26orderby%3Ddateline%26typeid%3D14%26typeid%3D14%26orderby%3Ddateline','')
    return newTitle,newUrl

def addzhuanbasqldata(newTitle, newUrl):
    data={
        'type':'add',
        'WebTitle':newTitle,
        'WebUrl':newUrl,
        'Webtype':'赚客吧'
    }
    requests.post('http://65.49.231.185/NewMsg/NewMsg.php',data=data)

if __name__ == '__main__':
    ZhuanbaTempNewTitl = ""
    while True:
        newTitle, newUrl = GetZhuanbaNewTitle()
        if ZhuanbaTempNewTitl!=newTitle:
            ZhuanbaTempNewTitl = newTitle
            addzhuanbasqldata(newTitle,newUrl)
            print('检测到有新线报'+ '\n' +newTitle + '\n' + newUrl)
        else:
            time.sleep(10)
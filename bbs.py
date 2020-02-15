import requests
from bs4 import BeautifulSoup
import re
from urllib.request import urlretrieve

url = 'https://www.ptt.cc/bbs/C_Chat/index.html'
reg_imgur_file = re.compile('http[s]?://[i.]*imgur.com/\w+\.(?:jpg|png|gif)')#get photo
for round in range(3):
    res = requests.get(url)
    soup = BeautifulSoup(res.text, 'html.parser')
    articles = soup.select('div.title a')
    paging = soup.select('div.btn-group-paging a')#下一頁的網址連結
    next_url = 'https://www.ptt.cc'+ paging[1]['href']#上一頁在第二行
    url = next_url
    for articles in articles:
        print(articles.text, articles['href'])#抓到標題及連結
        res = requests.get('https://www.ptt.cc'+articles['href'])
        images = reg_imgur_file.findall(res.text)
        print(images)
        for image in set(images):#刪掉重複的
            ID = re.search('http[s]?://[i.]*imgur.com/(\w+\.(?:jpg|png|gif))',image).group(1)
            print(ID)

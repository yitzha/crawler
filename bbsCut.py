#https://www.youtube.com/watch?v=q317e-0jwZY&list=PLS6ActuqbfA2bSOZV35MVpsVFvd6xxlzn&index=21
import requests
from bs4 import BeautifulSoup
import re
from urllib.request import urlretrieve
import os

def download_image(articles):
    for article in articles:
        print(article.text, article['href'])#抓到標題及連結
        #文章標題+資料夾
        if not os.path.isdir(os.path.join('download', article.text)):
            os.mkdir(os.path.join('download', article.text))
        res = requests.get('https://www.ptt.cc'+article['href'])
        images = reg_imgur_file.findall(res.text)
        print(images)
        for image in set(images):#刪掉重複的
            ID = re.search('http[s]?://[i.]*imgur.com/(\w+\.(?:jpg|png|gif))',image).group(1)
            print(ID)
            urlretrieve(image, os.path.join('download', article.text, ID))
def crawler():
    #建資料夾，先確認資料夾是否存在
    if not os.path.isdir('download'):
        os.mkdir('download')
    url = 'https://www.ptt.cc/bbs/C_Chat/index.html'
    for round in range(3):
        res = requests.get(url)
        soup = BeautifulSoup(res.text, 'html.parser')
        articles = soup.select('div.title a')
        paging = soup.select('div.btn-group-paging a')#下一頁的網址連結
        next_url = 'https://www.ptt.cc'+ paging[1]['href']#上一頁在第二行
        url = next_url
        download_image(articles)
reg_imgur_file = re.compile('http[s]?://[i.]*imgur.com/\w+\.(?:jpg|png|gif)')#get photo
crawler()

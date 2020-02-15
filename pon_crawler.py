#抓取PTT電影版網頁原始碼
import urllib.request as req
url = "https://www.ptt.cc/bbs/movie/index.html"
#建立一個Request 物件，附加 Header的資訊
request = req.Request(url, headers={
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36"
})
with req.urlopen(request) as response:
    data = response.read().decode("utf-8")
#print(data)
#解析原始碼，獲得標題
import bs4
root = bs4.BeautifulSoup(data, "html.parser")
titles = root.find_all("div", class_="title")#尋找class=title的div標籤
#print(titles)
for title in titles:
    if  title.a != None:
        print(title.a.string)


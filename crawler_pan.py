import pandas
dfs = pandas.read_html('https://rate.bot.com.tw/xrt?Lang=zh-TW')

#拿掉不相關的
currency = dfs[0]
#用typr得到是dataFrame
currency =currency.iloc[:, 0:5]#根據index取得前五欄
#修正欄為名稱
currency.columns = [u'幣別',u'現金-本行買入', u'現金-本行賣出',u'即期-本行買入',u'即期-本行賣出']
#幣別重複表達，抽取出來
currency[u'幣別'] = currency[u'幣別'].str.extract('\((\w+)\)')#抽出:英文字出現一次以上
currency.to_excel('currency.xlsx')
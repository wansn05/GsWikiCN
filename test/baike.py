from bs4 import BeautifulSoup
import urllib.request
import urllib.parse

zh = input("输入百科对象：")
wiki = urllib.parse.quote(zh)
url = "https://baike.baidu.com/item/" + wiki
response = urllib.request.urlopen(url)  # 访问并打开url
html = response.read()  # 创建html对象读取页面源代码

soup = BeautifulSoup(html, 'html.parser')  # 创建soup对象，获取html代码

title = soup.find_all('dt', class_="basicInfo-item name")  # 找到所有dt标签，返回一个列表
node = soup.find_all('dd', class_="basicInfo-item value")  # 找到所有dd标签，返回一个列表

allunivinfo = []
titlelist = []
infolist = []

for i in title:  # 将所有dt标签内容存入列表
    title = i.get_text()
    titlelist.append(title)
for i in node:  # 将所有dd标签内容存入列表
    info = i.get_text()
    infolist.append(info)
for i, j in zip(titlelist, infolist):  # 多遍历循环，zip()接受一系列可迭代对象作为参数，将对象中对应的元素打包成一个个tuple（元组），然后返回由这些tuples组成的list（列表）。
    info = ''.join((str(i)+':'+str(j)).split())
    allunivinfo.append(info)
print(allunivinfo)
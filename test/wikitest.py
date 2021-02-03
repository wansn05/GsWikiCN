from bs4 import BeautifulSoup
import urllib.request
import urllib.parse

zh = input("输入wiki对象：")
wiki = urllib.parse.quote(zh)
url = "https://wiki.biligame.com/ys/" + wiki

response = urllib.request.urlopen(url)  # 访问并打开url
html = response.read()  # 创建html对象读取页面源代码

soup = BeautifulSoup(html, 'html.parser')  # 创建soup对象，获取html代码

test = soup.find('table')

title = soup.find('table').find_all('th')
node = soup.find('table').find_all('td')


allunivinfo = []
titlelist = []
infolist = []

for i in title:
    title = i.get_text()
    titlelist.append(title)
for i in node:
    info = i.get_text()
    infolist.append(info)
for i, j in zip(titlelist, infolist):  # 多遍历循环，zip()接受一系列可迭代对象作为参数，将对象中对应的元素打包成一个个tuple（元组），然后返回由这些tuples组成的list（列表）。
    info = ''.join((str(i)+':'+str(j)).split())
    allunivinfo.append(info)

for i in range(0,10):
    if i <= 3:
        print(infolist[i])
    elif i == 4:
        continue
    else:
        print(infolist[i])
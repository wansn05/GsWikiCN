from bs4 import BeautifulSoup
import urllib.request
import urllib.parse
import re

code = "5"

url = "https://bbs.mihoyo.com/ys/obc/channel/map/" + code + "?bbs_presentation_style=no_header"
response = urllib.request.urlopen(url)  # 访问并打开url
html = response.read()  # 创建html对象读取页面源代码

soup = BeautifulSoup(html, 'html.parser')  # 创建soup对象，获取html代码

list = soup.find_all('li', {"class": "position-list__item"})

titlelist = []
urllist = []
allist = []

i = 1
for i in range(len(list)):
    item = str(list[i])
    url = re.findall('"href="(.*)" t', item, re.S)
    title = re.findall('title="(.*)">', item, re.S)
    titlelist.append(title)
    urllist.append(url)
    print(titlelist)
    i += 1

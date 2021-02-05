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

TitleList = []
ImageUrlList = []
DetailedUrlList = []
# alList = []

for i in range(len(list)):
    item = str(list[i])
    ImageUrl = re.findall('data-src="(.*)\?x-oss-process=image/quality,q_75/resize,s_20"/>', item, re.S)  # MingxuanGame:修复阴间url + 增加图片信息url
    DetailedUrl = re.findall('href="(.*)" t', item, re.S)  # MingxuanGame:增加详细信息url
    title = re.findall('title="(.*)">', item, re.S)
    TitleList.append(title)
    ImageUrlList.append(ImageUrl)
    DetailedUrlList.append("https://bbs.mihoyo.com/" + DetailedUrl[0])
print(TitleList)
print(ImageUrlList)
print(DetailedUrlList)

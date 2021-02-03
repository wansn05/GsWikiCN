# -*- coding:utf-8 -*-
#python 2.7
#XiaoDeng
#http://tieba.baidu.com/p/2460150866
#抓取图片地址


from bs4 import BeautifulSoup
import urllib.request


html_doc = "http://tieba.baidu.com/p/2460150866"
req = urllib.request.Request(html_doc)  
webpage = urllib.request.urlopen(req)  
html = webpage.read()


soup = BeautifulSoup(html, 'html.parser')


#抓取图片地址
#抓取img标签且class为BDE_Image的所有内容
img_src=soup.findAll("img",{'class':'BDE_Image'})
for img in img_src:
    img=img.get('src')   #抓取src
    print(img)

print(img_src)
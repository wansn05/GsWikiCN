from bs4 import BeautifulSoup
import urllib.request
import urllib.parse
import re

unsupport = ['纪行', '祈愿', '冒险等阶']


# 无法解析的wiki页面.

def format_result(zh):
    name = urllib.parse.quote(zh)
    url = "https://wiki.biligame.com/ys/" + name
    if zh in unsupport:
        return "无法解析该页面，请自行点击如下链接查看:{}".format(url)
    try:
        response = urllib.request.urlopen(url)
        html = response.read()
        soup = BeautifulSoup(html, 'html.parser')

        th = soup.find('table').find_all('th')
        td = soup.find('table').find_all('td')
        s_img = soup.find('table').find('img')

        thlist = []  # 第一列
        tdlist = []  # 第二列

        for i in th:
            th = i.get_text()
            thlist.append(th)
        for i in td:
            td = i.get_text()
            tdlist.append(td)
        # 将标签内容加入列表

        if thlist[5] == "元素属性\n":  # 判定百科内容是否为角色,并判定角色星级
            star = ""
            mz = tdlist[1].replace('\n', '')

            if s_img.get('src') == "https://patchwiki.biligame.com/images/ys/c/c7/qu6xcndgj6t14oxvv7yz2warcukqv1m.png":
                star = "5星"
            elif s_img.get('src') == "https://patchwiki.biligame.com/images/ys/9/9c/sklp02ffk3aqszzvh8k1c3139s0awpd.png":
                star = "4星"
            else:
                star = "未知星级"

            return "名称:{}({})\n称号:{}".format(mz, star, tdlist[0])  # bwiki的玄学逻辑，先称号后全名
        elif thlist[1] == "稀有度\n":  # 判定百科内容是否为资源,并判定资源星级
            return "资源"
        else:
            return "无法解析该wiki页面\n将在未来的数个版本内更新。"
        # if re.match(pattern, string, flags=0) = True:
    except urllib.error.HTTPError as e:  # 错误参数处理
        if e.reason == "Not Found":
            return "找不到这个词条"

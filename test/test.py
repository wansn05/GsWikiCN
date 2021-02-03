import re

def getContent():
    html = '''
    <tr>
        <th>性別：</th>
        <td>男</td>
    </tr>
    '''
    print(html)
    # 正则表达式获取<tr></tr>之间内容
    res_tr = r'<tr>(.*?)</tr>'
    m_tr = re.findall(res_tr, html, re.S | re.M)
    for line in m_tr:
        print(line)
        # 获取表格第一列th 属性
        res_th = r'<th>(.*?)</th>'
        m_th = re.findall(res_th, line, re.S | re.M)
        for mm in m_th:
            # 默认end='\n'
            print(mm, end='')
        # 获取表格第二列td 属性值
        res_td = r'<td>(.*?)</td>'
        m_td = re.findall(res_td, line, re.S | re.M)
        for nn in m_td:
            print(nn)


def getAttribute():
    html = '''
    <td> 
        <a href="https://www.baidu.com/articles/zj.html" title="浙江省">浙江省主题介绍</a> 
        <a href="https://www.baidu.com//articles/gz.html" title="贵州省">贵州省主题介绍</a> 
    </td> 
    '''
    # 获取链接属性方法1
    print(re.findall(r'<a href="(.*?)".*?</a>', html))

    # 获取链接属性方法2
    # ?<= 之前 的字符串内容需要匹配表达式才能成功匹配
    # ?=  之后 的字符串内容需要匹配表达式才能成功匹配
    print(re.findall(r'(?<=href=\").+?(?=\")', html))


if __name__ == '__main__':
    getContent()
    getAttribute()
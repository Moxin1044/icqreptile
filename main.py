import requests
import re
from bs4 import BeautifulSoup
from distutils.filelist import findall

# url config
u = "https://bbs.ichunqiu.com/portal.php"
u0 = "https://bbs.ichunqiu.com/"
d = "200"
a = ""


def rhook(u1):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36',
        'Host': 'bbs.ichunqiu.com',
    }
    s = requests.get(u1, headers=headers)
    if s.status_code == 200:
        return s.text
    else:
        return "访问失败"


# 获取最新文章
def parsing(page):
    soup = BeautifulSoup(page, "html.parser")
    print("--i春秋社区最新文章--")
    i = 0
    text1=""
    for tag in soup.find_all('div', class_='ui_2_ul_li_con'):
        # m_name = tag.find('a', class_='ui_colorG').get_text()
        i = i + 1
        m_name = tag.find('a', class_='ui_colorG').get_text()
        # m_rating_score = tag.find('div', class_='renshu').get_text() # 围观人数
        m_url = tag.find('a').get('href')
        # m_people = tag.find('a', style="color: #F35B4F;").get_text()
        # print(m_name + "\n" + u + m_url + " " + m_people + "\n围观人数：" + m_rating_score) #已经移动到下一行
        # text1 = text1 + "\n" + m_name + "\n" + u + m_url + " " + m_people + "\n围观人数：" + m_rating_score #空格太大
        text1 = text1 + m_name + "\n" + u0 + m_url  + "\n\n"
        # 此处输出前六个页面的数据
        if i == 10:
            print(text1 )
            return text1
            break


with open("wz.txt", "w") as f:
    f.write(parsing(rhook(u)))
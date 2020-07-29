# -*- coding:utf-8 -*-

from bs4 import BeautifulSoup
import requests
import re

def get_page():
    url = "https://item.jd.com/36854432733.html"
    headers = {
        "User-Agent":"Mozilla/4.0 (compatible;MSIE 7.0;Windows NT 5.1;360SE)"
    }
    reponse = requests.get(url,headers=headers)
    if reponse.status_code == 200:
        return reponse.text
    return None

def prase_page(html):
    soup = BeautifulSoup(html,'html.parser')
    print(soup.select('.sku-name'))
    title = soup.select('.sku-name')[0]
    
    if not title.string is None:
        title = title.string.strip()

    price_url = "https://p.3.cn/prices/mgets?skuIds=J_36854432733"
    url_session = requests.Session()
    price_req = url_session.get(price_url).text
    price = re.findall(r'"p":"(.*?)"', price_req)

    appraise_url = "https://sclub.jd.com/comment/productPageComments.action?&productId=36854432733&score=0&sortType=5&page=0&pageSize=10&isShadowSku=0&fold=1"
    appraise_session = requests.Session()
    appraise_req = appraise_session.get(appraise_url).text
    appraise = re.findall(r'"goodRateShow":(\d+),.*', appraise_req)

    print(title)
    print(price[0])
    print(appraise[0])

#   for tag in soup.find_all('div',class_='itemInfo-wrap'):
#       title = tag.find('div',class_='sku-name').get_text()
# #     price = tag.find('span',class_='price J-p-3133817').get_text()
#       p_price = tag.find('div',class_='dd')
#       p_span = p_price.findAll('span')
#       price = p_span[0].contents[1]
#       print(price)

html = get_page()
prase_page(html)
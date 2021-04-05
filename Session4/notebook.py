import requests
from bs4 import BeautifulSoup
import csv

file = open('notebook.csv', mode='w', newline='')
writer = csv.writer(file)
writer.writerow(["상품 제품명", "상품 가격명", "상품 상세설명"])  #엑셀 파일의 첫 번째 줄을 어떻게 작성하겠다.


# 우리가 정보를 얻고 싶어 하는 URL
NOTEBOOK_URL = f'https://search.shopping.naver.com/search/all?pagingIndex=1&pagingSize=80&query=노트북'
# get 요청을 통해 해당 페이지 정보를 저장
notebook_html = requests.get(NOTEBOOK_URL)
# bs4 라이브러리를 통해 불러온 html을 우리가 원하는 형태로 파싱
notebook_soup = BeautifulSoup(notebook_html.text,"html.parser")


notebook_list_box = notebook_soup.find('ul', {'class' :'list_basis'}) #클래스, 클래스명 find = 가장 먼저 매칭되는 첫 번째 태그
notebook_items = notebook_list_box.find_all('li', {'class':'basicList_item__2XT81'}) #많은 태그를 다 가져오고 싶다.
# print(notebook_items)

# print(len(notebook_items))
# print(type(notebook_items))
# print(notebook_items[0]) #첫번째 노트북
notebook_list = notebook_list_box.find_all('li', {'class':'basicList_item__2XT81'})
title = notebook_list[0].find("div", {"class" : "basicList_title__3P9Q7"}).find("a").string
#.string 안 쓰면 a 태그 전체가 추출됨. = .text
# print(title)

price = notebook_list[0].find("div", {"class" : "basicList_price_area__1UXXR"}).find("span", {"class": "price_num__2WUXn"}).string


details = []
# details = notebook_list[0].find("div", {"class" : "basicList_desc__2-tko"}).find("a", {"class": "basicList_detail__27Krk"}).string

detail = notebook_list[0].find_all("a", {"class" : "basicList_detail__27Krk"}) #find_all이라 string아니고 배열 됨.


temp = []


# for detail_item in detail:
#     temp.append(detail_item.text)

final_result = []   #정보 가공 최종.
for notebook_item in notebook_list:
    title = notebook_item.find("div", {"class" : "basicList_title__3P9Q7"}).find("a").string
    price = notebook_item.find("div", {"class" : "basicList_price_area__1UXXR"}).find("span", {"class": "price_num__2WUXn"}).string
    detail = notebook_item.find_all("a", {"class" : "basicList_detail__27Krk"}) #find_all이라 string아니고 배열 됨.

    temp = []

    for detail_item in detail:
        temp.append(detail_item.text)

    result = {
    'title' : title,
    'price' : price,
    'detail' : temp
    }

    final_result.append(result)


for result in final_result:
    row =[]
    row.append(result['title'])
    row.append(result['price'])
    row.append(result['detail'])
    writer.writerow(row)

    
print(final_result)



import requests
from bs4 import BeautifulSoup
import re
from movie_f import extract_info
import csv

file = open('movie_info.csv', mode='w', newline='')
writer = csv.writer(file)
writer.writerow(["img URL", "Title", "Rating", "Director", "Actors", "Release_Date"])

movie_URL = f'https://movie.naver.com/movie/running/current.nhn'
movie_html = requests.get(movie_URL)
movie_soup = BeautifulSoup(movie_html.text, "html.parser")
movie_list_box = movie_soup.find("ul", {"class":"lst_detail_t1"})
movie_elements = movie_list_box.find_all("li")

final_result = extract_info(movie_elements)

for result in final_result:
    row = []
    row.append(result['img'])
    row.append(result['title'])
    row.append(result['rate'])
    row.append(result['director'])
    row.append(result['actors'])
    row.append(result['release'])
    
    writer.writerow(row)

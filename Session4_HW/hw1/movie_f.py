import requests
from bs4 import BeautifulSoup
import re

def extract_info(movie_elements):
    result = []
    for movie_element in movie_elements:
        title = movie_element.find("dt", {"class":"tit"}).find("a").text
        rate= movie_element.find("div", {"class":"star_t1"}).find("span", {"class":"num"}).text
        img = re.search('(src=")(.+)"', str(movie_element.find("div", {"class":"thumb"}).find("img"))).group(2)
        
        other_texts = movie_element.find("dl", {"class":"info_txt1"}).find_all("dd")
        release = re.search('(\s)([\d.]+)(\s)', other_texts[0].text).group(2)
        director = other_texts[1].find("a").text
        
        if len(other_texts) >=3:
            actors_list = []
            actors_text = (other_texts[2].text).strip().split(',')
            for actor in actors_text:
                actors_list.append(actor.strip())
            actors = ', '.join(actors_list)
        else:
            actors = None
        
        movie_info = {
            'img' : img,
            'title' : title,
            'rate' : rate,
            'director' : director,
            'actors' : actors,
            'release' : release
        }

        result.append(movie_info)
    
    return result



        

    
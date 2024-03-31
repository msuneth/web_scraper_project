import requests
from bs4 import BeautifulSoup

#URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"
URL = "https://www.empireonline.com/movies/features/best-movies-2/"

# Write your code below this line 👇
response = requests.get(URL)
web_page = response.text
soup = BeautifulSoup(web_page,'html.parser')
#article_span_tag = soup.find_all('span', class_='titleline')
movie_titles = soup.find_all('h3', class_='listicleItem_listicle-item__title__BfenH')
with open("movie_list.txt","w") as file:
    for movie in movie_titles:
        file.writelines(movie.getText()+"\n")
        print(movie.getText())


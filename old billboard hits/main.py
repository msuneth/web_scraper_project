import requests
from bs4 import BeautifulSoup

time_travel_date = input("Which year do you want to travel to?Type date in this format YYYY-MM-DD:")
print(time_travel_date)

#URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"
URL = f"https://www.billboard.com/charts/hot-100/{time_travel_date}/"
print(URL)

# Write your code below this line 👇
response = requests.get(URL)
web_page = response.text
soup = BeautifulSoup(web_page,'html.parser')
print(web_page)
from bs4 import BeautifulSoup

with open("website.html",encoding="utf-8") as file:
    content = file.read()

soup = BeautifulSoup(content,'html.parser')
print(soup.title)
print(soup.title.string)

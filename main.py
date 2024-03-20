from bs4 import BeautifulSoup

with open("website.html",encoding="utf-8") as file:
    content = file.read()

print(content)
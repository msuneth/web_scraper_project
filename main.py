from bs4 import BeautifulSoup
import requests

response = requests.get("https://news.ycombinator.com/")
web_page = response.text
#print(web_page)

soup = BeautifulSoup(web_page,'html.parser')
print(soup.title)
#article_span_tag = soup.find_all('span', class_='titleline')
articles = soup.find_all('span', class_='titleline')
article_texts = []
article_links = []
# print(article_span_tag.getText())
# print(article_span_tag.find('a').get('href'))
for article in articles:
    article_texts.append(article.getText())
    article_links.append(article.find('a').get('href'))
article_upvotes = [vote.getText() for vote in soup.find_all(name='span',class_='score')]
print(article_texts)
print(article_links)
print(article_upvotes)
#print(article_text)
# with open("website.html",encoding="utf-8") as file:
#     content = file.read()
#
# soup = BeautifulSoup(content,'html.parser')
# print(soup.title)
# print(soup.title.string)
# print(soup.prettify())
# print(soup.a)
# print(soup.p)
# print(soup.li)
#
# all_anchor_tag = soup.findAll(name="a")
# print(all_anchor_tag)
#
# for tag in all_anchor_tag:
#     print(tag.getText())
#     print(tag.get("href"))
#
# heading = soup.find(name="h1",id="name")
# print(heading)
#
# section_heading = soup.find(name="h3",class_="heading")
# print(section_heading)
#
# h3_heading = soup.find_all("h3",class_="heading")
# print(h3_heading)
#
# company_url = soup.select_one(selector="p a")
# print(company_url)
#
# name = soup.select_one(selector="#name")
# print(name)
#
# headings = soup.select_one(selector=".heading")
# print(headings)
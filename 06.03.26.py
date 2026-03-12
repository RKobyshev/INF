# import requests
# import lxml
# import pandas
# import networkx
# headers = {
#     "User-Agent": "Mozilla/5.0 (SeminarScraper/1.0; +https://example.org/)",
#     "Accept": "text/html,application/xhtml+xml",
#     "Accept-Language": "ru,en;q=0.8",
# }
#
# session = requests.Session()
# session.headers.update(headers)
#
# r1 = session.get("https://ru.wikipedia.org", timeout=20)
# #
# from bs4 import BeautifulSoup
# #
# soup = BeautifulSoup(r1.text, "lxml")  # если lxml не установлен, используйте "html.parser"
# #
# # links = soup.find_all("a", href=True)
# # l = []
# # for a in links:
# #     h = a["href"]
# #     l.append(h)
# # print(l)
#
# from urllib.parse import urljoin
#
# BASE = "https://ru.wikipedia.org"
#
# dyk = soup.find(id='main-dyk')
# link = dyk.find("a", href=True)["href"]
#
# article_url = urljoin(BASE, link)
#
# print(article_url)
#
# resp_article = requests.get(article_url, headers=headers, timeout=20)
#
# soup_article = BeautifulSoup(resp_article.text, "lxml")
# title = soup_article.find("h1").get_text(strip=True)
# print(title)

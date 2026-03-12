import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

headers = {
    "User-Agent": "Mozilla/5.0 (SeminarScraper/1.0; +https://example.org/)",
    "Accept": "text/html,application/xhtml+xml",
    "Accept-Language": "ru,en;q=0.8",
}

session = requests.Session()
session.headers.update(headers)

BASE = "https://ru.wikipedia.org"

rnd = "https://ru.wikipedia.org/api/rest_v1/page/random/summary"

a = session.get(rnd, timeout=20).json()
s0 = a["content_urls"]["desktop"]["page"]
t0 = a["title"]

a1 = session.get(s0, timeout=20)
soup1 = BeautifulSoup(a1.text, "lxml")
t1 = soup1.find("h1").get_text(strip=True)
s1 = urljoin(BASE, soup1.find(id="mw-content-text").find("a", href=True)["href"])

a2 = session.get(s1, timeout=20)
soup2 = BeautifulSoup(a2.text, "lxml")
t2 = soup2.find("h1").get_text(strip=True)
s2 = urljoin(BASE, soup2.find(id="mw-content-text").find("a", href=True)["href"])

a3 = session.get(s2, timeout=20)
soup3 = BeautifulSoup(a3.text, "lxml")
t3 = soup3.find("h1").get_text(strip=True)
s3 = urljoin(BASE, soup3.find(id="mw-content-text").find("a", href=True)["href"])

print(s0, t0)
print(s1, t1)
print(s2, t2)
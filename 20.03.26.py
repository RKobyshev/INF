import networkx
import requests
from bs4 import BeautifulSoup
from urllib.parse import unquote
from collections import deque
import time

import networkx as nx
import pandas as pd
import matplotlib.pyplot as plt

# Вспомогательные функции
BASE = "https://ru.wikipedia.org"
HEADERS = {
    "User-Agent": "WikiGraphBot/1.0 (https://example.org/bot; your-email@example.org)",
    "Accept-Encoding": "gzip",
    "Accept-Language": "ru,en;q=0.8"
}

def article_to_url(title: str) -> str:
    return f"{BASE}/wiki/{title.replace(' ', '_')}"

def is_valid_article_href(href: str) -> bool:
    if not href.startswith("/wiki/"):
        return False

    title = href[len("/wiki/"):]

    if not title:
        return False
    if "#" in title:
        return False
    if ":" in title:
        return False
    if title.startswith("Заглавная_страница"):
        return False

    return True

def href_to_title(href: str) -> str:
    return unquote(href[len("/wiki/"):]).replace("_", " ")

def extract_article_links(article_title: str, max_links: int = 30):
    url = article_to_url(article_title)
    resp = requests.get(url, headers=HEADERS, timeout=200)
    resp.raise_for_status()

    soup = BeautifulSoup(resp.text, "lxml")
    content = soup.find("div", id="mw-content-text")
    if content is None:
        return []

    links = []
    seen = set()

    for a in content.find_all("a", href=True):
        href = a["href"]

        if not is_valid_article_href(href):
            continue

        target_title = href_to_title(href)

        if target_title == article_title:
            continue
        if target_title in seen:
            continue

        seen.add(target_title)
        links.append(target_title)

        if len(links) >= max_links:
            break

    return links
def build_wikipedia_graph(start_title: str, depth: int = 1, max_links_per_page: int = 20, sleep_sec: float = 1.0):
    G = nx.DiGraph()
    visited = set()
    queue = deque([(start_title, 0)])

    while queue:
        current_title, current_depth = queue.popleft()

        if current_title in visited:
            continue
        visited.add(current_title)

        try:
            neighbors = extract_article_links(current_title, max_links=max_links_per_page)
        except Exception as e:
            print(f"Ошибка при обработке статьи '{current_title}': {e}")
            continue

        for nb in neighbors:
            G.add_edge(current_title, nb)

            if current_depth < depth:
                queue.append((nb, current_depth + 1))

        time.sleep(sleep_sec)

    return G
sample_links = extract_article_links("Математика", max_links=15)
sample_links[:10]

START_ARTICLE = "Математика"

G = build_wikipedia_graph(
    start_title=START_ARTICLE,
    depth=1,
    max_links_per_page=15,
    sleep_sec=1
)

print("Число вершин:", G.number_of_nodes())
print("Число рёбер:", G.number_of_edges())

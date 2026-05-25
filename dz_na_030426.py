import requests
from bs4 import BeautifulSoup
from urllib.parse import unquote
from collections import deque
import time
import matplotlib.pyplot as plt
#мой код не заработал, поэтому нейронке пришлось его исправлять(
HEADERS = {
    "User-Agent": "Mozilla/5.0 (SeminarScraper/1.0; +https://example.org/)",
    "Accept": "text/html,application/xhtml+xml",
    "Accept-Language": "ru,en;q=0.8",
}
session = requests.Session()
session.headers.update(HEADERS)
session.proxies = {"http": None, "https": None}
BASE = "https://ru.wikipedia.org"


def article_to_url(title): return f"{BASE}/wiki/{title.replace(' ', '_')}"


def is_valid_article_href(href):
    return href.startswith("/wiki/") and "#" not in href and ":" not in href and not href.startswith(
        "/wiki/Заглавная_страница")


def href_to_title(href): return unquote(href[6:]).replace("_", " ")


def extract_article_links(article_title, max_links=20):
    soup = BeautifulSoup(session.get(article_to_url(article_title), timeout=5).text, "lxml")
    content = soup.find("div", id="mw-content-text")
    links, seen = [], set()
    for a in content.find_all("a", href=True) if content else []:
        href = a["href"]
        if not is_valid_article_href(href): continue
        target = href_to_title(href)
        if target == article_title or target in seen: continue
        seen.add(target)
        links.append(target)
        if len(links) >= max_links: break
    return links


TARGET = "Математика"
TRIALS = 10
MAX_DEPTH = 5
distances = []

for trial in range(TRIALS):
    rnd = session.get("https://ru.wikipedia.org/api/rest_v1/page/random/summary", timeout=5).json()
    start = rnd["title"]
    print(f"\n{trial + 1}. {start} -> ", end="")

    queue = deque([(start, 0)])
    visited = {start}
    found = None
    processed = 0
    last_depth = -1

    while queue and found is None:
        cur, d = queue.popleft()
        processed += 1
        if d != last_depth:
            last_depth = d
            print(f"глуб.{d} (обр.{processed}, в очереди {len(queue)}) ", end="")
        if d >= MAX_DEPTH:
            continue
        for nb in extract_article_links(cur, max_links=5):
            if nb == TARGET:
                found = d + 1
                break
            if nb not in visited:
                visited.add(nb)
                queue.append((nb, d + 1))
        time.sleep(0.1)

    if found is not None:
        distances.append(found)
        print(f"найдено за {found} шагов")
    else:
        print(f"не найдено за {MAX_DEPTH} шагов")

# --- гистограмма ---
if distances:
    plt.hist(distances, bins=range(1, max(distances) + 2), edgecolor='black')
    plt.title(f"Расстояния от случайных статей до «{TARGET}» (n={len(distances)})")
    plt.xlabel("Число переходов")
    plt.ylabel("Частота")
    plt.show()
    print(f"Среднее: {sum(distances) / len(distances):.2f}, мин={min(distances)}, макс={max(distances)}")
else:
    print("Нет успешных попыток")
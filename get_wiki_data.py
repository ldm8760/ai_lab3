import requests
from bs4 import BeautifulSoup
import random
import pandas as pd
import re
import time

def pull_page(url: str):
    time.sleep(random.uniform(0.5, 1.5))
    response = requests.get(url, headers={"User-Agent": random.choice(user_agents)})
    print(f"Request {request_index} successful!")
    return response

def get_data(url, lang):
    page = pull_page(url)

    soup = BeautifulSoup(page.text, "html.parser")

    # print(soup.find("h1").text)
    paragraphs = soup.find_all("p")

    rows = []
    for pg in paragraphs:
        pg = pg.text.strip()
        pg = re.sub(r"[^\w\d\s]", "", pg)
        pg = re.sub(r"\[\d\]", "", pg)
        pg = pg.split()
        words = len(pg)

        if words > 15:
            start = random.randint(0, words - 15)
            entry = []
            for i in range(start, start + 15):
                entry.append(pg[i])
            row = [lang] + entry
            rows.append(row)

    return rows


if __name__ == "__main__":
    links = {
        "en": "https://en.wikipedia.org/wiki/Special:Random", 
        "nl": "https://nl.wikipedia.org/wiki/Special:Random"
    }
    user_agents = [
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) Gecko/115.0 Firefox/115.0",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Version/13.1 Safari/537.36",
        "Mozilla/5.0 (Linux; Android 11; Pixel 5 Build/RQ3A.210805.001) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Mobile Safari/537.36"
    ]
    request_index = 1

    columns = ["lang"] + [f"word{i+1}" for i in range(15)]
    all_rows = []
    for i in range(5):
        lang = random.choice(list(links.keys()))
        url = links[lang]
        new_rows = get_data(url, lang)
        request_index += 1
        all_rows.extend(new_rows)

    df = pd.DataFrame(all_rows, columns=columns)
    df.to_csv("data/wiki_data.csv", mode="a", header=False, index=False)



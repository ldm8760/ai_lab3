import requests
from bs4 import BeautifulSoup
import csv
import random
import pandas as pd
import re

url = "https://en.wikipedia.org/wiki/Special:Random"
# url = "https://nl.wikipedia.org/wiki/Special:Random"

page = requests.get(url)

soup = BeautifulSoup(page.text, "html.parser")

print(soup.find("h1").text)
paragraphs = soup.find_all("p")

for pg in paragraphs:
    pg = pg.text.strip()
    pg = re.sub(r"[^\w\d\s]", "", pg)
    pg = re.sub(r"\[\d\]", "", pg)
    pg = pg.split(" ")
    # print(pg)
    pg_len = len(pg)
    if pg_len > 15:
        start = random.randint(0, pg_len - 15)
        end = start + 15
        entry = []
        for i in range(15):
            entry.append(pg[i])
        
        print(entry)


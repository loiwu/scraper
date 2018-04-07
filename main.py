import urllib.request
from bs4 import BeautifulSoup

import csv
from datetime import datetime

quote_page = 'http://www.jihuawang.net/'

page = urllib.request.urlopen(quote_page)

soup = BeautifulSoup(page, 'html.parser')

title_box = soup.find('h2', attrs={'class': 'entry-title'})

title = title_box.text.strip()
print(title)

published_box = soup.find('time', attrs={'class':'published'})
published = published_box.text
print(published)

summary_box = soup.find('div', attrs={'class':'entry-summary'})
summary = summary_box.text
print(summary)

link_box = soup.find('a', attrs={'class':'continue-reading-link'})
link = link_box["href"]
print(link)

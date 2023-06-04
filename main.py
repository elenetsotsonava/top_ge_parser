import time
import requests
from bs4 import BeautifulSoup
from database import DB
from info import Info


db = DB('top_info.db')

for i in range(1, 6):
    response = requests.get(f'https://top.ge/page/{i}')
    soup = BeautifulSoup(response.content, 'html.parser')

    names = soup.find_all('a', {'class': 'stie_title'})
    topics = soup.find_all('a', {'class': 'cat_name_list'})
    descriptions = soup.find_all('td', {'class': 'tr_paddings desc_pd hidden-xs ipad_hidden'})

    for j in range(20):
        info = Info(names[j].text.strip(), topics[j].text.strip(), descriptions[j].text.strip())
        db.add_info(info)

    time.sleep(15)

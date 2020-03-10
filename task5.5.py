import requests
import datetime
import json
from bs4 import BeautifulSoup

republika={
    "time":"",
    "category":"",
    "tittle":""
}

data = []

page = requests.get("https://www.republika.co.id/")
obj = BeautifulSoup(page.text,'html.parser');

for headline in obj.find_all('div', class_='conten1'):
    republika["category"] = (headline.find('h1').text)
    republika["tittle"] = (headline.find('h2').text)
    date = datetime.datetime.now()
    today = data.strftime("%A")+", "+date.strftime("%d")+" "+data.strftime("%B")+" "+data.strftime("%Y")
    republika["time"] = today

    data.append (str(republika))

with open ("headline.json", "w") as write_file:
    json.dump(data, write_file)

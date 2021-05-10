import pandas as pd
import requests
from bs4 import BeautifulSoup


url = "https://247sports.com/college/penn-state/Season/2022-Football/Commits/"
# Add the `user-agent` otherwise we will get blocked when sending the request
headers = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36"
}


response = requests.get(url, headers=headers).content
soup = BeautifulSoup(response, "html.parser")
data = []

for tag in soup.find_all("li", class_="ri-page__list-item")[1:]:  # `[1:]` Since the first result is a table header
    school = tag.find_next("span", class_="meta").text
    name = tag.find_next("a", class_="ri-page__name-link").text
    position = tag.find_next("div", class_="position").text
    height_weight = tag.find_next("div", class_="metrics").text
    rating = tag.find_next("span", class_="score").text
    nat_rank = tag.find_next("a", class_="natrank").text
    state_rank = tag.find_next("a", class_="sttrank").text
    pos_rank = tag.find_next("a", class_="posrank").text
    status = tag.find_next("p", class_="commit-date withDate").text

    data.append(
        {
            "school": school,
            "name": name,
            "position": position,
            "height_weight": height_weight,
            "rating": rating,
            "nat_rank": nat_rank,
            "state_rank": state_rank,
            "pos_rank": pos_rank,
            "status": status,
        }
    )

df = pd.DataFrame(data)

print(df.to_string())
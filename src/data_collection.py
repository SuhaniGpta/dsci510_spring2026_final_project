from pytrends.request import TrendReq
from src.config import TRENDS_KEYWORD, TRENDS_TIMEFRAME
import requests

# AI generated:
def get_trends_data():
    pytrends = TrendReq()
    keywords = [
        "Resident Evil Requiem",
        "Resident Evil Village",
        "Resident Evil 4",
        "Resident Evil 2",
        "Resident Evil 3"
    ]
    pytrends.build_payload(keywords, timeframe=TRENDS_TIMEFRAME)
    data = pytrends.interest_over_time()
    return data

# AI generated:
def get_steam_app_details(app_id):
    url = f"https://store.steampowered.com/api/appdetails?appids={app_id}"
    response = requests.get(url)
    data = response.json()
    return data[str(app_id)]["data"]


# AI generated:
def get_steam_review_summary(app_id):
    url = f"https://store.steampowered.com/appreviews/{app_id}"
    params = {"json": 1}
    response = requests.get(url, params=params)
    return response.json()["query_summary"]

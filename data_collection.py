from pytrends.request import TrendReq

def get_trends_data():
    pytrends = TrendReq()
    keywords = ["Resident Evil Requiem"]
    pytrends.build_payload(keywords, timeframe="today 3-m")
    data = pytrends.interest_over_time()
    return data

if __name__ == "__main__":
    data = get_trends_data()
    print(data.head())
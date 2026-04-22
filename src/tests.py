from src.data_collection import get_trends_data
from src.config import TRENDS_KEYWORDS

# AI Generated:
# Learned and Understood by Creator:

def test_trends_data():
    data = get_trends_data()
    assert data is not None
    assert not data.empty
    assert TRENDS_KEYWORDS[0] in data.columns

if __name__ == "__main__":
    test_trends_data()
    print("Yay Yippie!")

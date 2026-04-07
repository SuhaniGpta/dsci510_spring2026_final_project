from data_collection import get_trends_data

def test_trends_data():
    data = get_trends_data()

    assert data is not None
    assert not data.empty
    assert "Resident Evil Requiem" in data.columns

    print("--- Data Sample ---")
    print(data.head())

if __name__ == "__main__":
    test_trends_data()
    print("It works!")

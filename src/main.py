import matplotlib.pyplot as plt
import pandas as pd
import os
from src.data_collection import get_trends_data, get_steam_app_details, get_steam_review_summary
from src.config import GAME_IDS, RESULTS_DIR


# AI Generated:
# Learned and Understood by Creator:

def run_analysis_pipeline():
    os.makedirs(RESULTS_DIR, exist_ok=True)
    
    data = get_trends_data()
    games = [col for col in data.columns if col != "isPartial"]

    print("--- Google Trends Data Sample ---")
    print(data.head())

    data[games].plot()
    plt.title("Google Trends Interest Comparison")
    plt.xlabel("Date")
    plt.ylabel("Relative Search Interest")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig(f"{RESULTS_DIR}/trends_over_time.png")
    plt.clf()

    data.to_csv(f"{RESULTS_DIR}/trends_data.csv")

    peak_values = data[games].max()
    peak_values.plot(kind="bar")
    plt.title("Peak Search Interest Comparison")
    plt.ylabel("Maximum Search Interest")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig(f"{RESULTS_DIR}/peak_comparison.png")
    plt.clf()

    print("\nFetching Steam API data...")
    steam_rows = []

    for game, app_id in GAME_IDS.items():
        details = get_steam_app_details(app_id)
        reviews = get_steam_review_summary(app_id)

        steam_rows.append({
            "Game": game,
            "AppID": app_id,
            "Release_Date": details.get("release_date", {}).get("date", "N/A"),
            "Price": details.get("price_overview", {}).get("final_formatted", "N/A"),
            "Recommendations": details.get("recommendations", {}).get("total", 0),
            "Total_Reviews": reviews.get("total_reviews", 0),
            "Total_Positive": reviews.get("total_positive", 0),
            "Total_Negative": reviews.get("total_negative", 0),
            "Review_Score": reviews.get("review_score_desc", "N/A")
        })

    steam_df = pd.DataFrame(steam_rows)
    steam_df["Positive_Percentage"] = (
        steam_df["Total_Positive"] / (steam_df["Total_Positive"] + steam_df["Total_Negative"])
    ) * 100

    print("--- Steam Data Summary ---")
    print(steam_df)

    steam_df.to_csv(f"{RESULTS_DIR}/steam_summary.csv", index=False)

    steam_df.set_index("Game")["Total_Reviews"].plot(kind="bar", color='skyblue')
    plt.title("Steam Total Reviews Comparison")
    plt.ylabel("Total Count")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig(f"{RESULTS_DIR}/steam_reviews_comparison

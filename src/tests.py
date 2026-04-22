from src.data_collection import get_trends_data, get_steam_app_details, get_steam_review_summary
import matplotlib.pyplot as plt
import pandas as pd
import os

# AI generated:
def main():
    os.makedirs("results", exist_ok=True)

    # ---------------------------
    # Google Trends
    # ---------------------------
    data = get_trends_data()
    games = [col for col in data.columns if col != "isPartial"]

    print("--- Google Trends Data Sample ---")
    print(data.head())

    data[games].plot()
    plt.title("Google Trends Comparison")
    plt.xlabel("Date")
    plt.ylabel("Search Interest")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig("results/trends_over_time.png")
    plt.clf()

    data.to_csv("results/trends_data.csv")

    peak_values = data[games].max()
    avg_values = data[games].head(14).mean()

    peak_values.plot(kind="bar")
    plt.title("Peak Search Interest Comparison")
    plt.ylabel("Search Interest")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig("results/peak_comparison.png")
    plt.clf()

    avg_values.plot(kind="bar")
    plt.title("Average Early Search Interest (First 2 Weeks)")
    plt.ylabel("Search Interest")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig("results/early_interest.png")
    plt.clf()

    # ---------------------------
    # Steam data
    # ---------------------------
    game_ids = {
        "Resident Evil Requiem": 3764200,
        "Resident Evil Village": 1196590,
        "Resident Evil 4": 2050650,
        "Resident Evil 2": 883710,
        "Resident Evil 3": 952060
    }

    steam_rows = []

    for game, app_id in game_ids.items():
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

    print("\n--- Steam Data ---")
    print(steam_df)

    # AI generated:
    steam_df["Positive_%"] = (
                                     steam_df["Total_Positive"] /
                                     (steam_df["Total_Positive"] + steam_df["Total_Negative"])
                             ) * 100
    steam_df.to_csv("results/steam_summary.csv", index=False)

    steam_df.set_index("Game")["Total_Reviews"].plot(kind="bar")
    plt.title("Steam Total Reviews Comparison")
    plt.ylabel("Total Reviews")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig("results/steam_reviews_comparison.png")
    plt.clf()
    # AI generated:
    steam_df.set_index("Game")["Positive_%"].plot(kind="bar")
    plt.title("Steam Positive Review %")
    plt.ylabel("Percent Positive")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig("results/steam_positive_percent.png")
    plt.clf()

    # AI generated:
    steam_df.set_index("Game")["Recommendations"].plot(kind="bar")
    plt.title("Steam Recommendations Comparison")
    plt.ylabel("Recommendations")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig("results/steam_recommendations.png")
    plt.clf()

if __name__ == "__main__":
    main()

# Resident Evil Requiem: Early Market Signals Analysis

This project looks at the early launch performance of *Resident Evil Requiem* on Steam. The main goal is to understand how player engagement and public interest change during the first few weeks after release. I am using Google Trends data along with Steam data to see how search interest and player activity relate to each other.

# Data sources

I am using a few different data sources for this project:

- **Google Trends (API using pytrends)**  
  This gives search interest over time for *Resident Evil Requiem*. It helps show how public interest changes.

- **Steam User Reviews**  
  This includes review text, dates, playtime, and helpful votes. This will be used to understand player engagement and reactions.

- **Steam Web API / Game Metadata**  
  This includes information like release date, price, tags, and review counts. This helps compare the game with previous Resident Evil titles and other AAA games.

# Results

Right now, I have successfully collected Google Trends data using Python. The next step is to bring in Steam data and start comparing how engagement changes over time. The goal is to identify early signals that show whether a game is performing well after launch.

# Installation

To run this project, install the required packages:

```bash
pip install -r requirements.txt

# Resident Evil Requiem: Early Market Signals Analysis

This project analyzes the early launch performance of Resident Evil Requiem on Steam. The main goal is to understand how player engagement and public interest change during the first few weeks after release. I use Google Trends data along with Steam data to examine how search interest and player activity relate to each other and to compare these patterns with previous Resident Evil titles.

# Data sources

I am using a few different data sources for this project:

- **Google Trends (API using pytrends)**  
  This gives search interest over time for *Resident Evil Requiem*. It helps show how public interest changes.

- **Steam User Reviews**  
  This includes review text, dates, playtime, and helpful votes. This will be used to understand player engagement and reactions.

- **Steam Web API / Game Metadata**  
  This includes information like release date, price, tags, and review counts. This helps compare the game with previous Resident Evil titles and other AAA games.

## Analysis
The project compares five Resident Evil titles:
- Resident Evil Requiem  
- Resident Evil Village  
- Resident Evil 4  
- Resident Evil 2  
- Resident Evil 3

Key analysis includes:
- Search interest over time (Google Trends)
- Peak search interest comparison
- Average early search interest (first two weeks)
- Steam total review comparison
- Steam positive review percentage

# Results

So far, I have successfully collected and analyzed Google Trends data to examine early public interest in Resident Evil Requiem. The data shows a clear spike in search interest around the game’s release, indicating strong initial attention.

I have also begun integrating Steam data, including review counts and ratings, to analyze player engagement and reception. Early comparisons suggest that while Resident Evil Requiem generates significant initial hype, older titles may show stronger long-term engagement.

The project is currently focused on combining these data sources to better understand how public attention and player activity evolve over time. The goal is to identify early signals that indicate how well a game is performing shortly after launch.

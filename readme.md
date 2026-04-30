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

The results show that Resident Evil Requiem generates the strongest initial spike in search interest, indicating high early public attention at launch. However, older titles such as Resident Evil 2 and Resident Evil 4 demonstrate higher average search interest and greater total review counts, suggesting stronger sustained engagement over time.

Additionally, all games maintain high positive review percentages, indicating strong overall player satisfaction across the franchise. While Requiem shows strong early engagement for a newly released game, it has not yet reached the long-term engagement levels of older titles.

Overall, the analysis highlights a key insight: early hype does not necessarily translate into sustained player engagement. By combining Google Trends and Steam data, this project provides a more complete understanding of early game performance.

# AI Usage

This project was developed with assistance from generative AI tools, including ChatGPT (OpenAI) and Google Gemini. As a beginner in Python and data analysis, I used these tools to help understand how the code works, structure the project, and implement certain components such as data collection and analysis.

AI was primarily used as a learning aid to support understanding of concepts and to guide development. All AI-generated code sections are clearly labeled in the source files with the comment # AI generated:. Please know I tried my best to understand everything within this project!

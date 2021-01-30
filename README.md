# PokerAnalysisHackit2021

This program analyzes Texas Holdem' hands and games.

Developed in Python


### Resources
- I'm watching this video to figure out how the API stuff works https://www.youtube.com/watch?v=uFsaiEhr1zs



### Pushing code to AWS Lambda

1. Download AWS CLI
2. Run `aws configure`
3. Type in info from your email
4. zip code
5. `aws lambda update-function-code --function-name PokerAnalyzer --zip-file <zip file>`

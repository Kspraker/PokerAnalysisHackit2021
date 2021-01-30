# PokerAnalysisHackit2021

This program analyzes Texas Holdem' hands and games.

Developed in Python


### Resources
- I'm watching this video to figure out how the API stuff works https://www.youtube.com/watch?v=uFsaiEhr1zs

- Files should look like this apparently
lambda-test.zip/
├── main.py(lambda entry point containing the lambda_handler method)
├── Folder1/
│ ├── File1
│ ├── File2
│ ├── some_method.py
│ └── docs
├── SomeOtherFolder/
│ ├── File1
│ └── docs
├── package1
├── package2
├── package3
└── package4



### Pushing code to AWS Lambda

1. Download AWS CLI
2. Run `aws configure`
3. Type in info from your email
4. zip code
5. `aws lambda update-function-code --function-name PokerAnalyzer --zip-file <zip file>`

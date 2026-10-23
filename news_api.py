
import requests

query = input("What type of news are you interested in today? ")

api = "533e8abc7b9746e58f244eeb9b1a964f"

url = (
    f"https://newsapi.org/v2/everything?"
    f"q={query}&language=en&sortBy=publishedAt&apiKey={api}"
)

response = requests.get(url)

data = response.json()

if data["status"] != "ok":
    print("Error:", data["message"])
else:
    articles = data["articles"]

    for index, article in enumerate(articles, start=1):
        print(f"{index}. {article['title']}")
        print(f"Source: {article['source']['name']}")
        print(f"URL: {article['url']}")
        print("*" * 50)
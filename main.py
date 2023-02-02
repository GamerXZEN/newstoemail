import requests
from send_email import send_email as se

api_key = "ab1ef33e9fcc448b86f1e7b0cf03c98f"
url = "https://newsapi.org/v2/everything?q=" \
      "tesla&from=2023-01-02&sortBy=publishedAt&apiKey" \
      "=ab1ef33e9fcc448b86f1e7b0cf03c98f"

request = requests.get(url)
content = request.json()

email_addresses = ["testcasepython123@gmail.com", "sujathanelluri@gmail.com",
                   "pedineedi@gmail.com", "gouthamnarayana.pedinedi.437@k12"
                                          ".friscoisd.org",
                   "karthik.saripalli.643@k12.friscoisd.org"]

body = ""
for article in content["articles"]:
	body = body + str(article["title"]) + "\n" + str(article["description"]) + "\n\n"

body = body.encode("utf-8")
for email_address in email_addresses:
	se(body, email_address)

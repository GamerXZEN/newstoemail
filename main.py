import requests
from send_email import send_email as se

topic = "tesla"
api_key = "ab1ef33e9fcc448b86f1e7b0cf03c98f"
url = "https://newsapi.org/v2/everything?" \
      f"q={topic}" \
      "&from=2023-01-02&" \
      "sortBy=publishedAt" \
      "&apiKey=ab1ef33e9fcc448b86f1e7b0cf03c98f" \
      "&language=en" \

request = requests.get(url)
content = request.json()

email_addresses = ["testcasepython123@gmail.com", "sujathanelluri@gmail.com",
                   "pedineedi@gmail.com", "gouthamnarayana.pedinedi.437@k12"
                                          ".friscoisd.org",
                   "karthik.saripalli.643@k12.friscoisd.org"]

body = ""
for article in content["articles"][:20]:
	if article["title"] is not None:
		body = "Subject: Today's Morning News" + \
		body + article["title"] + "\n" + \
		article["description"] + "\n" + article["url"] + "\n\n"

body = body.encode("utf-8")
for email_address in email_addresses:
	se(body, email_address)

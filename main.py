import requests
from send_email import send_email as se

api_key = "ab1ef33e9fcc448b86f1e7b0cf03c98f"
url = "https://newsapi.org/v2/everything?q=" \
      "tesla&from=2023-01-02&sortBy=publishedAt&apiKey" \
      "=ab1ef33e9fcc448b86f1e7b0cf03c98f"

request = requests.get(url)
content = request.json()
print(content["articles"])

email_addresses = ["testcasepython123@gmail.com", "sujathanelluri@gmail.com",
                   "pedineedi@gmail.com", "gouthamnarayana.pedinedi.437@k12"
                                          ".frisco.org"]

for email_address in email_addresses:
	se("Hello", email_address)

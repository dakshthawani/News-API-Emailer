import requests
from send_email import send_mail

api_key = "34fa364fd3a34cefb72b136aed702bb1"
url = ('https://newsapi.org/v2/everything?'
       'q=Apple&'
       'from=2024-08-11&'
       'sortBy=popularity&'
       'apiKey=' + api_key + '&language=en')
request = requests.get(url)
content = request.json()
print(len(content['articles']))
body = "Subject: Today's News" + "\n"
for article in content['articles'][:20]:
    if article['title'] is not None and article['description'] is not None:
        # print(article['title'])
        # print(article['description'])
        body = (body + article['title'] \
                + "\n" + article['description'] \
                + article['url'] + 2*"\n")
body = body.encode("utf-8")
send_mail(message=body)

import requests
url = "https://vercel.com/411017284/misruby"
Data = requests.get(url)
print(Data.text)
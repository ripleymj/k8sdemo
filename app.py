from flask import Flask
import requests
from bs4 import BeautifulSoup

app = Flask('hello-cloudbuild')

@app.route('/')
def hello():
    r = requests.get('https://finance.yahoo.com/quote/BTC-USD?p=BTC-USD')
    data = r.text
    soup = BeautifulSoup(data)

    print(soup)
  return "Goodbye World!\n"

if __name__ == '__main__':
  app.run(host = '0.0.0.0', port = 8080)

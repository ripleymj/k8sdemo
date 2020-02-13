

from flask import Flask
app = Flask('hello-cloudbuild')

@app.route('/')
def hello():
  import requests
  head = {"Accept": "text/plain"}
  req = requests.get('https://icanhazdadjoke.com/',headers=head)
  return req.text
  #return "Hello World!\n"

if __name__ == '__main__':
  app.run(host = '0.0.0.0', port = 8080)

from flask import Flask
app = Flask('hello-cloudbuild')

@app.route('/')
def hello():
  return "Hello World!\n This is Riley's Page!"

if __name__ == '__main__':
  app.run(host = '0.0.0.0', port = 8080)

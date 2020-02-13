from flask import Flask
app = Flask('hello-cloudbuild')

@app.route('/')
def hello():
  return "When you realize you don't really know python like that.\n"

if __name__ == '__main__':
  app.run(host = '0.0.0.0', port = 8080)

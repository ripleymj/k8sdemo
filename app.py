from flask import Flask
app = Flask('hello-cloudbuild')

@app.route('/')
def hello():
    print("Insert cliche quote here")

if __name__ == '__main__':
  app.run(host = '0.0.0.0', port = 8080)

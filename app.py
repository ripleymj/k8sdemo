from flask import Flask
app = Flask('hello-cloudbuild')

@app.route('/')
def hello():
    return "<style>body {background-color: red;}</style><body><h1>Hello World!</h1>\n<img href='https://i.kym-cdn.com/photos/images/newsfeed/001/480/544/6c1.jpg' /></body>"

if __name__ == '__main__':
  app.run(host = '0.0.0.0', port = 8080)

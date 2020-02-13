import random
from flask import Flask
app = Flask('hello-cloudbuild')

@app.route('/')
def hello():
  return "Crappy website.\n"

@app.route('/oop')
def yuck():
    largest_prime = random.randint(1, 500000000)

    return f"Largest prime; {largest_prime}"

if __name__ == '__main__':
  app.run(host = '0.0.0.0', port = 8080)

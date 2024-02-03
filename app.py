from flask import Flask

app = Flask(__name__)

@app.route('/')
def main():
  return {"message": "pasta raiz"}

if __name__ == "__main__":
  app.debug = True
  app.run()
  
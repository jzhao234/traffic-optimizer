from flask import Flask

app = Flask(__name__)

@app.route("/ ")
def members():
  return "3212"

if __name__ == "__main__":
  app.run(debug=True)
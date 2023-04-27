from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return """<!DOCTYPE html>
<html>
  <head>
    <title>非同期Webページのサンプル</title>
  </head>
  <body>
    <h1>Hello</h1>
    <div id="result"></div>
    <script src="static/script.js"></script>
  </body>
</html>
"""

@app.route("/get_result")
def get_result():
    return "World"

if __name__ == "__main__":
    app.run()

from flask import Flask

from app_init import init

app = Flask(__name__)
init(app)

@app.route("/")
def hello():
    return "Hello World!"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=3000, debug=True)

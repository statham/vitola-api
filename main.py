from flask import Flask

from app_init import init

app = Flask(__name__)
init(app)

if __name__ == "__main__":
    app.run(port=3000, debug=True)

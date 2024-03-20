import os
import random
from flask import Flask

app = Flask(__name__)


@app.route("/")
def index():
    return "Привет от приложения Flask"


@app.route("/vestertn")
def user_hack():
    ls = []
    error = 0
    while error < 200:
        created_code = random.randint(10000, 99999999999999)
        if created_code in ls:
            error += 1
        else:
            ls.append(created_code)
    return ls


if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)

from flask import *
from gis import *
import datetime
from core import *
from caching import cache
app = Flask(__name__)
cache = cache.init_app(app)
app.register_blueprint(gis, url_prefix='/gis')


@app.route("/")
def main():
    return "Hello Uzbekistan"

if __name__ == '__main__':
    app.run(debug=True)


#!/usr/bin/python3
"""
Initiates a Flask-based web application.
"""

from flask Import Flask, render_template
from models import *
from models import storage

app = Flask(__name__)


@app.route('/hbnb_filters', strict_slashes=False)
def filters():
    """Shows a HTML page like 6-index.html from static"""
    states = storage.all("state").values()
    amentities = storage.all("Amenity").values()
    return render_template('10-hbnb_filters.html', states=states,
                            amenities=amenities)


@app.teardown_appcontext
def teardown_db(exception):
    """Shuts the storage on teardown"""
    storage.close()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')

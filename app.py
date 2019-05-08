from flask import Flask, render_template, url_for

app = Flask(__name__)

import json

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', images=fetch_images(), title="Cybage")

def fetch_images():
    images = [{
        "name": "Front",
        "width": 274,
        "image_path": "../static/images/fulls/cybage_1.jpg",
        "thumb_path": "../static/images/thumbs/cybage_1.jpg"
    }, {
        "name": "Terrace",
        "width": 282,
        "image_path": "../static/images/fulls/cybage_2.jpg",
        "thumb_path": "../static/images/thumbs/cybage_2.jpg"
        },
        {
        "name": "UpShot",
        "width": 476,
        "image_path": "../static/images/fulls/cybage_3.jpg",
        "thumb_path": "../static/images/thumbs/cybage_3.jpg"
        },
        {
        "name": "Ground",
        "width": 232,
        "image_path": "../static/images/fulls/cybage_4.jpg",
        "thumb_path": "../static/images/thumbs/cybage_4.jpg"
    }

             ]

    return images

@app.errorhandler(404)
def not_found_error(error):
    return render_template('404.html', title="404 Not Found"), 404

@app.errorhandler(500)
def internal_error(error):
    return render_template('500.html', title="500 Internal Error"), 500

if __name__ == '__main__':
    app.run( debug=True)

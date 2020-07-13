from flask import Flask, render_template, jsonify
from flask_cors import CORS
import os

app = Flask(__name__)
port = int(os.getenv("PORT", 9099))
CORS(app)

@app.route('/')
def index():
    return render_template('index.html'), 200


@app.route('/section.html')
def section():
    return render_template('section.html'), 200


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=port)

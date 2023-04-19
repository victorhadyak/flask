from flask import Flask, render_template, url_for, jsonify, request
import sys

app = Flask(__name__)

# Object that will hold last connection state
@app.route('/')
def index():
    return render_template('index.html')
    
@app.route('/healthz')
def healthz():
    return 'OK', 200

if __name__ == "__main__":
    app.run(host="0.0.0.0")

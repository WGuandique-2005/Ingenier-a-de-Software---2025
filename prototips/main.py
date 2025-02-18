from flask import Flask, render_template, Response, request, redirect, url_for, jsonify
import cv2
from threading import Lock
import time

app = Flask(__name__)
app.config['DEBUG'] = True

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=False)
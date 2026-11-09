from pathlib import Path
from flask import Flask, send_file

app = Flask(__name__)

@app.get('/')
def index():
    return send_file(Path(__file__).with_name('index.html'))

@app.get('/health')
def health():
    return {'status': 'ok'}, 200

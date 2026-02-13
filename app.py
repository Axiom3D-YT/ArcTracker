from flask import Flask, render_template, jsonify
import requests
import json
from datetime import datetime, timezone

app = Flask(__name__)

API_BASE = "https://metaforge.app/api/arc-raiders"
ENDPOINTS = {
    "timers": f"{API_BASE}/event-timers",
    "schedule": f"{API_BASE}/events-schedule",
    "arcs": f"{API_BASE}/arcs"
}

def fetch_data(name):
    try:
        response = requests.get(ENDPOINTS[name])
        response.raise_for_status()
        return response.json()
    except Exception as e:
        print(f"Error fetching {name}: {e}")
        return None

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/data')
def get_all_data():
    return jsonify({
        "timers": fetch_data("timers"),
        "arcs": fetch_data("arcs"),
        "schedule": fetch_data("schedule")
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True, port=5000)

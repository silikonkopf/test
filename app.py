from flask import Flask
from prometheus_client import Counter, Histogram, generate_latest
import random
import time

app = Flask(__name__)

REQUESTS = Counter("requests_total", "Total number of requests")
LATENCY = Histogram("processing_time_seconds", "Processing time")

@app.route("/")
def index():
    REQUESTS.inc()
    with LATENCY.time():
        time.sleep(random.uniform(0.1, 0.8))
    return "Hello Metrics!"

@app.route("/metrics")
def metrics():
    return generate_latest(), 200, {"Content-Type": "text/plain"}

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)

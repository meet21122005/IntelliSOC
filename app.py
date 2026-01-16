from flask import Flask, request, jsonify, render_template
from core.database.db import init_db, insert_log, insert_alert, get_alerts, get_logs
from core.normalization.parser import normalize_log
from core.detection.rule_engine import detect_threats

app = Flask(__name__, template_folder="web/templates", static_folder="web/static")

init_db()

@app.route("/")
def dashboard():
    return render_template("index.html")

@app.route("/api/logs", methods=["POST"])
def receive_logs():
    raw_log = request.json
    log = normalize_log(raw_log)
    insert_log(log)

    alerts = detect_threats(log)
    for alert in alerts:
        insert_alert(alert)

    return jsonify({"status": "processed", "alerts": alerts})

@app.route("/api/logs", methods=["GET"])
def fetch_logs():
    return jsonify(get_logs())

@app.route("/api/alerts", methods=["GET"])
def fetch_alerts():
    return jsonify(get_alerts())

if __name__ == "__main__":
    app.run()
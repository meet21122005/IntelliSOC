from datetime import datetime

def normalize_log(raw):
    return {
        "timestamp": raw.get("timestamp", datetime.utcnow().isoformat()),
        "source": raw.get("source", "unknown"),
        "ip": raw.get("ip", "0.0.0.0"),
        "user": raw.get("user", "unknown"),
        "event_type": raw.get("event_type", "unknown"),
        "severity": raw.get("severity", "low"),
        "message": raw.get("message", "")
    }
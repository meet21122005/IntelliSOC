from datetime import datetime

FAILED_LOGINS = {}

def detect_threats(log):
    alerts = []

    if log["event_type"] == "login_failed":
        ip = log["ip"]
        FAILED_LOGINS[ip] = FAILED_LOGINS.get(ip, 0) + 1

        if FAILED_LOGINS[ip] >= 5:
            alerts.append({
                "timestamp": datetime.utcnow().isoformat(),
                "title": "Brute Force Attack Detected",
                "ip": ip,
                "severity": "HIGH",
                "description": "Multiple failed login attempts from same IP"
            })

    if log["event_type"] == "port_scan":
        alerts.append({
            "timestamp": datetime.utcnow().isoformat(),
            "title": "Port Scanning Detected",
            "ip": log["ip"],
            "severity": "MEDIUM",
            "description": "Suspicious scanning behavior detected"
        })

    if log["event_type"] == "malware":
        alerts.append({
            "timestamp": datetime.utcnow().isoformat(),
            "title": "Malware Activity Detected",
            "ip": log["ip"],
            "severity": "CRITICAL",
            "description": "Known malicious activity detected"
        })

    return alerts
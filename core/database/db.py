import sqlite3

DB_NAME = "soc.db"

def connect():
    return sqlite3.connect(DB_NAME)

def init_db():
    with connect() as con:
        cur = con.cursor()

        cur.execute("""
        CREATE TABLE IF NOT EXISTS logs (
            id INTEGER PRIMARY KEY,
            timestamp TEXT,
            source TEXT,
            ip TEXT,
            user TEXT,
            event_type TEXT,
            severity TEXT,
            message TEXT
        )
        """)

        cur.execute("""
        CREATE TABLE IF NOT EXISTS alerts (
            id INTEGER PRIMARY KEY,
            timestamp TEXT,
            title TEXT,
            ip TEXT,
            severity TEXT,
            description TEXT
        )
        """)
        con.commit()

def insert_log(log):
    with connect() as con:
        con.execute("""
        INSERT INTO logs VALUES (NULL,?,?,?,?,?,?,?)
        """, (log["timestamp"], log["source"], log["ip"], log["user"],
              log["event_type"], log["severity"], log["message"]))
        con.commit()

def insert_alert(alert):
    with connect() as con:
        con.execute("""
        INSERT INTO alerts VALUES (NULL,?,?,?,?,?)
        """, (alert["timestamp"], alert["title"], alert["ip"],
              alert["severity"], alert["description"]))
        con.commit()

def get_logs():
    with connect() as con:
        return con.execute("SELECT * FROM logs ORDER BY id DESC LIMIT 200").fetchall()

def get_alerts():
    with connect() as con:
        return con.execute("SELECT * FROM alerts ORDER BY id DESC LIMIT 100").fetchall()
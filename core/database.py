import sqlite3
import json
from utils.logger import get_logger

logger = get_logger()

def init_db(db_path="nmz_cache.db"):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS scans (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            target TEXT,
            timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
            results TEXT
        )
    ''')
    conn.commit()
    conn.close()

def save_scan_to_db(target, data, db_path="nmz_cache.db"):
    try:
        init_db(db_path)
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()
        cursor.execute("INSERT INTO scans (target, results) VALUES (?, ?)", (target, json.dumps(data)))
        conn.commit()
        conn.close()
    except Exception as e:
        logger.error(f"Database write error: {e}")

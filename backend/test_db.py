# backend/test_db.py
import datetime as dt
from backend.db import get_connection
from tabulate import tabulate

def main():
    cn = get_connection()
    cur = cn.cursor()

    # Yeni satır ekle
    cur.execute(
        "INSERT INTO readings(ts,device_id,parameter,value) VALUES (?,?,?,?)",
        dt.datetime.now(dt.UTC), "PLC1", "pressure", 3.14
    )
    cn.commit()

    # Son 5 satırı çek
    cur.execute("SELECT TOP 5 id, ts, device_id, parameter, value FROM readings ORDER BY id DESC")
    rows = cur.fetchall()
    headers = ["id", "timestamp", "device_id", "parameter", "value"]

    print(tabulate(rows, headers=headers, tablefmt="github"))
    cn.close()

if __name__ == "__main__":
    main()

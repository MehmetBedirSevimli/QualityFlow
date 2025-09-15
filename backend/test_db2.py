# backend/test_db2.py
from backend.db import get_connection
from tabulate import tabulate

def main():
    cn = get_connection()
    cur = cn.cursor()
    cur.execute(
        "INSERT INTO readings(ts,device_id,parameter,value) VALUES (SYSUTCDATETIME(), ?, ?, ?)",
        ("PLC2", "flow", 7.89)
    )
    cn.commit()
    cur.execute("SELECT TOP 5 id, ts, device_id, parameter, value FROM readings ORDER BY id DESC")
    rows = cur.fetchall()
    print(tabulate(rows, headers=["id","timestamp","device_id","parameter","value"], tablefmt="github"))
    cn.close()

if __name__ == "__main__":
    main()

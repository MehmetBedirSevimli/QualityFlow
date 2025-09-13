import pyodbc

# Baglanti bilgisi
conn = pyodbc.connect(
    "Driver={ODBC Driver 17 for SQL Server};"
    "Server=localhost;"
    "Database=QualityFlowDB;"
    "Trusted_Connection=yes;"
)

cursor = conn.cursor()

# 1. Veri ekle
cursor.execute(
    "INSERT INTO SensorData (SensorName, Value) VALUES (?, ?)",
    ("TempSensor", 25.3)
)
conn.commit()
print("Veri basariyla eklendi.")

# 2. Tabloyu oku
cursor.execute("SELECT Id, SensorName, Value, Timestamp FROM SensorData")
rows = cursor.fetchall()

print("Tablodaki kayitlar:")
for row in rows:
    print(row)

conn.close()

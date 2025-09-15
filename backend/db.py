# backend/db.py
import os
import pyodbc
from dotenv import load_dotenv

# .env dosyasını yükle
load_dotenv()

def get_connection():
    """
    .env dosyasındaki DSN üzerinden SQL Server bağlantısı kurar.
    """
    dsn = os.getenv("SQLSERVER_DSN")
    return pyodbc.connect(dsn)

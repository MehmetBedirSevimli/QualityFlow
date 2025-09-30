import time
import logging
import os
from plc_client import connect_plc, read_plc_data
from db_client import connect_db, insert_reading
from utils import setup_logging

def main():
    setup_logging()
    logging.info("Veri toplama servisi baslatiliyor...")

    plc = connect_plc()
    db_conn = connect_db()

    max_records = int(os.getenv("MAX_RECORDS", 0))  # 0 = sınırsız
    count = 0

    while True:
        try:
            readings = read_plc_data(plc)
            insert_reading(db_conn, "PLC_1", readings)

            #  Eklenen satır: Okunan degerleri logla
            logging.info(
                f"Temp={readings['temperature']:.2f} °C | "
                f"Pressure={readings['pressure']:.3f} bar | "
                f"MotorSpeed={readings['motorspeed']:.0f} rpm | "
                f"CycleCounter={readings['cyclecounter']}"
            )

            time.sleep(1)

            count += 1
            if max_records > 0 and count >= max_records:
                logging.info(f"{max_records} kayit alındı, collector duruyor.")
                break

        except Exception as e:
            logging.error(f"Dongu hatasi: {e}")
            time.sleep(5)

if __name__ == "__main__":
    main()

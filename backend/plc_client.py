# PLC baglanti ve veri okuma fonksiyonlari

import snap7
from snap7.util import get_real, get_dint
from snap7.exceptions import Snap7Exception
from snap7.types import Areas
import logging
import config

def connect_plc():
    plc = snap7.client.Client()
    try:
        logging.info("snap7 client olusturuluyor")
        logging.info(f"connecting to {config.PLC_IP}:102 rack {config.PLC_RACK} slot {config.PLC_SLOT}")
        plc.connect(config.PLC_IP, config.PLC_RACK, config.PLC_SLOT)

        if not plc.get_connected():
            raise Snap7Exception("PLC baglanti kurulamaz")
        logging.info("PLC baglantisi basarili.")
    except Snap7Exception as e:
        logging.error(f"PLC baglanti hatasi: {e}")
        raise
    return plc


def read_plc_data(plc):
    """
    PLC'den proses verilerini okur.
    - Areas.PE -> Process Inputs alanindan belirtilen byte sayisi okunur.
    - Donen sozluk icinde sensor/motor degerleri bulunur:
        - temperature (REAL)
        - pressure (REAL)
        - motorspeed (REAL)
        - cyclecounter (DINT)
    """
    try:
        # PLC'den PE alanindan config.DATA_SIZE kadar veri oku
        data = plc.read_area(Areas.PE, 0, 0, config.DATA_SIZE)

        return {
            "temperature": get_real(data, config.TEMP_OFFSET),
            "pressure": get_real(data, config.PRESSURE_OFFSET),
            "motorspeed": get_real(data, config.MOTORSPEED_OFFSET),
            "cyclecounter": get_dint(data, config.COUNTER_OFFSET),
        }
    except Exception as e:
        logging.error(f"PLC veri okuma hatasi: {e}")
        raise

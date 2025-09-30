# Loglama ve hata yönetimi

import logging

def setup_logging():
    """
    Proje için loglama ayarlarını yapar.
    - Log seviyesini INFO olarak belirler.
    - Log formatı: tarih-saat, seviye, mesaj
    - Log çıktısı hem dosyaya hem de konsola gider.
    """
    logging.basicConfig(
        level=logging.INFO,                           # INFO ve üstü logları yakala
        format="%(asctime)s [%(levelname)s] %(message)s",  # Log formatı
        handlers=[
            logging.FileHandler("collector.log", encoding="utf-8"),  # Dosyaya log yaz
            logging.StreamHandler()                                  # Konsola log yaz
        ]
    )

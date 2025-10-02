# backend/analyze.py
"""
Asama 4: Veri Isleme ve Analiz Ana Akisi
"""

import logging
from backend.analysis import (   # __init__.py sayesinde tek satir import
    load_data,
    preprocess,
    train_isolation_forest,
    detect_and_attach,
    evaluate_model,
    print_evaluation,
    export_to_onnx,
)
from backend import config


logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)


def main():
    # 1. Veriyi yukle
    df = load_data(limit=None)  # test icin limit=1000 kullanilabilir
    logging.info("Ham veri boyutu: %s satir", len(df))

    # 2. On isleme uygula
    df_processed, scaler = preprocess(df)
    logging.info("On islenmis veri boyutu: %s satir", len(df_processed))

    # 3. Ozellik matrisini hazirla
    feature_cols = ["temperature", "pressure", "motorspeed"]
    X = df_processed[feature_cols]

    # 4. Modeli egit (IsolationForest)
    model = train_isolation_forest(X)

    # 5. Anomali tespiti yap ve DataFrame'e ekle
    df_with_anomalies = detect_and_attach(model, X, df_processed)
    logging.info("Anomali etiketleri veriye eklendi")

    # 6. (Opsiyonel) Performans degerlendirme
    if "label" in df_with_anomalies.columns:  # eger gercek etiket varsa
        y_true = df_with_anomalies["label"]
        y_pred = df_with_anomalies["anomaly"]
        metrics = evaluate_model(y_true, y_pred)
        print_evaluation(metrics)

    # 7. Modeli ONNX olarak kaydet
    export_path = export_to_onnx(model, input_dim=len(feature_cols))
    logging.info("Model kaydedildi: %s", export_path)

    # 8. Kontrol icin ilk 5 satir ve anomaly sayilari yazdir
    print("\n=== Ilk 5 satir ===")
    print(df_with_anomalies.head())
    print("\n=== Anomali Dagilimi ===")
    print(df_with_anomalies["anomaly"].value_counts())


if __name__ == "__main__":
    main()

import pandas as pd
import numpy as np
from scipy.stats import ks_2samp
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

from app.repository import get_dataset_by_id

def compute_similarity(db,real_id, syn_id):

    real_dataset = get_dataset_by_id(db, real_id)
    synthetic_dataset = get_dataset_by_id(db, syn_id)
    real_df = pd.read_csv(real_dataset.file_path)
    syn_df = pd.read_csv(synthetic_dataset.file_path)

    numeric_cols = real_df.select_dtypes(include=np.number).columns

    # -------------------------------
    # 1. Distribution Similarity (KS Test)
    # -------------------------------
    ks_results = {}

    for col in numeric_cols:
        try:
            stat, p_value = ks_2samp(real_df[col], syn_df[col])
            ks_results[col] = {
                "statistic": float(stat),
                "p_value": float(p_value)
            }
        except:
            continue

    # -------------------------------
    # 2. Correlation Similarity
    # -------------------------------
    real_corr = real_df[numeric_cols].corr()
    syn_corr = syn_df[numeric_cols].corr()

    corr_diff = np.abs(real_corr - syn_corr).mean().mean()

    # -------------------------------
    # 3. Classifier Test
    # -------------------------------
    real_df["label"] = 0
    syn_df["label"] = 1

    combined = pd.concat([real_df, syn_df], ignore_index=True)

    combined = combined.dropna()
    X = combined[numeric_cols]
    y = combined["label"]

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3)

    clf = RandomForestClassifier()
    clf.fit(X_train, y_train)

    y_pred = clf.predict(X_test)
    acc = accuracy_score(y_test, y_pred)

    return {
        "ks_test": ks_results,
        "correlation_difference": float(corr_diff),
        "classifier_accuracy": float(acc)
    }

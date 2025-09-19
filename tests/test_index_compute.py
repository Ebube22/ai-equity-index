# tests/test_index_compute.py
import pandas as pd
from src.index.compute import compute_index

def test_compute_index_with_normals(tmp_path, monkeypatch):
    # Create a small features parquet
    df = pd.DataFrame({
        'fairness_combined_norm': [0.0, 0.5, 1.0],
        'gender_equity_index_norm': [1.0, 0.5, 0.0],
    })
    p = tmp_path / 'features.parquet'
    df.to_parquet(p, index=False)
    out_csv = tmp_path / 'out.csv'
    out_parquet = tmp_path / 'out.parquet'
    out = compute_index(str(p), str(out_csv), str(out_parquet))
    assert 'equity_index' in out.columns
    # The middle row should average to 50
    assert round(out.loc[1, 'equity_index'], 6) == 50.0

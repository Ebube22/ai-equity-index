# src/index/compute.py
import pandas as pd
from pathlib import Path

def compute_index(features_parquet: str = 'data/processed/features.parquet',
                  out_csv: str = 'data/processed/equity_index.csv',
                  out_parquet: str = 'data/processed/equity_index.parquet') -> pd.DataFrame:
    df = pd.read_parquet(features_parquet)
    norm_cols = [c for c in df.columns if c.endswith('_norm')]
    if not norm_cols:
        raise ValueError('No normalized columns found. Run src.features.engineering first and/or check your dataset.')
    df['index_compute_log'] = df[norm_cols].notna().sum(axis=1)
    df['equity_index'] = (df[norm_cols].mean(axis=1) * 100).clip(0, 100)
    Path(out_csv).parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(out_csv, index=False)
    df.to_parquet(out_parquet, index=False)
    return df[['equity_index', 'index_compute_log'] + norm_cols]

if __name__ == '__main__':
    out = compute_index()
    print('Computed equity_index. Head:\n', out.head())

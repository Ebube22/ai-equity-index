# src/index/export_powerbi.py
import pandas as pd
from pathlib import Path

def export_powerbi(in_parquet: str = 'data/processed/equity_index.parquet',
                   out_csv: str = 'powerbi/equity_index_export.csv') -> str:
    df = pd.read_parquet(in_parquet)
    keep_cols = [c for c in df.columns if c in [
        'equity_index','fairness_combined','gender_equity_index','inspection_norm','la_name','school_id','index_compute_log'
    ] or c.endswith('_norm')]
    export = df[keep_cols] if keep_cols else df
    Path(out_csv).parent.mkdir(parents=True, exist_ok=True)
    export.to_csv(out_csv, index=False)
    return out_csv

if __name__ == '__main__':
    path = export_powerbi()
    print('Exported for Power BI:', path)

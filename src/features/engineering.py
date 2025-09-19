# src/features/engineering.py
import pandas as pd
from pathlib import Path

# Simple bounds; adjust per research/bounds_literature.md
BOUNDS = {
    "fairness_combined": (0.0, 1.0),
    "gender_equity_index": (0.0, 1.0),
    "inspection_norm": (0.0, 1.0),
    "overall_exam_score_norm": (0.0, 1.0),
}

def clamp01(series, lo, hi):
    return series.clip(lower=lo, upper=hi)

def normalize_if_needed(series, lo, hi):
    # If values already appear in [0,1], return as is; else apply min-max to [0,1]
    s = series.astype('float')
    if s.min() >= 0 and s.max() <= 1:
        return s
    denom = (hi - lo) if (hi - lo) != 0 else 1.0
    return (s.clip(lo, hi) - lo) / denom

def run_features(input_csv: str = 'data/processed/refined_gender_equity_index.csv',
                 output_parquet: str = 'data/processed/features.parquet') -> pd.DataFrame:
    df = pd.read_csv(input_csv)
    # Determine which indicators exist
    indicators = [c for c in BOUNDS.keys() if c in df.columns]
    for col in indicators:
        lo, hi = BOUNDS[col]
        df[f'{col}_norm'] = normalize_if_needed(df[col], lo, hi)
    # Persist
    Path(output_parquet).parent.mkdir(parents=True, exist_ok=True)
    df.to_parquet(output_parquet, index=False)
    return df

if __name__ == '__main__':
    out = run_features()
    print('Features saved with normalized columns:', [c for c in out.columns if c.endswith('_norm')])

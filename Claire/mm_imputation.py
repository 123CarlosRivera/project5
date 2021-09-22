import pandas as pd
import numpy as np

def mm_impute(df, mode_cols, mean_cols):
    for col in df.columns:
        if col in mode_cols:
            mode = df[col].value_counts().index[0]
            if mode != np.nan:
                df[col] = df[col].fillna(value = mode)
            else:
                df[col] = df[col].fillna(value = df[col].value_counts().index[1])
        elif col in mean_cols:
            df[col] = df[col].fillna(value = df[col].mean())
    return df
import pandas as pd
import numpy as np

def segment_causal_uplift(df):
    res = df.copy()
    segments = []
    for _, row in res.iterrows():
        prob = row.get('Churn_Probability', row.get('Churn_Probability_%', 50.0) / 100.0 if 'Churn_Probability_%' in row else 0.5)
        active = row.get('IsActiveMember', 0)

        if prob >= 0.4 and active == 0:
            seg = '🎯 Persuadables'
        elif prob < 0.3:
            seg = '🔒 Sure Things'
        elif prob >= 0.75:
            seg = '❌ Lost Causes'
        else:
            seg = '⚠️ Sleeping Dogs'
        segments.append(seg)

    res['Causal_Segment'] = segments
    return res

import pandas as pd
import numpy as np

def predict_survival_timeline(current_prob):
    hazard_rate = 0.02 + (current_prob * 0.08)
    months = np.arange(1, 25)
    survival_probs = np.exp(-hazard_rate * months) * 100

    survival_df = pd.DataFrame({
        'Month': months,
        'Survival_Probability_%': np.round(survival_probs, 1)
    })

    below_50 = survival_df[survival_df['Survival_Probability_%'] < 50]
    if not below_50.empty:
        exp_months = int(below_50.iloc[0]['Month'])
    else:
        exp_months = 24

    prob_6m = float(survival_df[survival_df['Month'] == 6]['Survival_Probability_%'].iloc[0])

    if current_prob >= 0.6:
        category = "HIGH HAZARD ⚠️"
    elif current_prob >= 0.35:
        category = "MODERATE HAZARD ⚡"
    else:
        category = "LOW HAZARD ✅"

    return {
        'Expected_Months_Until_Churn': exp_months,
        'Prob_Survival_6M_%': prob_6m,
        'Hazard_Risk_Category': category,
        'Survival_Curve_DF': survival_df
    }

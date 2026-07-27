import numpy as np

def calculate_clv(balance, salary, num_products, tenure):
    base = float(salary) * 0.15 + float(balance) * 0.05
    product_multiplier = 1.2 if num_products == 2 else (0.8 if num_products > 2 else 1.0)
    tenure_multiplier = 1.0 + (tenure * 0.03)
    clv = base * product_multiplier * tenure_multiplier
    return max(500.0, float(clv))

def calculate_expected_retention_roi(clv, churn_prob, retention_cost=200.0, success_rate=0.4):
    expected_saved_value = clv * churn_prob * success_rate
    net_roi = expected_saved_value - retention_cost
    return {
        'Expected_Saved_CLV': round(expected_saved_value, 2),
        'Net_ROI': round(net_roi, 2),
        'ROI_Percentage': round((net_roi / retention_cost) * 100, 2) if retention_cost > 0 else 0.0
    }

def optimize_decision_threshold(res_df):
    best_threshold = 0.45
    max_profit = 0.0
    if 'Churn_Probability' in res_df.columns:
        probs = res_df['Churn_Probability'].values
        for th in np.linspace(0.1, 0.9, 17):
            predicted_churn = (probs >= th)
            saved = float(np.sum(predicted_churn) * (2500 * 0.30 - 150))
            if saved > max_profit:
                max_profit = saved
                best_threshold = round(float(th), 2)
    if max_profit == 0.0:
        max_profit = len(res_df) * 450.0
    return {
        'Optimal_Threshold': best_threshold,
        'Max_Net_Profit': float(max_profit)
    }

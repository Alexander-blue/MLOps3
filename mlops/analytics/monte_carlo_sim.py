import numpy as np
import pandas as pd

def run_monte_carlo_simulation(df_ana, n_trials=1000):
    np.random.seed(42)
    if 'Balance' in df_ana.columns:
        balances = df_ana['Balance'].values
    else:
        balances = np.array([50000.0, 85000.0, 120000.0])

    if 'Churn_Probability_%' in df_ana.columns:
        probs = df_ana['Churn_Probability_%'].values / 100.0
    else:
        probs = np.array([0.5, 0.3, 0.7])

    total_losses = []
    for _ in range(n_trials):
        churn_sim = np.random.rand(len(probs)) < probs
        loss = np.sum(balances[churn_sim])
        total_losses.append(loss)

    total_losses = np.array(total_losses)
    var_95 = float(np.percentile(total_losses, 95))

    return {
        'VaR_95_USD': round(var_95, 2),
        'Loss_Distribution': total_losses
    }

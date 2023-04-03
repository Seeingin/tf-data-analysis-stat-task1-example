import pandas as pd
import numpy as np


chat_id = 752592494

def solution(x: np.array) -> float:
    from scipy.optimize import minimize 

    def log_like(alpha, x):
      return np.sum(np.log(607 + np.random.lognormal(mean=np.log(alpha), sigma=1, size=len(x))) - x)

    result = minimize(lambda alpha: -log_like(alpha, x), x0=1, method='BFGS')
    return result.x[0]

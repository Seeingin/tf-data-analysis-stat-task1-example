import pandas as pd
import numpy as np


chat_id = 752592494

def solution(x: np.array) -> float:
    from scipy.stats import norm
    p = (x - 607).mean() / np.sqrt(np.var(x) / len(x))
    alpha = 1 - p
    return alpha

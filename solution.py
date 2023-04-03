import pandas as pd
import numpy as np


chat_id = 752592494

def solution(x: np.array) -> float:
    mu = np.log(np.mean(x) - 607)
    sigma = np.sqrt(np.log(1 + np.var(x) / np.power(np.mean(x) - 607, 2)))
    alpha = np.exp(mu - sigma**2 / 2)
    return alpha

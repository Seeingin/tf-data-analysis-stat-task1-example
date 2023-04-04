import pandas as pd
import numpy as np


chat_id = 752592494

def solution(x: np.array) -> float:
    loc = x.mean()
    unbiased_variance = np.var(x, ddof=1)
    alpha = np.log(unbiased_variance)
    return alpha

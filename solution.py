import pandas as pd
import numpy as np


chat_id = 752592494

def solution(x: np.array) -> float:
    return np.log(x - 607).mean()

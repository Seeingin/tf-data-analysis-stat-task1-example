import pandas as pd
import numpy as np


chat_id = 752592494

def solution(x: np.array) -> float:
    from scipy.optimize import minimize
    from scipy.stats import lognorm
    
    def log_likelihood(params, x):
        alpha, sigma = params
        mu = 607 + np.exp(alpha)
        log_pdf = lognorm.logpdf(x, sigma, scale=mu)
        return -np.sum(log_pdf)

    initial_guess = [0.5, 1.0]
    result = minimize(log_likelihood, initial_guess, args=(x,))
    alpha = result.x[0]
    return alpha

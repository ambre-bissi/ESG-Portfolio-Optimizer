import numpy as np
import pandas as pd

def annual_return(returns):
    return returns.mean() * 252

def annual_volatility(returns):
    return returns.std() * np.sqrt(252)

def sharpe_ratio(returns, risk_free_rate=0.02):
    annual_ret = annual_return(returns)
    annual_vol = annual_volatility(returns)
    return (annual_ret - risk_free_rate) / annual_vol

def max_drawdown(prices):

    cumulative = prices / prices.iloc[0]
    rolling_max = cumulative.cummax()
    drawdown = (cumulative - rolling_max) / rolling_max

    return drawdown.min()

def value_at_risk(returns,confidence=0.95):

    return np.percentile(returns,(1-confidence)*100)
  

def expected_shortfall(returns,confidence=0.95):
    var = value_at_risk(returns, confidence)
    return returns[returns <= var].mean()


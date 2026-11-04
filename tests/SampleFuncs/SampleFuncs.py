import xloil as xlo
import numpy as np

# Basic scalar function
@xlo.func
def Greeting(who: str) -> str:
    """Returns a greeting. Example: =Greeting("World")"""
    return f"Hello {who}!"

@xlo.func
def Adder(x: float, y: float) -> float:
    """Adds two numbers. Works with arrays too. Example: =Adder(10, 20)"""
    return x + y

# Array functions (excellent for financial data)
@xlo.func
def ArraySum(arr: xlo.Array(float)) -> float:
    """Sums a range. Example: =ArraySum(A12:A18)"""
    return float(np.nansum(arr))

@xlo.func
def WeightedAvg(values: xlo.Array(float), weights: xlo.Array(float)) -> float:
    """Weighted average. Example: =WeightedAvg(A12:A18, B12:B18)"""
    values = np.asarray(values).flatten()
    weights = np.asarray(weights).flatten()
    if values.size == 0 or weights.size == 0:
        return float('nan')
    return float(np.average(values, weights=weights))

@xlo.func
def SimpleReturn(end: float, start: float) -> float:
    """Simple return (end/start - 1). Example: =SimpleReturn(107.5, 100)"""
    if start == 0:
        return float('nan')
    return end / start - 1

@xlo.func
def LogPrices(prices: xlo.Array(float)) -> xlo.Array(float):
    """Natural log of a price series (returns array). Example: =LogPrices(A12:A18)"""
    arr = np.asarray(prices, dtype=float)
    return np.log(arr)

@xlo.func
def EnvInfo():
    """Returns the Python executable and whether pandas can be imported."""
    import sys
    try:
        import pandas as pd
        pandas_ver = pd.__version__
    except Exception as e:
        pandas_ver = f"FAILED: {type(e).__name__}: {e}"
    return f"exe={sys.executable} | pandas={pandas_ver}"

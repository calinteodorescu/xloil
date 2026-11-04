import SampleFuncs

try:
    import get_candle_value
except Exception as e:
    import xloil as xlo
    xlo.log.error(f"get_candle_value import failed: {type(e).__name__}: {e}")
    raise
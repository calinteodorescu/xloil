import xloil as xlo

try:
    xlo.log.debug(f"##### trying to import SampleFuncs")
    import SampleFuncs
except Exception as e:
    xlo.log.error(f"SampleFuncs import failed: {type(e).__name__}: {e}")
    raise

try:
    xlo.log.debug(f"##### trying to import get_candle_value")
    import get_candle_value
except Exception as e:
    xlo.log.error(f"get_candle_value import failed: {type(e).__name__}: {e}")
    raise
import xloil as xlo

import debugpy
debugpy.listen(("localhost", 5678))
# Optional: uncomment the next line if you want Excel to wait until VS Code attaches
# debugpy.wait_for_client()

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
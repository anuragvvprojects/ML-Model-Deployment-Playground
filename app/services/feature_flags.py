import os
def is_enabled(flag: str) -> bool:
    return os.getenv(f"FLAG_{flag.upper()}", "false").lower() in ("1","true","yes","on")

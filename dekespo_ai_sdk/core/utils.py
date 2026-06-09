import sys

ERROR_PRINT_CONFIG = {"enabled": True}

def error_print(*args, **kwargs):
    if not ERROR_PRINT_CONFIG["enabled"]:
        return
    print(*args, file=sys.stderr, **kwargs)

def disable_error_print():
    ERROR_PRINT_CONFIG["enabled"] = False

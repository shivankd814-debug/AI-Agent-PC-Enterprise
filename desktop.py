from app.config import settings

def get_desktop_status():
    if not settings.allow_desktop_control:
        return {"enabled": False, "message": "Desktop control is disabled by default."}
    try:
        import pyautogui
        return {"enabled": True, "screen": list(pyautogui.size())}
    except Exception as exc:
        return {"enabled": False, "message": str(exc)}

def move_mouse(x: int, y: int):
    if not settings.allow_desktop_control:
        raise RuntimeError("Desktop control disabled.")
    if not (0 <= x <= 10000 and 0 <= y <= 10000):
        raise ValueError("Coordinates out of allowed range.")
    import pyautogui
    pyautogui.moveTo(x, y, duration=0.2)
    return {"moved": True, "x": x, "y": y}

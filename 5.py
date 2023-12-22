def time_since_midnight(time_str):
    match = re.match(r'^(\d{2}):(\d{2})(?::(\d{2})(?:\.(\d+))?)?$', time_str)
    if not match:
        return "Помилка"
    hours, minutes, seconds, ms = match.groups(default="0")
    if not (0 <= int(hours) < 24 and 0 <= int(minutes) < 60 and 0 <= int(seconds) < 60 and 0 <= int(ms) < 1000):
        return "Помилка"
    total_seconds = int(hours) * 3600 + int(minutes) * 60 + int(seconds)
    return total_seconds
from datetime import datetime, timedelta


def current_unix_time():
    """Возвращает текущее время по Unix time."""
    return datetime.now().timestamp()


def next_hour_unix_time():
    """Возвращает текущее время по Unix time + час."""
    return (datetime.now() + timedelta(hours=1)).timestamp()

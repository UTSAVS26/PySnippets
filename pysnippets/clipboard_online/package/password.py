from datetime import datetime


def valid_password(password: int) -> bool:
    current_time = int(datetime.now().strftime("%H%M"))
    return password == current_time

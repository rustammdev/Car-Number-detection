import datetime

def get_datetime_string():
    now = datetime.datetime.now()
    return now.strftime("%Y-%m-%d_%H:%M")

# Foydalanish
datetime_str = get_datetime_string()
print(datetime_str)  # 2024-06-12 12:34:56
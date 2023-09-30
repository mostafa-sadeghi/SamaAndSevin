"""
30              =>      30s
60              =>      1m
90              =>      1m 30s
3600            =>      1h
3601            =>      1h 1s
90042           =>      25h 42s


"""


def get_hours_minutes_seconds(total_seconds):
    if total_seconds >= 3600:
        hours = total_seconds//3600
        total_seconds = total_seconds % 3600
    else:
        hours = 0

    if total_seconds >= 60:
        minutes = total_seconds // 60
        total_seconds = total_seconds % 60
    else:
        minutes = 0

    seconds = total_seconds
    return (str(hours)+'h', str(minutes) + 'm', str(seconds)+'s')


print(get_hours_minutes_seconds(60))
print(get_hours_minutes_seconds(61))
print(get_hours_minutes_seconds(3600))
print(get_hours_minutes_seconds(3601))

# TODO   به خروجی های عددی کاراکتر های
# h , m , s
# را بچسبانید
# 1h  1m  1s

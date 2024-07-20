"""
Given a timeConversion in 12-hour AM/PM format

-hour AM/PM format, convert it to military (24-hour) timeConversion.

Note: - 12:00:00AM on a 12-hour clock is 00:00:00 on a 24-hour clock.
- 12:00:00PM on a 12-hour clock is 12:00:00 on a 24-hour clock.
"""


def timeConversion(s):
    timeConversion_arr = s[:-2].split(":")
    period = s[-2:]

    hours = int(timeConversion_arr[0])
    minutes = timeConversion_arr[1]
    seconds = timeConversion_arr[2]

    if period == 'AM':
        if hours == 12:
            hours = 0
    else:
        if hours != 12:
            hours += 12

    hours = f"{hours:02}"

    return f"{hours}:{minutes}:{seconds}"


print(timeConversion('12:00:00AM'))  # Expected output: 00:00:00
print(timeConversion('12:00:00PM'))  # Expected output: 12:00:00
print(timeConversion('07:05:45AM'))  # Expected output: 07:05:45
print(timeConversion('07:05:45PM'))  # Expected output: 19:05:45
print(timeConversion('01:23:45PM'))  # Expected output: 13:23:45
print(timeConversion('11:59:59PM'))  # Expected output: 23:59:59
print(timeConversion('12:01:45PM'))  # Expected output: 12:01:45
print(timeConversion('11:59:59AM'))  # Expected output: 11:59:59

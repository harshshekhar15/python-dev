
from typing import List


def maxHoliday(holidays: List[str], x: int):
    n = len(holidays)
    holiday_perm = []
    while x < n:
        print(f"***\nx={x}\n")
        for i in range(0, n):
            print(f"i -->{i}")
            if i+x > n:
                holiday = holidays[i:n]
                rest = holidays[:i+x-n]
                holiday = holiday + rest
            else:
                holiday = holidays[i:i+x]
            print(f"holiday --> {holiday}")
            holiday_perm.append(holiday)
        x += 1
        print("***\n")
    holiday_perm.append(holidays)
    return holiday_perm

holidayList = ["Jan-1", "Jan-26", "Aug-15", "Aug-1", "Dec-25"]
x = 3
# holidayList = ["Jan-1", "Jan-26", "Aug-15"]
# x = 1
print(maxHoliday(holidayList, x))
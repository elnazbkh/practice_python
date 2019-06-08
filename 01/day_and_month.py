# date based on day number
daynum = int(input("enter number of day:"))
Day = 0
Month = 0

if 0 < daynum < 186:
    Month = (daynum // 31) + 1
    Day = daynum % 31
elif 186 < daynum < 365:
    daynum -= 186
    Month = (daynum // 30) + 7
    Day = daynum % 30
else:
    print("the number is out of range")

print("the date is:", Month, ".", Day)
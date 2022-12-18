def timeConversion(s):
    # Write your code here
    twelve_clock = s[:2]
    day_night = s[-2:]
    
    if twelve_clock == '12':
        if day_night == 'PM' or 'pm':
            new_time = s[:-2]
            return new_time
        else:
            new_time = str(int(s[:2]) - 12)+s[2:-2]
            return new_time
        
    elif day_night == 'PM' or 'pm':
        new_time = str(int(s[:2]) + 12)+s[2:-2]

    return new_time

time1 = '12:40:22AM'
time2 = "07:05:45PM"
print(timeConversion(time1))
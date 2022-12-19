def timeConversion(s):
    # Write your code here
    twelve_clock = s[:2]
    day_night = s[-2:]
    
    if twelve_clock == '12':
        if day_night == 'PM':
            new_time = s[:-2]
            return new_time
        else:
            new_time = '00'+s[2:-2]
            return new_time
        
    elif day_night == 'PM':
        new_time = str(int(s[:2]) + 12)+s[2:-2]
        return new_time
    elif day_night == 'AM':
        new_time = s[:-2]
        return new_time

time1 = '12:40:22PM'
time2 = "07:05:45PM"
time3 = "12:40:22AM"
time4 = "06:40:03AM"
time5 = "12:05:39AM"
time6 = "12:00:00AM" 
print(timeConversion(time5))
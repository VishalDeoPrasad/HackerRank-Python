def timeConversion(s):
    h = s[:2]
    m = s[3:5]
    ss = s[6:8]
    time_format = s[8:]
    
    if time_format == "AM":
        if h != "12":
            return s[:8]
        else:
            return "00"+s[2:8]
        
    elif time_format == "PM":
        if h != "12":
            h = str(int(h)+12)
            return h+s[2:8]
        else:
            return s[:8]
    
print(timeConversion("07:05:45PM"))
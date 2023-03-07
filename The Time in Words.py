def timeInWords(h, m):
    time_dict = { 
                0: "o' clock", 1:"one", 2:"two", 3:"three", 4:"four", 5:"five", 6:"six", 7:"seven", 8:"eight",  
                9:"nine", 10:"ten", 11:"eleven", 12:"twelve", 13:"thirteen", 14:"fourteen", 15:"quarter", 
                16:"sixteen", 17:"seventeen", 18:"eighteen", 19:"nineteen", 20:"twenty", 21:"twenty one", 
                22:"twenty two", 23:"twenty three", 24:"twenty four", 25:"twenty five", 26:"twenty six", 
                27:"twenty seven", 28:"twenty eight", 29:"twenty nine", 30:"half" }
    if m <= 30:
        if m == 0:
            return (time_dict[h]+" "+"o' clock")
        if m == 1:
            return time_dict[m]+" "+"minute past"+" "+(time_dict[h])
        elif m == 15:
            return time_dict[m]+" "+"past"+" "+(time_dict[h])
        elif m == 30:
            return time_dict[m]+" "+"past"+" "+(time_dict[h])
        else:
            return time_dict[m]+" "+"minutes past"+" "+(time_dict[h])
        
    else:
        if m == 45:
            return time_dict[60-m]+" "+"to"+" "+(time_dict[h+1])
            
        return time_dict[60-m]+" "+"minutes to"+" "+(time_dict[h+1])

print(timeInWords(5,47))
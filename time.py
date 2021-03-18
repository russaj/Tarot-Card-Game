import time
import calendar

localtime = time.localtime(time.time())
##print(localtime)

month = localtime[1];
fullDate = localtime[2], month
##print(fullDate)

if 1 < fullDate[1] < 2:
    print("January")


month = calendar.month_name[month]
day = localtime[2];




#for month_idx in range(1, 13):
    #print (calendar.month_name[month_idx])
    ##print (calendar.month_abbr[month_idx])
    ##print ("")



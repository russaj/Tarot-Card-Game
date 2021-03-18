import time
import calendar

localtime = time.localtime(time.time())
##print(localtime)

month = calendar.month_name[localtime[1]]
fullDate = localtime[2], month
##print(type(fullDate))

currentDate = int(str(localtime[1]) + str(localtime[2]))

if 120 <= currentDate <= 218:
    print("Aquarius")
elif 219 <= currentDate <= 320:
    print("Pisces")
elif 321 <= currentDate <= 419:
    print("Aries")
elif 420 <= currentDate <= 520:
    print("Taurus")
elif 521 <= currentDate <= 620:
    print("Gemini")
elif 621 <= currentDate <= 722:
    print("Cancer")
elif 723 <= currentDate <= 822:
    print("Leo")
elif 823 <= currentDate <= 922:
    print("Virgo")
elif 923 <= currentDate <= 1022:
    print("Libra")
elif 1023 <= currentDate <= 1121:
    print("Scorpio")
elif 1122 <= currentDate <= 1221:
    print("Sagittarius")
else:
    print("Capricorn")




##if 1 < fullDate[1] < 2:
##    print("January")

##print(month)
##day = localtime[2];
##print(day)



##for month_idx in range(1, 13):
##    print (calendar.month_name[month_idx])

    ##print (calendar.month_abbr[month_idx])
    ##print ("")

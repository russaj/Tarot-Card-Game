import time
import calendar

localtime = time.localtime(time.time())
##print(localtime)

month = calendar.month_name[localtime[1]]
fullDate = localtime[2], month
##print(type(fullDate))

currentDate = int(str(localtime[1]) + str(localtime[2]))

def currentZodiacSign(currentDate):
    if 120 <= currentDate <= 218:
        return "Aquarius"
    elif 219 <= currentDate <= 320:
        return "Pisces"
    elif 321 <= currentDate <= 419:
        return "Aries"
    elif 420 <= currentDate <= 520:
        return "Taurus"
    elif 521 <= currentDate <= 620:
        return "Gemini"
    elif 621 <= currentDate <= 722:
        return "Cancer"
    elif 723 <= currentDate <= 822:
        return "Leo"
    elif 823 <= currentDate <= 922:
        return "Virgo"
    elif 923 <= currentDate <= 1022:
        return "Libra"
    elif 1023 <= currentDate <= 1121:
        return "Scorpio"
    elif 1122 <= currentDate <= 1221:
        return "Sagittarius"
    else:
        return "Capricorn"

def zodiacSign(birthDate):
    if 120 <= currentDate <= 218:
        return "Aquarius"
    elif 219 <= currentDate <= 320:
        return "Pisces"
    elif 321 <= currentDate <= 419:
        return "Aries"
    elif 420 <= currentDate <= 520:
        return "Taurus"
    elif 521 <= currentDate <= 620:
        return "Gemini"
    elif 621 <= currentDate <= 722:
        return "Cancer"
    elif 723 <= currentDate <= 822:
        return "Leo"
    elif 823 <= currentDate <= 922:
        return "Virgo"
    elif 923 <= currentDate <= 1022:
        return "Libra"
    elif 1023 <= currentDate <= 1121:
        return "Scorpio"
    elif 1122 <= currentDate <= 1221:
        return "Sagittarius"
    else:
        return "Capricorn"

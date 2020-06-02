# Time Calculator

time = int(input('Enter in the number of seconds: '))

if time < 60:
    print('Time entered in seconds is', time)

if time >= 60 and time < 3600:
    seconds = time % 60
    minutes = time // 60

    print('\nMinute(s): ', minutes)
    print('Second(s): ', seconds)

elif time >= 3600 and time < 86400:
    seconds = time % 60
    minutes = ((time % 3600) // 60)
    hours = time // 3600

    print('\nHour(s): ', hours)
    print('Minute(s): ', minutes)
    print('Second(s): ', seconds)

elif time >= 86400:
    seconds = time % 60
    minutes = (((time % 86400) % 3600) // 60)
    hours = ((time % 86400) // 3600)
    days = time // 86400

    print('\nDay(s): ', days)
    print('Hour(s): ', hours)
    print('Minute(s): ', minutes)
    print('Second(s): ', seconds)
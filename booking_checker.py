from datetime import datetime, timedelta

def is_available_date(booked_dates, date_for_booking):
    booked = []
    want_to_book = []
    for dt in booked_dates:
        if '-' not in dt:
            booked.append(datetime.strptime(dt, '%d.%m.%Y'))
        else:          
            start, end = dt.split('-')
            start = datetime.strptime(start, '%d.%m.%Y')
            end = datetime.strptime(end, '%d.%m.%Y')
            delta = end - start
            for i in range(delta.days + 1):
                booked.append(start + timedelta(i))

    
    if '-' not in date_for_booking:
        want_to_book.append(datetime.strptime(date_for_booking, '%d.%m.%Y'))
    else:
        for dt in date_for_booking:            
            start, end = date_for_booking.split('-')
            start = datetime.strptime(start, '%d.%m.%Y')
            end = datetime.strptime(end, '%d.%m.%Y')
            delta = end - start
            for i in range(delta.days + 1):
                want_to_book.append(start + timedelta(i))

    return len(set(booked).intersection(set(want_to_book))) == 0

# TEST_11:
dates = ['01.11.2021', '05.11.2021-09.11.2021', '12.11.2021', '15.11.2021-21.11.2021']
some_date = '10.11.2021-14.11.2021'
print(is_available_date(dates, some_date))

# TEST_12:
dates = ['01.11.2021', '05.11.2021-09.11.2021', '12.11.2021', '15.11.2021-21.11.2021']
some_date = '03.11.2021-05.11.2021'
print(is_available_date(dates, some_date))

# TEST_13:
dates = ['01.11.2021', '05.11.2021-09.11.2021', '12.11.2021', '15.11.2021-21.11.2021']
some_date = '09.11.2021-10.11.2021'
print(is_available_date(dates, some_date))

# TEST_14:
dates = ['01.11.2021', '05.11.2021-09.11.2021', '12.11.2021', '15.11.2021-21.11.2021']
some_date = '06.11.2021-08.11.2021'
print(is_available_date(dates, some_date))

# TEST_15:
dates = ['01.11.2021', '05.11.2021-09.11.2021', '12.11.2021', '15.11.2021-21.11.2021']
some_date = '14.11.2021-22.11.2021'
print(is_available_date(dates, some_date))

# TEST_16:
dates = ['14.09.2022-14.10.2022']
some_date = '20.09.2022'
print(is_available_date(dates, some_date))

# TEST_17:
dates = ['14.09.2022-14.10.2022']
some_date = '14.11.2022'
print(is_available_date(dates, some_date))

# TEST_18:
dates = ['14.09.2022-14.10.2022']
some_date = '15.11.2022-16.11.2022'
print(is_available_date(dates, some_date))

# TEST_19:
dates = ['14.09.2022-14.10.2022']
some_date = '14.09.2022-22.09.2022'
print(is_available_date(dates, some_date))

# TEST_20:
dates = ['02.11.2021', '05.11.2021-09.11.2021']
some_date = '04.11.2021'
print(is_available_date(dates, some_date))


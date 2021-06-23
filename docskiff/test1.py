from datetime import timedelta, datetime


def get_sat_date(start_date=None, end_date=None):
    """
    This function returns list of dates that satisfy exactly one of the following conditions-
    1 The day is the 4th Saturday of the month.
    2 The day is Saturday and the date is multiple of 5.
    :param start_date:str
    :param end_date:str
    :return:list
    """

    if not (start_date and end_date):
        raise ValueError('start_date and/or end_date can not be empty!')
    if len(start_date) != 8 or len(end_date) != 8:
        raise ValueError("start_date and end_date should be in the format of 'YYYYMMDD'!")

    start_date = datetime.strptime(start_date, '%Y%m%d')
    end_date = datetime.strptime(end_date, '%Y%m%d')

    if not ((1900 <= start_date.year <= 2100) and (1900 <= end_date.year <= 2100)):
        raise ValueError("Input dates should belong the year 1900 to 2100!")

    next_sat = start_date + timedelta((7 + 5 - start_date.weekday()) % 7)  # get next Saturday
    no_of_days = (end_date - next_sat).days + 1  # total no of days in interval
    data = []
    for index in range(0, no_of_days, 7):
        sat_date = next_sat + timedelta(days=index)
        if (sat_date.day in range(22, 29)) ^ (sat_date.day % 5 == 0):
            data.append(sat_date.strftime('%Y%m%d'))

    return data


if __name__ == '__main__':
    try:
        dates = get_sat_date('20180728', '20180927')
    except ValueError as e:
        print(e)
    else:
        print(*dates, sep='\n')

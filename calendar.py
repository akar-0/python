"""Several functions to manipulate calendar values"""


def leapYear(y):
    """
    Find out whether a year is leap year or not.

    Parameters
    ---------
    y (int): year

    Returns
    -------
    True (bool) if year is a leap year, False otherwise.
    """

    if (y % 400) == 0:
        return True
    elif (y % 100) == 0:
        return  False
    elif (y % 4) == 0:
        return  True
    else:
        return  False


def readDate():
    """
    Retrieve date from user in format yyyy/mm/dd and check that entered values
    are correct.

    Parameters
    ---------
    None.

    Returns
    ------
    [y, m, d] (list), with:

    y (int): year
    m (int): month
    d (int): day

    Returned values are checked so that they match with an actually valid date
    (the program loops until entered values are correct).
    """

    months_31 = (1, 3, 5, 7, 8, 10, 12)
    error = "This is not a correct value."
    prompt_y = "Please enter a year:\n\t> "
    prompt_m = "Please enter a month:\n\t> "
    prompt_d = "Please enter a day:\n\t> "

    # Read a correct year from user.
    while True:
        y = input(prompt_y)
        try:
            y= float(y)
            if y < 1 or int(y) != y:
                float('')
        except:
            print(error)
        else:
            y = int(y)
            break
    # Check leap year:
    leap = leapYear(y)

    # Read a correct month from user.
    while True:
       m = input(prompt_m)
       try:
          m = float(m)
          if int(m) != m or m < 1 or m > 12:
              float('')
       except:
           print(error)
       else:
           m = int(m)
           break

    # Read a correct day from user.
    while True:
        d = input(prompt_d)
        try:
            d = float(d)
            if d < 1 or d > 31 or d != int(d):
                float('')
            elif m not in months_31:
                if m == 2:
                    if d > 29 and leap:
                        float('')
                    elif d > 28 and not leap:
                        float('')
                else:
                    if d == 31:
                        float('')
            d= int(d)
        except:
            print(error)
        else:
            break

    return [y, m, d]


def gregorianToOrdinalDate(y, m, d):
    """
    Find ordinal date from Gregorian date.

    Parameters
    ---------
    y (int): month
    m (int): month
    d (int): day

    Returns
    ------
    rank (int): ordinal date of the day within the year.

    """
    months_31 = (1, 3, 5, 7, 8, 10, 12)

    if leapYear(y):
        gap = 1
    else:
        gap = 0

    if m == 1:
        rank = d
    elif m == 2:
        rank = 31 + d
    else:
        rank = 59 + gap + d
        for month in range(3, m):
            if month in months_31:
                rank = rank + 31
            else:
                rank = rank + 30

    return rank


def ordinalToGregorianDate(y, rank):
    """
    Find Gregorian date from ordinal date.

    Parameters
    ---------
    y (int): year.
    rank (int): ordinal day within the year.

    Returns
    ------
    [m, d] (list) with:
    m (int): month
    d (int): day

    """


    months_lengths = (31, 
                      (28 + (leapYear(y) * 1)), 
                      31, 
                      30, 
                      31, 
                      30, 
                      31, 
                      31, 
                      30,
                      31,
                      30,
                      31)

    m = 1
    lim = 31
    d = rank

    for n in range(0, 11):
        if rank > lim:
            lim += months_lengths[n + 1]
            m += 1
            d -= months_lengths[n]
        else:
            break

    return [m, d]


def dateToWeekDay(y, m, d):
    """
    Find day of the week from Gregorian date.

    Parameters
    ---------
    d (int): day
    m (int): month
    y (int): month

    Returns
    ------
    day (str): day of the week.

    """

    # Rank of the day compared to January first.
    rank = gregorianToOrdinalDate(y, m, d) - 1

    # Day for January 1.
    d1 = (y + ((y - 1) // 4) \
          - ((y - 1) // 100) \
          + ((y - 1) // 400)) \
          % 7

    # Day.
    day = (rank + d1) % 7

    if day == 0:
        day = 'Sunday'
    elif day == 1:
        day = 'Monday'
    elif day == 2:
        day = 'Tuesday'
    elif day == 3:
        day = 'Wednesday'
    elif day == 4:
        day = 'Thursday'
    elif day == 5:
        day = 'Friday'
    else:
        day = 'Saturday'

    return day

def lengthYear(y):
    """
    Returns the number of days within the year given as argument (both as int
    values).
    """
    return 365 + (leapYear(y) * 1)


def dateToDate(y, m, d, n):
    """
    Find the date n days before (if n is negative) or after (if positive)
    a given date.

    Parameters
    ---------
    y (int), m (int), d (int) respectively year/month/day of a date.
    n (int): gap between the entered date and the date to be computed.

    Returns
    ------
    [y, m, d] (list): list of int corresponding to the searched date with
    format year/month/day respectively.
    """

    rank = gregorianToOrdinalDate(y, m, d) + n

    if rank > 0:
        while rank > lengthYear(y):
            rank -= lengthYear(y)
            y += 1
    else:
        while rank < 0:
            y -= 1
            rank += lengthYear(y)

    date = ordinalToGregorianDate(y, rank)

    return [y, date[0], date[1]]


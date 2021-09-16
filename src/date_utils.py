from datetime import date, timedelta

def workday(from_date: date, offset: int) -> date:
    """ Return the offset workday from the specific date
    """
    direction = offset//abs(offset)
    for _ in range(0, offset, direction):
        from_date += timedelta(days=direction)
        while from_date.weekday() == 5 or from_date.weekday() == 6:
            from_date += timedelta(days=direction)

    return from_date
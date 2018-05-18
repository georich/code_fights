"""Solution for centuryFromYear."""


def century_from_year(year: int) -> int:
    """Figure out which century a given year would be in."""
    if year % 100 == 0:
        return year // 100
    else:
        return (year // 100) + 1

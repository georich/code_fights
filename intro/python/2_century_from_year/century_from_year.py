def century_from_year(year):
    if year % 100 == 0:
        return year // 100
    else:
        return (year // 100) + 1


year = 2405
print(f"{year} is in the {century_from_year(year)}th century.")

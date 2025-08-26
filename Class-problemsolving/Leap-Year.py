
def is_leap(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return f'{year} True'
            else:
                return f'{year} False'
        else:
            return f'{year} True'
    else:
        return f'{year} False'

year = 2025
print(is_leap(year))
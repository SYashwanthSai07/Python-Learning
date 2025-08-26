'''
name = input('name:')
name = name.upper()
a = 'hello'
b = f'{a} {name} Welcome to the Python Programming Language'
print(b)



a=[1, 2, 3, 4, 5]
b= [6, 7, 8, 9, 10]
a.insert(5, b[:])
print(a)

x=0
for i in range(1,101):
    print(i)
    x += 1
    if i == 100:
        print('End of the loop')
        break
print('Loop completed')

x = 0
while x < 100:   
    print(x)
    x += 1
    if x == 50:
        print('End of the loop')
        break 
    print('Loop completed')
    
def year_calculator(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return f'{year} is a leap year'
            else:
                return f'{year} is not a leap year'
        else:
            return f'{year} is a leap year'
    else:
        return f'{year} is not a leap year'
year = int(input('Enter a year: '))
print(year_calculator(year))

def prime_number_checker(num):
    if num > 1:
        for i in range(2, int(num/2)+1):
            if (num % i) == 0:
                return f'{num} is not a prime number'
        else:
            return f'{num} is a prime number'
    else:
        return f'{num} is not a prime number'
num = int(input('Enter a number: '))
print(prime_number_checker(num))

def days_in_month(month, year):
    month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if month < 1 or month > 12:
        return 'Invalid month'
    if month == 2:
        if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
            return 29
        else:
            return 28
    else:
        return month_days[month - 1]
month = int(input('Enter month (1-12): '))
year = int(input('Enter year: '))
day = int(input('Enter day: '))
print("That Month contains"+days_in_month(month, year))
def day_of_week(day, month, year):
    if month < 3:
        month += 12
        year -= 1
    k = year % 100
    j = year // 100
    f = day + ((13 * (month + 1)) // 5) + k + (k // 4) + (j // 4) - (2 * j)
    day_of_week = f % 7
    days = ['Saturday', 'Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
    return days[day_of_week]  
print(day_of_week(day, month, year))
'''
x=0
for i in range(1,99999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999):
    print(i)
    x += 1

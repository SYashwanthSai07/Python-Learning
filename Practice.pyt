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
'''
repeat_pattern = 3
print(("Python" + "* * *")*repeat_pattern)
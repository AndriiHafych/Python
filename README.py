y1 = int(input())
y2 = int(input())
y3 = int(input())
x1 = int(input())
x2 = int(input())

max = int()
min = int()
if x1 >= x2:
    max = x1
    min = x2
else:
    max = x2
    min = x1
if y1 >= y2 and y1 >= y3:
    if y2 <= max and y3 <= min or y3 <= max and y2 <= min:
        print("YES")
    else:
        print('NO')
elif y2 >= y1 and y2 >= y3:
    if y1 <= max and y3 <= min or y3 <= max and y1 <= min:
            print("YES")
    else:
            print('NO')
elif y3 >= y1 and y3 >= y2:
    if y1 <= max and y2 <= min or y2 <= max and y1 <= min:
        print("YES")
    else:
        print('NO')

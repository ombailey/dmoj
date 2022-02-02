# Input a year and output the year that follows that has distinct digits (no digits are the same for example : 2014)
# Need a program that reads each "year" and if the year doesn't have distinct digits to keep adding until it finds one that does.

y = input()
x = [int(a) for a in y]
newyear = []

while int(y) <=  100000:
    y = int(y) + 1
    y = str(y)
    x = [int(a) for a in y]
    for digit in x:
        if digit not in newyear:
            newyear.append(digit)
    if len(newyear) != len(x):
        newyear = []
        continue  
    if len(newyear) == len(x):
        break

final = int(''.join(map(str,newyear)))
print(final)
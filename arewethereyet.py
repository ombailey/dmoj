x = input()
city = x.split()
distance_city = []
for number in city:
    distance_city.append(int(number))
y = []
num = 0 
a = 0 
y.append([0])
index = 0
for distance in distance_city:
    a += distance
    y.append([a])

def distance(num):
    index = 0
    for number in range(5):
        if (0 in y[index]) == True:
            d = y[index][num] + distance_city[num]
        else:
            d = y[index][num] - distance_city[num]
        y[index].append(d)
        index +=1
distance (0)
distance(1)
distance(2)
distance(3)

for number in range(5):
    z = [str(int) for int in y[number]] 
    a = ' '.join(z)
    print (a)
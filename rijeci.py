num_buttonpressed = int(input())
A = 0
B = 0
letters = ''

for number in range(0, num_buttonpressed) :

	character = number % 2


	if number == 0:
		B = B + 1
		letters = letters + 'B'
		continue

	if number == 1:
		A = A + 1
		letters = letters + 'A'
		continue


	if number > 0 and character > 0:

		B = B + 1
		A = A + 1
		letters = letters + 'BA'	

	else:
		B = B + 1
		letters = letters + 'B'

letters.replace('A', 'B')
letters.replace('B', 'BA')

print(character)

print (A, B)

print(letters)
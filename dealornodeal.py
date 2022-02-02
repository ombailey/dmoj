briefcases = [100, 500, 1000, 5000, 10000, 25000, 50000, 100000, 500000, 1000000]
briefcasesremoved = []
 
casesopened = int(input())
for number in range(casesopened):
		removed = int(input())
		briefcasesremoved.append(briefcases[removed -1])
		
for value in range(len(briefcasesremoved)):
	briefcases.remove(briefcasesremoved[value])	

totalvalueleft = sum(briefcases) // len(briefcases)

offer = int(input())
if offer > totalvalueleft:
	print ('deal')
else:
	print ('no deal')
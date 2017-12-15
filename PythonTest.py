'''
Questions

1.Given two lists L1 = ['a','b','c'], L2 = ['b','d'], find common elements, find elements present in L1
and not in L2?
2. How many Thursdays were there between 1990 - 2000?
'''

# Solution 1

L1 = ['a', 'b', 'c']

L2 = ['b', 'd']

common = []
L1only = []

for element in L1:
	if element in L2:
		common.append(element)
	else:
		L1only.append(element)

print('Solution 1')
print('Common elements =', common)
print('Elements in L1 and not in L2 =', L1only)

# Solution 2

#NO of days between 1990 and 2000

days = 0
for i in range(1990,2000):
	if i%4 == 0:
		days += 366
	else:
		days += 365

# As 1st january 1990 was a monday, we subtract 3 to number of days to keep the starting day as thursday

days -= 3

# no of weeks therefore will give the number of thursdays

thursdays = int(days/7)

print('\nSolution 2')
print('No of thursdays =', thursdays)
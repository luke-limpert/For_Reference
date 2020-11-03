#example of list comprehension

my_list = []
for number in range(0,1000):
	if number % 2 == 0:
		my_list.append(number)

print(my_list)

#list comprehension format

my_list = [number for number in range(0,1000) if number % 2 == 0]
print(my_list)
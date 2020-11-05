#example of list comprehension

my_list = []
for number in range(0,1000):
	if number % 2 == 0:
		my_list.append(number)

print(my_list)

#list comprehension format

my_list = [number for number in range(0,1000) if number % 2 == 0]
print(my_list)

#wine Example
#this line generates an array from a txt or in this case a csv file
wines = np.genfromtxt("datasets/winequality-red.csv", delimiters=";", skip_headers = 1)


#example for map() funciton

people = ['Dr. Christopher Brooks', 'Dr. Kevyn Collins-Thompson', 'DR. VG Vinod Vydiswaran', 'Dr. Daniel Romero']

def split_title_and_name(person):
	#split the string and then subset the portion of the string you want to retain
	title = person.split()[0]
	#split the string and then subset the portion of the string you want to retain
	#remember subset numbers can be negative to capture the right hand side of the split
	name = person.split()[-1]
	#A way to return more than 1 value when they are strings - good thing to keep in mind for when you are working with strings
	return '{} {}'.format(title,name)
#map is going to run the function for every iteration available
#people is a list, so it will run the function for every person in the list
print(list(map(split_title_and_name, people)))

#reworked into a lambda function with built in iteration
for person in people:
	print(lambda x: x.split()[0](person) + ' ' + x.split()[-1](person))

#reworked using map() 
print(list(map(lambda person: person.split()[0] + ' ' + person.split()[-1], people)))



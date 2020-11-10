#########################################################################
# Please note that this file is a playground and is not of importance
#########################################################################
print("Hello world")

# for x in range(1, 10, 3):
# 	print(x)


def votes(params):
	for vote in params:
	    print("Possible option:" + vote)

votes(['yes', 'no', 'maybe'])

# for x in range(10):
#     for y in range(x):
#         print(y)

number = 1
while number in range(1,8):
	print(number, end=" ")
	number += 1


def decade_counter():
	year = 100
	while year < 50:
		year += 10
	return year
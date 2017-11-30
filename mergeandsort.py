import numpy
import numpy.random as r


# grab the first indixesof each array and append the smaller one and remove it from that array

def merge_and_sort(first_array, second_array):
	third_array = []
	while len(first_array) != 0 and len(second_array) != 0:
		if first_array[0] < second_array[0]:
			third_array.append(first_array[0])
			first_array.remove(first_array[0])
		else:
			third_array.append(second_array[0])
			second_array.remove(second_array[0]);
	if len(first_array) != 0:
		third_array += first_array
	elif len(second_array) != 0:
		third_array += second_array
	return third_array




a = [1, 3, 5]
b = [2, 4, 6]

print merge_and_sort(a, b)

def merge_sort(a):
	if len(a) == 1:
		return a
	# split the array into two pieces
	
	mid = len(a)/2 
	first_half = merge_sort(a[:mid])
	second_half = merge_sort(a[mid:])
	return merge_and_sort(first_half, second_half)


	# perform our merge and sort method passing both arrays
	# return result

random_array = r.random_integers(0, 100, 10).tolist()
print random_array

sorted_array = merge_sort(random_array)
print sorted_array

# complexity O(n) because there is only one loop and becasue we are only moving/touching/looking at each number once


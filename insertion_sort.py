import picasso
import numpy.random as r

def linear_search(a, v):
	for i in range(len(a)):
		if v == a[i]:
			return i
    pass

def binary_search(a, v):
	start = 0
	end = len(a)-1



	while True:
		for i in range(len(a)):
			mid_index = (end+start)/2
			mid_value = a[mid_index]
			if v == mid_value:
				return mid_index
			elif v > mid_value:
				start = mid_index + 1
			elif v < mid_value:
				end = mid - 1





a = range(0, 10, 1)
print linear_search(a, 1)

p = picasso.Picasso('linear_search')
p.draw_best_fitting_line = True
for i in range(0, 15001, 1000):
    p.start(i)
    a = r.random_integers(0, i, i)
    linear_search(a, 1)
    p.end()
    p.export()


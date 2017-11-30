import picasso
import numpy.random as r

def linear_search(a, v):
	for i in range(len(a)):
		if v == a[i]:
			return i
    

def binary_search(a, v):
	start = 0
	end = len(a)-1
	


	while start < end:
		
		mid_index = (end+start)/2
		print start, end, mid_index
		mid_value = a[mid_index]
		if v == mid_value:
			return mid_index
		elif v > mid_value:
			start = mid_index + 1
		elif v < mid_value:
			end = mid_index - 1

		print start, end





a = range(0, 20, 1)
print "Index of target:" + str(binary_search(a, 17))

p = picasso.Picasso('linear_search')
p.draw_best_fitting_line = True
for i in range(0, 15001, 1000):
    p.start(i)
    a = r.random_integers(0, i, i)
    linear_search(a, -1)
    p.end()
    p.export()


p = picasso.Picasso('binary_search')
p.draw_best_fitting_line = True
for i in range(0, 15001, 1000):
    p.start(i)
    a = range(0, i)
    binary_search(a, -1)
    p.end()
    p.export()


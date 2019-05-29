#lst = [(60, 10), (20, 20), (100, 60)]

#f = lambda x: abs(x[1] - x[0])

#diff = [f(lst[0]), f(lst[1]), f(lst[2])]
#print(diff)


data = [(1, 2), (3, 4), (5, 6), (7, 0)]
f = lambda x: x[0]**2 + x[1]**2

data_1 = [f((1, 2)), f((3, 4)), f((5, 6)), f((7, 0))]

print (data_1)
f = key
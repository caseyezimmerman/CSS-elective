def merge_square_and_sort(a, b):
    c = []

    while len(a) != 0 and len(b) != 0:
        last_index = len(a) - 1
        if abs(a[last_index]) < abs(b[0]):
            value = a[last_index]
            a.remove(value)
            c.append(value * value)
        else:
            value = b[0]
            b.remove(value)
            c.append(value * value)

    if len(a) == 0:
        for i in b:
            c.append(i * i)
    else:
        for i in range(len(a) - 1, -1, -1):
            c.append(a[i] * a[i])

    return c



a = range(-15, 15, 2)
smallest_abs_index = 0

for i in range(len(a)):
    if abs(a[i]) < abs(a[smallest_abs_index]):
        smallest_abs_index = i

    if a[i] > 0:
        break

a1 = a[:smallest_abs_index]
a2 = a[smallest_abs_index:]

print merge_square_and_sort(a1, a2)
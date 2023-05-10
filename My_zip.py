def my_zip(*args):
    min_len = min(len(seq) for seq in args)
    for i in range(min_len):
        yield tuple(seq[i] for seq in args)


a = [1, 2, 3]
b = [4, 5, 6]
c = ['Abby', 'Banny', 'Canny']
for x, y, z in my_zip(a, b, c):
     print (x, y, z)
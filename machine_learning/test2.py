a = [[1,2], [1,3], [2, 3], [2, 1], [5, 6], [6, 5], [1, 2], [7, 8], [11, 12], [5, 7],[11,3],
         [8, 3]]
b = [[2,1], [1,2 ], [100,11]]
a = [v for v in a if v not in b]
print a
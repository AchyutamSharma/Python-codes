mtx = [[1,2,3,4],
       [5,6,7,8],
       [9,10,11,12],
      ]

transposed = []
for i in range(4):
    transposed.append([row[i] for row in mtx])
transposed    
# output:- [[1, 5, 9], [2, 6, 10], [3, 7, 11], [4, 8, 12]]

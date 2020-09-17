matrix_a=[[3,6],[4,5]]
matrix_b=[[5,8],[6,7]]
result=[[sum(row) for row in zip(*t)] for t in zip(matrix_a,matrix_b)]
print (result)

for t in zip(matrix_a,matrix_b):
    print(t)

print( i for i in zip(matrix_a,matrix_b))
#3,6 5,8
#4,5 6,7 이 각각 함께 표시해서 언패킹 후에 zip하고 sum으로 더하면 값 도출.
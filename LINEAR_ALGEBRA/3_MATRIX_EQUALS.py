#동치 행렬이란 A B행렬이 있으면 A=B를 나타내는 동치조건이다.

matrix_a = [[1,1],[1,1]]
matrix_b = [[1,1],[1,1]]

print(all([row[0]==value for t in zip(matrix_a,matrix_b) for row in zip(*t) for value in row]))
#all함수는 똑같으면 트루 반환

matrix_b=[[5,8],[6,7]]

print(all([all([row[0] == value for value in row])for t in zip(matrix_a,matrix_b)for row in zip(*t)]))

print([[row[0]==value for value in row]for t in zip(matrix_a,matrix_b) for row in zip(*t)])

#시험
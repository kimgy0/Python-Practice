u=[2,2]
v=[2,3]
z=[3,5]

row_vectors=[[2,2],[2,3],[3,5]]

def vector_addition(*args):
    return [sum(t) for t in zip(*args)]

print(vector_addition(u,z,v))

print(vector_addition(*row_vectors))
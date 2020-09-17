#함수를 호출하며 사용했을 때는 10초 정도 걸렸음.

def sclar_vector_product(scalar, vector):
    result=[]
    for value in vector:
        result.append(scalar*value)
    return result

iteration_max=10000

vector = list(range(iteration_max))
scalar=2

for _ in range(iteration_max): #아무것도 안가져오고 그냥 돌리기만 할 때는 _만 쓴다.
    print(sclar_vector_product(scalar,vector))
    #*교수님 4_PERFORMANCE_LIST_COMPREHENSION, 2 같은 경우에는 예제 코드를 클론 코딩하면 루프가 함수를 실행하는 것 뿐 아니라 표현까지해서 PRINT함수에 묶으면 이런식으로 돌아갈 수 밖에 없을 것 같습니다.
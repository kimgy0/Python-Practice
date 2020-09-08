#for문으로 구구단 출력하기
for i in range(2,10):
    for j in range(1,10):
        print(i*j,end=" ")
        #print(f'{i*j:3}',end="")
    print('')
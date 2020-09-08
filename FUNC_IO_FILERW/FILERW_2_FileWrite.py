#새파일에 쓰기모드로 열어 출력값 적기
f=open("newFile.txt",'w')
for i in range(1,11):
    data=f'{i}번째 줄 입니다.\n'
    f.write(data)
f.close()
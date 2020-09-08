#기존의 새로쓰기방식 말고 이어서 새로운 내용 추가하기
f=open("newFile.txt",'a')
for i in range(11,20):
    data="%d번째 줄입니다.\n"%i
    f.write(data)
f.close()
f=open("newFile.txt",'r')
print(f.read())
f.close()
#read함수는 전체 파일을 통째로 다 저장한다.

f=open("newFile.txt",'r')
data=f.read()
print(data)
f.close()
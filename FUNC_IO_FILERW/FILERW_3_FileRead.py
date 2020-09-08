#readline 함수는 첫째줄만 읽어낸다.
f=open("newFile.txt",'r')
line=f.readline()
print(line)
f.close()
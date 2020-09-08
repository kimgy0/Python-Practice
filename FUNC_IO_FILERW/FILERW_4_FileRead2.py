#readline으로 여러줄 읽어오기
f=open("newFile.txt",'r')
while True:
    line=f.readline()
    if not line:
        break
    print(line)
f.close()
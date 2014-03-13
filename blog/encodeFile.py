#coding:utf-8

import chardet

def convertEncoding(from_encode,to_encode,old_filepath,target_file):
    f1=file(old_filepath)
    content2=[]
    while True:
        line=f1.readline()
        content2.append(line.decode(from_encode).encode(to_encode))
        if len(line) ==0:
            break

    f1.close()
    f2=file(target_file,'w')
    f2.writelines(content2)
    f2.close()

convertFile = open('1234.csv','r')
data = convertFile.read()
convertFile.close()

convertEncoding(chardet.detect(data)['encoding'], "utf-8", "1234.csv", "1234_bak.csv")
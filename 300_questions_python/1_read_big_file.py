#read a big file and avoid the memory error
import time
from mmap import mmap

def creatfilesize(n):
    local_time = time.strftime("%Y%m%d%H%M%S",time.localtime())
    #file_name = "C:\测试大量文件与大文件\大文件\\"+str(local_time)+".txt"
    file_name = "C:\\" + str(local_time) + ".txt"
    bigFile= open(file_name, 'w',encoding='utf-8')
    bigFile.seek(1024*1024*1024*n)
    bigFile.write('test')
    bigFile.write("test")
    bigFile.close()
    return file_name

#use mmap
def get_lines(fp):
    with open(fp,"r+") as f:
        m = mmap(f.fileno(), 0)
        tmp = 0
        for i, char in enumerate(m):
            if char==b"\n":
                yield m[tmp:i+1].decode()
                tmp = i+1

#use yield to avoid the memory question
def read_file(fpath):
   BLOCK_SIZE = 65536
   with open(fpath, 'rb') as f:
       while True:
           block = f.read(BLOCK_SIZE)
           if block:
               yield block
           else:
               return

if __name__ == '__main__':
    n = int(input("输入你要生成的文件大小（单位为GB）:"))
    filename = creatfilesize(n)
    start_time = time.time()
    for i in read_file(filename):
        print(i)

    print('cost time:' ,time.time() - start_time)
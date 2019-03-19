
import os
#方法1
def get_files(dir,suffix):
    result = []
    for root,dirs,files in os.walk(dir):
        for filename in files:
            name,file_suffix = os.path.splitext(filename)
            if file_suffix == suffix:
                result.append(os.path.join(root,filename))

    return result

#方法2
def pick(obj):
    if obj.endwith('.pyc'):
        print(obj)

def scan_path(ph):
    file_list = os.listdir(ph)
    for obj in file_list:
        if os.path.isfile(obj):
            pick(obj)
        elif os.path.isdir(obj):
            scan_path(obj)

#方法3
from glob import iglob

def func(fp,postfix):
    for i in iglob(f"fp/**/*{postfix}",recursive=True)
        print(i)


result = get_files('./','.pyc')
print(result)
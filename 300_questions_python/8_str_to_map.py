#将字符串 "k:1 |k1:2|k2:3|k3:4"，处理成字典 {k:1,k1:2,...}
if __name__ == '__main__':
    str1 = "k:1|k1:2|k2:3|k3:4"
    compiled_map = {}
    for item in str1.split('|'):
        k,v = item.split(':')
        compiled_map[k] = v

    print(compiled_map)
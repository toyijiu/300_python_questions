list = [1,2,3,4,5]
print(list[10:])
#这里不会产生IndexError错误，比如list[10]这种尝试获取index为10的成员会导致IndexError错误，但是尝试获取切片时index溢出了仅仅返回一个空列表
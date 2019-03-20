a = [1,2,3,4,5,6,7,8]
print(id(a))
print(id(a[:]))


for i in a[:]:
    if i > 5:
        pass
    else:
        a.remove(i)
        print(a)

print(id(a))

#考虑到删除时数组的动态变化，可以从后往前删除
for i in range(len(a)-1,-1,-1):
    if a[i] > 5:
        pass
    else:
        a.remove(a[i])
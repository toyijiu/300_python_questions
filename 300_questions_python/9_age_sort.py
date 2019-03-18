#请按alist中元素的age由大到小排序
alist = [{'name':'a','age':20},{'name':'b','age':30},{'name':'c','age':25}]
alist = sorted(alist,key=lambda x:x['age'],reverse=True)
print(alist)
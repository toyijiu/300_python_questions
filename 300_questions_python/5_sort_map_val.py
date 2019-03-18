if __name__ =="__main__":
    test_map = {'a':1,'b':-2,'c':9,'d':7}
    print(sorted(test_map.items(),key=lambda x:x[1]))

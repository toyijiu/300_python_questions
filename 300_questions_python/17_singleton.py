#用装饰器
def singleton(cls):
    instances = {}
    def wrapper(*args,**kwargs):
        if cls not in instances:
            instances[cls] = cls(*args,**kwargs)
        return instances[cls]
    return wrapper

@singleton
class Foo(object):
    pass

foo1 = Foo()
foo2 = Foo()
print(foo1 == foo2)

#重写基类new
class Singleton(object):
    def __new__(cls,*args,**kwargs):
        #判断cls中是否有_instance属性，有就说明之前已经创建过该对象了
        if not hasattr(cls,'_instance'):
            cls._instance = super(Singleton,cls).__new__(cls,*args,**kwargs)

        return cls._instance
class Foo2(Singleton):
    pass
foo3 = Foo2()
foo4 = Foo2()
print(foo3 == foo4)

#元类，元类是创建类对象的类，类对象创建实例对象时会调用call方法，这里重写call.type是python的元类
class Singleton2(type):
    def __call__(cls, *args, **kwargs):
        if not hasattr(cls,'_instance'):
            cls._instance = super(Singleton2,cls).__call__(*args,**kwargs)

        return cls._instance

class Foo3(object):
    __metaclass__ = Singleton2

foo5 = Foo3()
foo6 = Foo3()
print(foo5 == foo6)
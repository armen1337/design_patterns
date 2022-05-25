#  ------------------- First realization -------------------
class SingletonMeta(type):
    """
    With this approach, the constructor will be called only once,
    but if we uncomment the rows 15-16, we can make the constructor to be called every time.
    Therefore, this approach is more agile
    """
    _instances = {}

    def __call__(cls, *args, **kwargs):
        instance = super().__call__(*args, **kwargs)

        if cls not in cls._instances:
            cls._instances[cls] = instance
        # else:
        #     cls._instances[cls].__init__(*args, **kwargs)

        return cls._instances[cls]


class Singleton(metaclass=SingletonMeta):
    def __init__(self, y):
        self.y = y

    def set_x(self, x):
        self.x = x


s1 = Singleton(1)
s1.set_x(5)
s2 = Singleton(2)
print("First realization")
print("s2.x -", s2.x)
print("s2.y -", s2.y, "so constructor is called once")
print("id(s1) == id(s2):", id(s1) == id(s2))


# ------------------- Second realization -------------------
class Singleton:
    """ With this approach, constructor will be called as many times as we call it """
    def __new__(cls, *args, **kwargs):
        instance = super().__new__(cls)
        if not hasattr(cls, '_instance'):
            cls._instance = instance
        return cls._instance

    def __init__(self, y):
        self.y = y


s1 = Singleton(1)
s2 = Singleton(2)
print("\nSecond realization")
print("id(s1) == id(s2):", id(s1) == id(s2))
print("s2.y -", s2.y, "so constructor is called again")

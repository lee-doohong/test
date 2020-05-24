# class simple:
#     count = 0 
#     def __init__(self):
#         simple.count += 1

#     @staticmethod #sm함수를 staticmethod에 전달하고 이것을 다시 sm에 전달한다
#     def get_count(): #애초에 스태틱 함수로 만들것이여서 받는 인자가 없다. 
#         return simple.count

# def main():
#     print(simple.get_count())
#     s = simple()
#     print(simple.get_count())

# main()

# class simple : 
#     num = 5
#     @staticmethod
#     def sm(i):
#         print('st~ 5 + {0} = {1}'.format(i, simple.num + i))
#     @classmethod
#     def cm(cls, i):
#         print('cl~ 5 + {0} = {1}'.format(i, simple.num + i))


# def main():
#     simple.sm(3)
#     simple.cm(3)
#     s = simple()
#     s.sm(4)
#     s.cm(4)

# main()

# class simple : 
#     count = 0
#     def __init__(self):
#         simple.count += 1
#     @classmethod
#     def get_count(cls):
#         return cls.count #cls에 전달되는 것은 simple 클래스 / cls.count == simple.count 

# def main():
#     print(simple.get_count())
#     s = simple()
#     print(simple.get_count())

# main()

# class natural:
#     def __init__(self, n):
#         self.n = n
#     def getn(self):
#         return self.n
#     @classmethod
#     def add(cls, n1, n2):
#         return cls(n1.getn() + n2.getn())

# def main():
#     n1 = natural(1)
#     n2 = natural(2)
#     n3 = natural.add(n1, n2) #natural(3)
#     print("{0} + {1} = {2}".format(n1.getn(), n2.getn(), n3.getn()))

# main()


# class cal: 
#     def deco(func):
#         def dc(self):
#             print("최첨단 계산기")
#             return func(self)
#         return dc

#     def __init__(self, a, b):
#         self.a = a 
#         self.b = b

#     @deco
#     def add(self):
#         return self.a + self.b

#     @deco
#     def sub(self):
#         return self.a - self.b

    
# s1 = cal(5,2)
# print(s1.add())

class date:
    def __init__(self, y, m, d):
        self.y = y
        self.m = m
        self.d = d 
    def show(self):
        print('{0}, {1}, {2}'.format(self.y, self.m, self.d))

    @classmethod
    def next_day(cls, today):
        return cls(today.y, today.m, today.d +1)

class kdate(date):
    def show(self):
        print('kor : {0}, {1}, {2}'.format(self.y, self.m, self.d))

class jdate(date):
    def show(self):
        print('jpn : {0}, {1}, {2}'.format(self.y, self.m, self.d))

def main():
    kd1 = kdate(2025, 4, 12)
    kd1.show()
    kd2 = kdate.next_day(kd1)
    kd2.show()

    jd1 = jdate(2025, 4, 12)
    jd1.show()
    jd2 = jdate.next_day(kd1)
    jd2.show()        

main()
# class Simple:
#     def __init__(self):
#         self.i = 0 # 변수 초기화, 이 순간에 변수 i 가 만들어짐
#     def seti(self, i): # seti 메소드 정의 / seti메소드를 호출하면 그 안에서 self.i=i 묹장이 실핸되면서 객체 내에 변수 i가 만들어 진다.
#         self.i = i
#     def geti(self): #geti 메소드 정의
#         return self.i 

# s1 = Simple()
# s1.seti(25)
# s1.geti()
# print(s1.geti())


class SoSimple:
    def geti(self):
        return self.i

ss = SoSimple()
ss.i = 27
ss.geti()
print(ss.geti())
ss.hello = lambda : print('hi')
ss.hello()

del ss.i
del ss.hello

ss.geti()
ss.hello()
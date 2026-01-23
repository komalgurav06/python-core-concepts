
X = 99
# def func2(y):
#     z = X + y
#     return z

# result = func2(1)
# print(result)

# def func3():
#     global X
#     X = 10

# func3()
# print(X)    


def f1():
    x = 88
    def f2():
        print(x)
    return f2
result = f1()    
result()


def chaicoder(num):
    def actual(x):
        return x ** num
    return actual

f = chaicoder(2)
g = chaicoder(3)

print(f(3))
print(g(3))
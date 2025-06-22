def foo(*args):
    return list(args)

def foo2(**kwargs):
    return kwargs

def foo3(*args):
    result = []
    salida = [result.extend(a) for a in args]
    return result

def foo4(*args):
    return [item for sublist in args for item in sublist]

def foo5(*args):
    for sublist in args:
        if len(sublist) == 0:
            return False
    return True


print(foo(1, "a", 5, "c"))
print(foo2(a = 1, c = 5, d = 109))

print(foo3([1, 2], [3, 5, 7, 8], [1]))

print(foo4([1, 2], [3, 5, 7, 8], [1]))

print(foo5([1, 2], [3, 5, 7, 8], []))

def foo6():
    return "Hello"
    def foo2():
        return foo6
    
print(foo6())
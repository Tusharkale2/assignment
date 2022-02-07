def mod_div(fun):
    def inner(a,b):
        if a < b:
            a,b=b,a
        return fun(a,b)
    return inner
@mod_div
def div(a,b):
    return a//b

a,b=(int(i) for i in input().split())
print(div(a,b))

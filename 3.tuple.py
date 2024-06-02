# ex=("one",1,None)
# print(ex)
# count index len
# print(ex.count("one"))
# print(ex[1:3])
# for i in ex:
#     print(i)

tup=("one","two",[1,2,3,4,5])
print(tup[2])
print(tup[2].pop())
tup[2].append("hi hello")
print(tup)

def fun(n,m):
    add=n+m
    gun=n*m
    return add,gun #return asa tuple
print(fun(4,5))
jog,gun=fun(4,5)
print(jog)
print(gun)
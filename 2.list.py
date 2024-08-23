  # #list e data change kore jebabe dic e data add kore seibabe

li=["hasib", 1,2,3.4,True ,None ]
print(li)
print(li[1])
print(li[1:3])
# li[1]= "one"
# print(li )
# li[1:]="one"
# print(li)

# ####### addd items: "append, insert, extend"
# fruits=["graps","mango",]
# fruits.append("apple") #add item in last
# print(fruits)

# fruits.insert(0,"jam") #add item by position
# # print(fruits)

# fruits2=["orrange","lemon"]
# # newfruits=fruits2+fruits
# # print(newfruits)
# fruits.extend(fruits2)
# print(fruits)
# print(fruits2)
# fruits.append(fruits2) #list inside list
# print(fruits)

# #  ##     delete items:" pop, remove, del "
# fruits=["graps","mango","apple"]
# fruits.pop() #by default last item delete korbe
# print(fruits)
# fruits.pop(1) # dewa item delete korbe
# print(fruits)
# del fruits[1]
# print(fruits)
# fruits.remove("apple")
# print(fruits)
# #
# print(fruits.count("apple"))
# fruits.sort()
# print(fruits)
# num=[3,4,5,2,1]
# # num.sort()
# print(num)
# print(sorted(num))
# print(num)
# # num.clear()
# # print(num)
# num2=num.copy()
# print(num2)
#
# info=input("enter ur name and age:").split() #space separated
# print(info) #['hasib', '34']
# info=input("enter ur name and age:").split(",")  #comma separated
# print(info) #['hasib', '34']
# name,age=input("enter ur name and age:").split(",")  #comma separated
# print(name)
# print(age)

# info=["hasib","34"]
# print(",".join(info)) #list to str
# fruits=["graps","mango","apple"]
# for i in fruits:
#     print(i)
# i=0
# while i<len(fruits):
#     print(fruits[i])
#     i+=1

# mat=[[1,2,3],[4,5,6],[7,8,9]]
# for i in mat:   # list inside list
#     for j in i:
#         print(j)
# print(mat[0])
# print(mat[1][0])  #print 4

# num=list(range(1,11))
# print(num)
# num=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10,1,2,3,1]
# print(num.index(2))
# print(num.index(2,num.index(2)+1))




# num=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10,]

# def neglist(li):
#     neg=[]
#     for i in li:
#         neg.append(-i)
#     return neg
# call=neglist(num)
# print(call)
#
# def numsq(li):
#     sq=[]
#     for i in li:
#         sq.append(i**2)
#     return sq
# print(numsq(num))

# def rev(li):
#      li.reverse()
#      return li
# print(rev(num))
# def rev(li):
#      return li[::-1]
# print(rev(num))

# def rev(li):
#     r=[]
#     for i in range(0,len(li)):
#         p=li.pop()
#         r.append(p)
#     return r
#
# print(rev(num))


# word=["abc","cde"]
# def revword(li):
#     l=[]
#     for i in li:
#         l.append(i[::-1])
#     return l
# print(revword(word))

# def fun(l):
#     odd=[]
#     even=[]
#     for i in l:
#         if i%2==0:
#             even.append(i)
#         else:
#             odd.append(i)
#     return [odd,even]
# li=list(range(1,11))
# print(fun(li))

# def com(l1,l2):
#     common=[]
#     for i in l1:
#         if i in l2:
#             common.append(i)
#     return common
#
# li1=list(range(1,6))
# li2=list(range(1,9))
# call=com(li1,li2)
# print(call)

# li=list(range(1,9))
# print(max(li))
# print(min(li))
# def diff(li):
#     return max(li)-min(li)
# print(diff(li))

# def f(li):
#     h=0
#     for i in li:
#         if type(i) == list:
#             h+=1
#     return h
# li=[1,2,[],3,[]]
# print(type(li))
# print(f(li))

# name=[1,2,3,4,51]
# for i in range(0,len(name)):
#     p=name.pop()
#     print(p)

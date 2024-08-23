#####        funtions

def sum(a,b):
    return a+b
i=int(input("enter"))
j=int(input("enter:"))
print(sum(i,j))


#####            return vs print
# def sum(a,b):
#     print(a+b)
#
# sum(5,6)

#               practise.....

# def nam(name):
#     return name[::-1]
# print(nam('Hasib'))

# def odd_even(num):
#     if num%2==0:
#         print("even")
#     print("odd")
# odd_even(6)

# def is_even(num):
#     if num%2==0:
#         print(True)
#     else:
#         print(False)
# is_even(5)

# def is_even(num):
#     if num%2==0:
#         return True
#     else:
#         return False
#
# print(is_even(5))

# def even(num):
#     return num%2 == 0
# print(even(6))

# def song():
#     print("hi hasib ")
# song()

#               **************

# def bigger(a,b):
#     if a>b:
#         print(f"{a} is bigger")
#     print(f"{b} is bigger")
#
# a=int(input("enter 2 num:"))
# h=int(input("enter2nd:"))
# bigger(a,h)

#                     ***  UNCOMMENT GREEN  *****
'''
def bigger(a,b):
    if a>b:
        return a
    return b
'''

# a=int(input("enter 2 num:"))
# h=int(input("enter2nd:"))
# big=bigger(a,h)
# print(f"{big} is bigger")

#                   fun inside fun

# def bigest(a,b,v):
#     x=bigger(a,b)
#     if x>v:
#         return x
#
#     else:
#         return v
#
# gr=bigest(1,2,3)
# print(f"{gr} is biggest")

# def bigest(a,b,v):
#     if bigger(a,b)>v:
#         return bigger()
#     return v
#
# gr=bigest(1,2,3)
# print(f"{gr} is biggest")

# def bigest(a,b,v):
#     x=bigger(a,b)
#     y=bigger(x,v)
#     return y
#
# gr=bigest(1,2,3)
# print(f"{gr} is biggest")

# def bigest(a,b,v):
#     x=bigger(a,b)
#
#     return bigger(x,v)
#
# gr=bigest(1,2,3)
# print(f"{gr} is biggest")

# def bigest(a,b,v):
#     return bigger(bigger(a,b) , v)
#
# gr=bigest(1,2,3)
# print(f"{gr} is biggest")


# def ultanam(nam):
#     if nam==nam[::-1]:
#         print(True)
#     else:
#         print(False)
#
# ultanam("hasan")
# ultanam("madam")

#                   default parametr

# def userinfo(name1,name2,age):
#     print(f"your 1st name is {name1}")
#     print(f"your 2nd name is {name2}")
#     print(f"your age is {age}")

# userinfo("hasib","hasan",45)
# userinfo("hasib","hasan")

# def userinfo(name1,name2,age=34):
#     print(f"your 1st name is {name1}")
#     print(f"your 2nd name is {name2}")
#     print(f"your age is {age}")

# userinfo("hasib","hasan")

# def userinfo(name1,name2,age=None):
#     print(f"your 1st name is {name1}")
#     print(f"your 2nd name is {name2}")
#     print(f"your age is {age}")
    
# userinfo("hasib","hasan")

# def userinfo(name1,name2="unknown",age=None): #last e NONE dilei age UNKNOWN kaj korbe
#     print(f"your 1st name is {name1}")
#     print(f"your 2nd name is {name2}")
#     print(f"your age is {age}")
    
# userinfo("hasib")


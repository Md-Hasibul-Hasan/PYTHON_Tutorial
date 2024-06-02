#list e data change kore jebabe dic e data add kore seibabe
# user={"name": "hasib",
#     "age": 43
#     }
# print(user)
# user2 =dict(name="hasib",
#           age = 43,
#           )
# print(user2)

# access data :
# print(user["name"]) # list er motoi tobe potion er jaigai "keY" likte hoi
# print(user["age"])
# print(user.get("name"))
# print(user.get("age"))
# print(user.get("sata"))
# print(user.get("sata","not found"))

# userinfo={
#     "name": "hasib",
#     "age": 43,
#     "movie": ["jani na",1,3],
#     "song" : ["ki jani ",4,5],
#     }
# print(userinfo)
# print(userinfo["song"])

# users={
#    " userinfo1" :{
#     "name": "hasib",
#     "age": 43,
#     "movie": ["jani na",1,3],
#     "song" : ["ki jani ",4,5],
#     },
#     " userinfo2": {
#         "name": "hasan",
#         "age": 46,
#         "movie": ["jani ", 1, 3],
#         "song": ["ki ", 4, 5],
#     }
# }
# print(users)
# print(users[" userinfo1"])

# add data in dc: list a data jebabe poriborton kora hoi dic a data seibabe add kora hou
# userinfo={  }
# userinfo["name"]="hasib"
# userinfo["age"]= 32
# userinfo["movie"]=["jani na",1,3]
# userinfo["song"]=["li la",5,6]
# print(userinfo)
#
# if "name" in userinfo.keys():
#     print("yes")
# else:
#     print("no")
# if 32 in userinfo.values():
#     print("yes")
# else:
#     print("no")
# for i in userinfo.keys():
#     print(i)
# for i in userinfo.values():
#     print(i)
# for i,j in userinfo.items():
#     print(f"keY is {i} and value is {j}")
# for i in userinfo.items(): # tuple unpacking
#     print(i)

# userinfo={
#     "name": "hasib",
#     "age": 43,
#     "movie": ["jani na",1,3],
#     }
# #add data
# userinfo["song"]= ["ki jani ",4,5]
# print(userinfo)
# #pop method
# poped_item=userinfo.pop("song") # list o pop() khali rakle laster da pop oito kintu dic o pop("kisu") den lago
# print(userinfo)
# print(poped_item)
# #popitem method
# pop=userinfo.popitem()# mon moto ekta pop koira dibo
# print(userinfo)
# print(pop)
# #update method
# moreinfo={
#     "name": "------",
#     "bari":"gafargaon",
#     "basa":"mymensingh"
# }
# userinfo.update(moreinfo)
# print(userinfo)
#fromkeys
# d=dict.fromkeys(["name","age"],"unknown")#list er maddome
# print(d)
# d2=dict.fromkeys(("name","age"),"unknown")#touple er maddome
# print(d2)
# d3=dict.fromkeys(("name"),"unknown")
# print(d3)
# d4=dict.fromkeys(range(1,11),"")
# print(d4)

#clear copy ager motoi

#cube finder

# def cubefinder(num):
#     d = {}
#     for i in range(1,num+1):
#         d[i]=i**3
#     print(d)
# cubefinder(3)

#word count
# def count(string):
#     d={}
#     if " " in string:
#         newstring=string.replace(" ","")
#     for i in newstring:
#         d[i]=newstring.count(i)
#     print(d)
# count("hasib hasan")
#
user={}
name=input("enter name:")
age=int(input("enter age:"))
song=input("enter song sepated by comma:").split(" ")
user["name"]=name
user["age"]=age
user["song"]=song
# print(user)
for i,j in user.items():
    print(f"{i}:{j}")

########            set
# s={1,2,3,4,5,"hasib"}
# print(s)
# s.add(6)
# print(s)
# s.remove(6)
# print(s)
# s.discard(9)
# print(s)

# li=[1,2,3,4,5,1,2,3,4,5]
# #remove duplicate
# s2=list(set(li))
# print(s2)
# s4={2,3,4}
# union=s | s4
# print(union)
# intersec=s & s4
# print(intersec)

 #    read method

# f=open("myfile.txt","r")
# print(f.read())
# f.close()



#    tell,seek.......

# f=open("myfile.txt","r")
# print(f"cursor position:{f.tell()}")
# print(f.read())
# print(f"cursor position:{f.tell()}")
# f.seek(0)
# print(f"cursor position:{f.tell()}")
# f.close()


#    readline,readlines.......

# f=open("myfile.txt","r")
# print(f.readline())
# print(f.readline(),end='')
# print(f.readline())
# f.close()


#    with open close korar dorkar nai

# with open("myfile.txt","r") as f:
#     data=f.read()
#     print(data)




#   write method 

# with open("myfile2.txt",'w') as f:
#     f.write("hello hasib shut up")


#     append method

# with open("myfile2.txt","a") as f:
#     f.write("\nsorry ami ")


#    read and write

# with open("myfile.txt","r") as rf:
#     with open("myfile2.txt","w") as wf:
#         wf.write(rf.read())



# exercise 1
'''
hasib,12
asif,13
output:
hasib er age 12
asif er age 13
'''

with open("myfile.txt","r") as rf:
    with open("myfile2.txt","w") as wf:
        for line in rf.readlines():
            name,age=line.split(",")
            wf.write(f"{name} er age {age}")


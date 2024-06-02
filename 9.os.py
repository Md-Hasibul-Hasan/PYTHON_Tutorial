import os

# os.getcwd()  get current working directory

# print(os.getcwd())


# create folder os.mkdir()

# if os.path.exists("movies"):
#     print("already exists")
# else:
#     os.mkdir("movies")




# create folder in another directory

# if os.path.exists(r"C:\Users\offic\OneDrive\Pictures\pics"):
#     print("already exists")
# else:
#    os.mkdir(r"C:\Users\offic\OneDrive\Pictures\pics")


# create foler in folder os.makedirs()
# os.makedirs("folder1/folder2")



#create file

# with open("aaa.txt","a") as f:
#     f.write("")



# os.listdir() 

# print(os.listdir())
# print(os.listdir(r"C:\Users\offic\OneDrive\Pictures"))



# complete walk of any directory

# t=os.walk(r"E:\JTT")
# for path_name,folder_name,file_name in t:
#     print(f"path name {path_name}")
#     print(f"folder name {folder_name}")
#     print(f"file name {file_name}")



import shutil

# delete folder  --> ("path")
# shutil.rmtree("movies") 

# copy files and folder   --> (r"path", r"path")
# shutil.copy("aaa.txt",r"D:\A_User\Music\aa.txt")
# shutil.copytree("folder1",r"D:\A_User\Music\folder1")


# move files and folders  --> (r"path", r"path")
# shutil.move("aaa.txt",r"D:\A_User\Music\aa.txt")
# shutil.move("folder1",r"D:\A_User\Music\folder1")



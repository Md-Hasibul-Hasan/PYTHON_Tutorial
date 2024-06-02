# while True:
#     try:
#         age=int(input("Enter Age:"))
          #break # ----> else na dile ekhane break dite hobe  

#     except:
#         print("something wrong TRY AGAIN")

#     else:  #-----> Try thik moto colle else colbe          
#         if age>18:
#             print("You Can")
#         else:
#             print("You Cant")

#         break  # loop theke ber hobe 
#     finally:
#         print("Finally always run ebon else er age print hoi")


# practise

def divide():
       
    while True:
        a=input("enter first number:")
        b=input("enter second number:")
        try:
            a=int(a)
            b=int(b)
            print(a/b)
            break
        except:
            print("error Try again")
divide()



        

    
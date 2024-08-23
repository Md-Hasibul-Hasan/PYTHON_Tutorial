
class person:
    def __init__(self,one,two):
        # print("hi")
        self.name=one
        self.age=two

p1=person("hasib",24)
p2=person("asif",32)
    
print(p1.name)
print(p2.name)
print(p1.age)
print(p2.age)




# class person:
#     def __init__(self,nam,pesa):
#         self.name= nam
#         self.occ= pesa
#     def info(self):
#         print(f"{self.name} is a {self.occ}")

# a=person("hasib","eng")
# a.info()

# b=person("asif","doc")
# b.info()


# practise 1

# class Laptop:
#     def __init__(self, brand, name, price) -> None:
#         self.brand=brand
#         self.name=name
#         self.price=price
#         self.brand_name=brand+" "+name
#     def info(self):
#         print(f"Brand= {self.brand} Name= {self.name} price={ self.price}")

# l1=Laptop("Walton", "BX3", 5000)
# l2=Laptop("Hp", "BX4", 7000)
# l1.info()
# print(l1.brand_name)

# l2.info()
# print(l2.brand_name)




# practise 1 modify

# class Laptop:
#     def __init__(self, brand, model_name, price) -> None:
#         self.brand = brand
#         self.name = model_name
#         self.price = price
#         self.laptop_name = brand + ' ' + model_name
#     def discount(self,value):
#         dis = self.price - self.price*(value/100)
#         print(f"your discount price is {dis}")
#     def info(self):
#         print(f"Brand={self.brand} Name={self.name} Price={self.price}")
    
# l1 = Laptop("hp", "bx1", 50000)
# l2 = Laptop("walton", "bx2", 60000)

# l1.info()
# l1.discount(10)




# more modify 

# class Laptop:
#     def __init__(self, brand, name, price) -> None:
#         self.brand=brand
#         self.name=name
#         self.price=price
#         self.brand_name=brand+" "+name
#     def discount(self):
#             discount_offer=int(input("enter discount:"))/100
#             print(f"discount_price={ self.price-self.price*discount_offer}")

#     def info(self):
#         print(f"Brand= {self.brand} Name= {self.name},price={ self.price}")
#         self.discount()

        
# l1=Laptop("Walton", "BX3", 5000)
# l2=Laptop("Hp", "BX4", 7000)
# l1.info()
# l2.info()


        

# practise 2

# class Circle:
#     def __init__(self, radius, pi) -> None:
#         self.radius = radius
#         self.pi = pi
#     def area(self):
#         return self.pi*self.radius*self.radius
#     def cir(self):
#         return self.radius*self.pi*2

# c1=Circle(2,3.14)
# c2=Circle(5,3.14)

# print(c1.area())
# print(c1.cir())



# modify practice 2

# class circle:
#     pi=3
#     def __init__(self,radius):
#         self.radius=radius
#     def area(self):
#         #######
#         a=circle.pi*self.radius**2
#         ######
#         print(a)

# c1=circle(3)
# c1.area()



# class Person:
#     count = 0
#     def __init__(self):
#         Person.count+=1

# p1=Person()
# p2=Person()
# p3=Person()
# print(Person.count)


# class person:
#     name="unknown"
#     pesa="unknown"
#     def info(self):
#         print(f"{self.name} is a {self.pesa}")

# a=person()
# print(a.name)
# a.name="hasib"
# a.pesa="eng"
# a.info()
    
# b=person()
# b.name="asif"
# b.info()





# class person:
#     def __init__(self): 
#         print("i am a person")

# a=person()
# b=person()










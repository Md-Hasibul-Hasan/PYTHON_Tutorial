
questions={

        "1.Sum of 1 plus 1?" : [1,2,3,4,2],
        "2.what is ur name?"  : ["Hasib","Asif","roudro","nabil",1],
        "3.what is ur frn name?" : ["Hasib","Asif","roudro","nabil",2],
        "4.Sum of 1 pllus 1?" : [1,2,3,4,3],
        "5.what is ur naame?"  : ["Hasib","Asif","roudro","nabil",2],
        "6.what is ur frrn name?" : ["Hasib","Asif","roudro","nabil",1],
        "7.Sum of 1 plussss 1?" : [1,2,3,4,2],
        "8.what is ur nameee?"  : ["Hasib","Asif","roudro","nabil",4],
        "9.what is ur frnnn name?" : ["Hasib","Asif","roudro","nabil",4],
        "10.Sum of 1 pluss 1?" : [1,2,3,4,4],


}
    
correct=0
skip=0
wrong=0
correctAns={}
wrongAns={}
skipAns={}

# for i in range(0,len(questions)):
for j,k in questions.items():
    print(f"\n{j}")
    print(f"a.{k[0]}           b.{k[1]}")
    print(f"c.{k[2]}           d.{k[3]}")


    reply=input("enter answer:")
    if reply=="a" or reply=="1":
        reply=1
    elif reply=="b" or reply=="2":
        reply=2
    elif reply=="c" or reply=="3":
        reply=3
    elif reply=="d" or reply=="4":
        reply=4
    elif  reply=="":
        reply=""


    if reply==k[4]:
        correct+=1
        correctAns[j]=k[4]
    elif reply=="":
        skip+=1
        skipAns[j]=k[4]
    else:
        wrong+=1
        wrongAns[j]=k[4]

        

marks=correct-wrong*.25
print(f"\nMarks={marks} Correct={correct} Wrong={wrong} skip={skip}")
print("\ncorrected ans are:")
for i,j in correctAns.items():
    print(f"{i} : {j}")
print("\nwrong ans are:")
for i,j in wrongAns.items():
    print(f"{i} : {j}")
print("\nskipped ans are:")
for i,j in skipAns.items():
    print(f"{i} : {j}")

        
        
        
        
    

    

    


    

        

    


            
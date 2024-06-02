question=[["whats ur name? ","hasib ","dfdfb","cdfdf","ddfdf",3],["whats ur name? ","aafda","dfdfb","cdfdf","ddfdf",3],["whats ur name? ","aafda","dfdfb","cdfdf","ddfdf",3],["whats ur name? ","aafda","dfdfb","cdfdf","ddfdf",3],["whats ur name? ","aafda","dfdfb","cdfdf","ddfdf",3],]
level=[100,200,300,400,500,600,700,800]
money=0

for i in range(0,len(question)):
    q=question[i]
    print(f" \n \n--> question for tk {level[i]} \n {i+1}. {q[0]}")
    print(f" a.{q[1]}            b.{q[2]}")
    print(f" c.{q[3]}            d.{q[4]}")

    reply=int(input("enter answer:"))
    if reply == q[-1]:
        print(f"Correct answer u won tk {level[i]}")
        money+=level[i]


    
    else:
        print("wrong ans")
        break

print(f"total money is {money}")



    


import random
num=random.randint(1,20)
guess=int(input("你猜數字是多少"))
if(guess==num):
    print("對")
else:
     print("錯")  
          
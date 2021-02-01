score=input('今天考幾分')
score=int(score)
if(score>=60):
 print("good")
else:
    print("bad")
score=input('今天考幾分')
score=int(score)
if(not(score>0 and score<100)):
  print("wrong")  
elif(score>90 and score<99):
  print("a")
elif(score>80 and score<89):
  print("b")
elif(score>70 and score<79):
  print("c")
elif(score>60 and score<69):
  print("d")
else:
  print("e")
A=input('今天考幾分') 
B=input('今天考幾分') 
A=int(A)
B=int(B)
if(A<60 and B<60):
   print("要處罰")
elif(A>60 and B>60):
   print("有獎品")
else:
    print("有獎品")
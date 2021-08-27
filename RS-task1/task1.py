import random
num=random.randint(1000,9999)
ran =[int(x)for x in str(num)]
# print(f"The random no.is : {num}")
gamepoint=20
user_guess=10
win=1
while(user_guess>=1):
   ran_copy=ran.copy()
   Y=int(input("guess the no."))
   res=[int(i)for i in str(Y)]
   list=[]
   count=0
   wrong=0
   if res==ran:
       gamepoint+=5
   else:
       gamepoint-=2
   for i in range(4):
       if res[i] in ran_copy:

           list.append(res[i])
           if ran_copy.index(res[i])!=i:
               count+=1
           else:
               ran_copy[i]=-1
       else:
           wrong+=1
   if count>0 or wrong>0:
       print(len(list)," digits:",list,"guessed correctly",count,"incorrect position")
       print("no.of turns left",user_guess-1)
   elif count==0 and wrong==0:
       print("congratulations")
       print("your score is :",gamepoint)
       win=0
       break

   user_guess-=1

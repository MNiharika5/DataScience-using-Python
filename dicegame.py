import random
p=[1,2,3,4,5,6]
co=random.choice(p)
print(co)
u=int(input())
if(u>co):
    print("user wins")
elif(u<co):
    print("computer wins")
else:
    u=int(input())

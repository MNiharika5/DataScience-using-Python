def isprime(n):
    c=0
    if(n==2):
        print('Is Prime')
    elif(n==0 or n==1):
        print('Not Prime')
    else:
        for i in range(1,n+1):
            if(n%i==0):
                c+=1
            else:
                c=0
        if(c==2):
            print('Is Prime')
        else:
            print('Not Prime')
def div(n):
    if(n%5==0):
        print('Divisible by 5')
    else:
        print('Not Divisible by 5')
def iseven(n):
    if(n%2==0):
        print('EVEN')
    else:
        print('ODD')
def sumn(n):
    s=n*(n+1)//2
    print(s)
a=int(input())
isprime(a)
div(a)
iseven(a)
sumn(a)
        

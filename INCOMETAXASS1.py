ai=int(input())
hra=int(input())
d=int(input())
t=ai-(hra*12)-d
ti=t-300000
if(ti<300000):
    I=0
elif(ti>=300000 and ti<600000):
    I=(0.1*ti)
elif(ti>=600000 and ti<1000000):
    I=(0.15*ti)
else:
    I=(0.2*ti)
print(I)


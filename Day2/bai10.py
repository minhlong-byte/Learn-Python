n=int(input())
if n<=50:
    print(n*1800,'VND')
elif n>51 and n<=100:
    print(90000+(n-50)*2000)
else:
    print(50*1800+50*2000+(n-100)*2500)
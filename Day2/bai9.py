a,pheptinh,b=map(str,input().split())
a=float(a)
b=float(b)
if pheptinh=='+' :
    print (a+b)
elif pheptinh=='-':
        print(a-b)

elif pheptinh=='*':
        print(a*b)
else :
    if b==0:
        print('Lỗi: Không thể chia cho số 0!')
    else:
        print('%.2f' % (a/b)) 
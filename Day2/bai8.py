a,b,c=int(input()),int(input()),int(input())
if a+b>=c and a+c>=b and c+b>=a:
    print('Tam giác hợp lệ')
else:
    print('Tam giác không hợp lệ')
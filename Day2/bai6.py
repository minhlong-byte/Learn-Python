n=int(input())
if n>35:
    print('Thời tiết Quá nóng, hạn chế ra đường')
elif n>25 and n<=35:
    print('Thời tiết Nóng')
elif n>15 and n<=25 :
    print('Thời tiết Mát mẻ')
else :
    print('Thời tiết Lạnh')
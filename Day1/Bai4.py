S=int(input())
gio=S//3600
du=S%3600
phut=du//60
giay=du%60
print (gio,phut,giay,sep=':')

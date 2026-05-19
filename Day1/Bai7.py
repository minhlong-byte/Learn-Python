x,y,z=map(float,input().split())
print( 'Mỗi người cần trả:','%.1f' %((x+(x*(y/100)))/z),'VND')
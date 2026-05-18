n=int(input())
donvi=n%10
chuc=((n-donvi)/10)%10
tram=n//100

print(int(donvi*100+chuc*10+tram))
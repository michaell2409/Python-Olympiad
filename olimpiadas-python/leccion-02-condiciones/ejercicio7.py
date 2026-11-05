año = int(input())
v1 = año % 4
v2 = año % 100 
v3 = año % 400
if ( v1 ==  0 and v2 != 0 ) or v3 == 0:
    print("bisiesto")
else:
    print("no biesto") 
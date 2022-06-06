# Enter your code here. Read input from STDIN. Print output to STDOUT
import math
AB = int(input())
BC = int(input())
# AC**2 = AB**2 + BC**2
AC = math.sqrt(AB**2 + BC**2)
MC = AC/2
# sin theta = AB/AC
# angle_C = math.acos(BC/AC) #math domain error
# cos A = (b**2 + c**2 - a**2) / 2bc
angle_C = math.asin(1*AB/AC) # math.acos( (AC**2 + BC**2 - AB**2)  / ( 2*AC*BC ) )
angle_B = 90
angle_A = 180 - angle_C - angle_B

BM = math.sqrt( BC**2 + MC**2 - (2*BC*MC* math.cos(angle_C) ) )


# cos A = (b**2 + c**2 - a**2) / 2bc
mbc=math.asin(math.sin(angle_C)*MC/BM)
print(int(round(math.degrees(mbc),0)),'\u00B0',sep='')
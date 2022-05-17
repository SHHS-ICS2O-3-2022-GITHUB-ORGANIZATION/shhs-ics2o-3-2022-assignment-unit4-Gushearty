import math
a = int(input("please enter the first side of the triangle: "))
b = int(input("please enter the second side of the triangle: "))
aa = math.pow(a, 2)
bb = math.pow(b, 2)
hh = aa+bb
cc = math.sqrt(hh)
d = str(cc)
e = str(a)
f = str(b)
print(e+" squared + " +f+" squared equals " + d+" squared")

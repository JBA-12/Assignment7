#Let xi be the possible differences between the number of heads and number of tails 
#Let ni = minimum{number of heads, number of tails}
#Clearly [xi>=0, xi<=6] and 2ni + xi = 6 => xi = 2(3-ni)
#implies [ni>=0, ni<=3]

#Case 1:
n1 = 0
x1 = 2*(3-n1)
print(x1)

#Case 2:
n2 = 1
x2 = 2*(3-n2)
print(x2)

#Case 3:
n3 = 2
x3 = 2*(3-n3)
print(x3)

#Case 4:
n4 = 3
x4 = 2*(3-n4)
print(x4)


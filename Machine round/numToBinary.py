a = 147 #normal number
b = [] #binary number come here as an array/list
while a > 0:
    b.append(a % 2)
    a = a // 2
b.reverse()

print(b)

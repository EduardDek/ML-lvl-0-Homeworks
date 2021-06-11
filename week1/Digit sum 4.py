a= int(input ("please input 4digit number"))
sumdigits =int(a/1000)

for i in range (1, 4):
    sumdigits +=  (int(a/10**(i-1))%(int(a/10**i)*10))


print (sumdigits)



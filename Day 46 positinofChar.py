# Find the index position of a particular character in another string.
var1="My name is Rajesh DaRhal"
char='R'
# index=var1.find(char)
# print(index)


indices=[i for i,c in enumerate(var1) if c==char]
print(indices)


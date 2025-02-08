# Write a program to print the following pattern
# *
# **
# ***
# ****
# *****

n='*'
for i in range(1,6):
    print(i*'*')
# Write a program to print the following pattern
# *
# **
# ***
# **
# *

n='*'
for i in range(1,4):
    print(i*'*')
for i in range(2,0,-1):
    print(i*'*')



# Write  a program to print the following pattern
#         *
#       * * *
#     * * * * *
#    * * * * * * *
# * * * * * * * * *


n=5
for i in range(1,n+1):
    space=' '*(n-i)
    star='*'*(2*i-1)
    print(space+star.strip())


# Write a program to print the following pattern
# 1
# 1 2 1
# 1 2 3 2 1
# 1 2 3 4 3 2 1
# 1 2 3 4 5 4 3 2 1
#
n=5
for i in range(1,n+1):
    inc_num=[str(j) for j in range (1,i+1)]
    # print(''.join(inc_num))
    dec_num = [str(j) for j in range((i - 1),0,-1)]
    # print(''.join(dec_num))
    final=inc_num+dec_num
    print(' '.join(final))

# Write a program to print the following pattern
# 1
# 2 3
# 4 5 6
# 7 8 9 10

n = 4
num = 1

for i in range(1, n + 1):
    row = []
    for j in range(i):
        row.append(str(num))
        num += 1
    print(' '.join(row))

# Print all the armstrong numbers in the range of 100 to 1000
count=100
while count<1000:
    is_armstrong=True
    hundred=count//100
    tens=(count//10)%10
    one=count%10
    # print(hundred,one,tens)
    sum=one**3+tens**3+hundred**3
    if sum!=count:
        is_armstrong=False

    if is_armstrong:
        print(count)
    count+=1


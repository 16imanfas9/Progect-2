import math
def varians_data(numbers):
    num=sum(numbers)
    size=len(numbers)
    global x
    x=num/size
    add=[]
    for i in numbers[0:]:
        Q=(i-x)**2
        add.append(Q)
    G=sum(add)
    result=G/size
    global SD
    SD=math.sqrt(result)
    return result
    
datalist=[int(i)for i in input("enter your numbers with cama:").split(",")]
varianc=varians_data(datalist)
print("the average is:",x)
print("the varianc is:",varianc)
print("the SD is :",SD)

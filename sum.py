def sums(list1):
    list3=[]
    total=0
    for count in range(len(list1)):
        value=0
        value1=list1[count]
        
        total=total + value1
        list3=list3+[total]
    return list3    
l1=[10,41,20,221]
l3=sums(l1)
print(l1)
print(l3)
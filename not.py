def nots(list1):
    list3=[]
    for count in range(len(list1)):
        value=0
        value1=list1[count] & 1
        value=(value1 + 1) & 1
        list3=list3+[value]
    return list3    
l1=[0,1,0,1]

l3=nots(l1)
print(l1)
print(l3)
def ors(list1,list2):
    list3=[]
    for count in range(len(list1)):
        value=0
        value1=list1[count] & 1
        value2=list2[count] & 1
        value=value1 | value2
        list3=list3+[value]
    return list3    
l1=[0,1,0,1]
l2=[0,0,1,1]
l3=ors(l1,l2)
print(l1)
print(l2)
print(l3)
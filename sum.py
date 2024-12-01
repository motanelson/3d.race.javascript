def sums(list1,list2):
    list3=[]
    for count in range(len(list1)):
        value=0
        value1=list1[count]
        value2=list2[count]
        value=value1 + value2
        list3=list3+[value]
    return list3    
l1=[10,41,20,221]
l2=[112,41,21,211]
l3=sums(l1,l2)
print(l1)
print(l2)
print(l3)
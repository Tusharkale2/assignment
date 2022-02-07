list1=[int(x) for x in input("Enter List:").split()]
print(list(filter(lambda x: x%3==0 and x%6==0,list1)))

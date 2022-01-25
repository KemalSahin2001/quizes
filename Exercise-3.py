list1=[1,2,3,4,5,6,7,8,9]
list2=[2,3,5,6,8]
lst = [x ** 2 for x in list1 if x not in list2]
print(lst)
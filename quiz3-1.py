import sys
a = int(input())
b = int(input())
mult_a_b = a**b
print("{}^{} = {}".format(a,b,mult_a_b),end="")
while len(str(mult_a_b)) > 1:
    sum_of_a_b = 0
    listofnumb = list()   
    for i in str(mult_a_b):
        listofnumb.append(i)
        sum_of_a_b += int(i)
    print(" = {} = {}".format(" + ".join(listofnumb),sum_of_a_b),end="")
    mult_a_b = sum_of_a_b
print()





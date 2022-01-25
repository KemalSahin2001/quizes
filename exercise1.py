def recursion():
    inpt = input("give a list:").split(" ")
    lst = [int(i) for i in inpt]
    print(f"Maximum: {maximum(lst)}")
    print(f"Minimum: {minimum(lst)}")
    print(f"Average: {avarage(lst)}")
def maximum(lst):
    if len(lst) <= 1:
        return lst[0]
    else:
        m = maximum(lst[1:])
        return m if m > lst[0] else lst[0]
def minimum(lst):
    if len(lst) <= 1: return lst[0]
    else:
        m = minimum(lst[1:])
        return m if m < lst[0] else lst[0]    
def avarage(lst):
    if len(lst) == 1: return lst[0]
    else: return (lst[0] + ((len(lst) - 1) * avarage(lst[1:]))) / len(lst)
recursion()

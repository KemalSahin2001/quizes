import sys
def Even_Number_Elevator(string):
        number_list = [int(x) for x in string.split(',') if int(x) > 0]
        Even_Numbers = [x for x in number_list if x % 2 == 0]
        print("Even numbers:",Even_Numbers)
        print("Sum of even numbers: ",sum(Even_Numbers))
        print("Even number rate: ",round(sum(Even_Numbers)/sum(number_list),3))               
def main():
    try:
        string_list = sys.argv[1]
        Even_Number_Elevator(string_list)
    except:
        print("Use only integer as input.")
main()

    
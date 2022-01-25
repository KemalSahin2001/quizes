import sys
def func(div,nondiv,frm,to): return [str(i) for i in range(frm,to + 1) if i % div == 0 and i % nondiv != 0]
try:
    with open(sys.argv[2]) as comparison: comparison_data = [comps.split(" ") for comps in comparison.read().splitlines()]
    try:
        with open(sys.argv[1]) as data:
                for line in data.read().splitlines():
                    line = line.split(" ")
                    print("-" * 12)
                    try:
                        result = func(div = int(float(line[0])),nondiv = int(float(line[1])),frm = int(float(line[2])),to = int(float(line[3])))
                        print("My results:\t\t {}\nResults to compare:\t {}".format(" ".join(result)," ".join(comparison_data[0])))
                        assert result == comparison_data[0]
                        print("Goool!!!")
                    except ValueError: print("ValueError: only numeric input is accepted.\nGiven input: {}".format(" ".join(line)))
                    except IndexError: print("IndexError: number of operands less than expected.\nGiven input: {}".format(" ".join(line)))
                    except ZeroDivisionError: print("ZeroDivisionError: You can't divide by 0.\nGiven input: {}".format(" ".join(line)))
                    except AssertionError: print("AssertionError: results don’t match.")  
                    comparison_data.pop(0)
    except IOError: print("IOError: cannot open {}".format(sys.argv[1])) 
except IOError: print("IOError: cannot open {}".format(sys.argv[2]))               
except IndexError: print("IndexError: number of input files less than expected")
except: print("”kaBOOM: run for your life!")
finally: print("\n˜ Game Over ˜")






def line1(n):
    if n in [0,5,10,15,20]:
        print("+---"*4+'+')
    else:
        print("1   "*4+'+')
for i in range(21):
    line1(i)

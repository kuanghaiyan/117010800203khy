i = 0
def move(n,a,buffer,c):
    global i
    if n == 1:
        i += 1
        print('move','a','-->',c)
    else:
        move(n-1,a,c,buffer)
        move(1,a,buffer,c)
        move(n-1,buffer,a,c)

move(4,'a','buffer','c')

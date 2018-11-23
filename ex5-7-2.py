i = 0
def move(n,a,b,c):
    global i
    if n==1:
        i += 1
        print('移动第',i,'次',a,'-->',c)
    else:
        move(n-1,a,c,b) 
        move(1,a,b,c)
        move(n-1,b,a,c)

        
move(4,'A','B','C')

import turtle as t
edge = 5
step = 5
def draw():
    global edge
    t.fd(edge)
    if t.isdown() == False:
        t.pendown()
    t.left(90)
    t.fd(edge)
    t.left(90)
    edge += step
    t.fd(edge)
    t.left(90)
    t.fd(edge)
    turtle.fd(edge)    
    turtle.left(90)
    turtle.fd(edge)
    turtle.left(90)
    edge = edge + 10

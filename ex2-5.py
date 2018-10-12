import turtle as t
t.pensize(3)
for i in range(4):
  t.fd(150)
  t.seth(60+120*i)
for i in range(4):
  t.fd(150)
  t.seth(300+240*i)
for i in range(4):
  t.fd(-150)
  t.seth(60+120*i)
for i in range(1):
  t.fd(-300)
  t.seth(300+240*i)
t.done()

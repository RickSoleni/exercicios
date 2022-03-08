import turtle

bob = turtle.Turtle()


print(bob)


def poligono(t, n, length):
    angle = 360 / n
    for i in range(n):
        t.fd(length)
        t.lt(angle)


poligono(bob, 22, 5)

turtle.mainloop()

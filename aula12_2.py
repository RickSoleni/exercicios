import turtle


class Point:
    """Classe que representa um ponto em um plano 2D."""

    def __init__(self, x: float, y: float) -> None:
        self.x = x
        self.y = y


class Retancle:
    """Classe para representar um retângulo."""

    def __init__(self, width: float, height: float, corner: Point) -> None:
        self.width = width
        self.height = height
        self.corner = corner


class Circle:
    """Classe que representa um círculo em um plano 2D."""

    def __init__(self, radius: float, center: Point) -> None:
        self.radius = radius
        self.center = center


def draw_rect(bob, retangulo):  # função para desenhar um retangulo
    bob.penup()
    bob.setpos(retangulo.corner.x, retangulo.corner.y)
    bob.pendown()
    for _ in range(2):
        bob.fd(retangulo.width)
        bob.lt(90)
        bob.fd(retangulo.height)
        bob.lt(90)


def draw_circle(bob, circulo):  # função para desenhar um círculo
    bob.penup()
    bob.setpos(circulo.center.x, circulo.center.y)
    bob.pendown()
    bob.circle(circulo.radius)


ponto = Point(30, 5)  # ponto do início do retangulo

ponto2 = Point(-200, -20)  # ponto do centro do círculo

retangulo = Retancle(
    100, 50, ponto
)  # atributos base, altura e ponto inicial do retangulo

circulo = Circle(100, ponto2)  # atributos raio e ponto central do circulo

tartaruga = turtle.Turtle()  # atribuição de tartaruga

print(draw_rect(tartaruga, retangulo))
print(draw_circle(tartaruga, circulo))

turtle.mainloop()

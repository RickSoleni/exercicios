class Point:
    """Classe que representa um ponto em um plano 2D."""

    x: float
    y: float


class Circle:
    """Classe que representa um círculo em um plano 2D."""

    radius: float
    center: Point


circulo = Circle()
circulo.radius = 75
circulo.center = Point()
circulo.center.x = 150
circulo.center.y = 100

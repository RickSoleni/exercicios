class Kangaroo:
    """Classe para canguru."""

    def __init__(self, name: str):
        self.name = name
        self.pouch_contents = list()

    def put_in_pouch(self, item):
        self.pouch_contents.append(item)
        return self

    def __str__(self):
        return f'Kang {self.name} tem um {self.pouch_contents} na bolsa'


kanga = Kangaroo('rogerio')
roo = Kangaroo('Jose')
kanga.put_in_pouch(roo)


print(roo)

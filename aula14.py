class Time:
    """Represents the time of day.
    attributes: hour, minute, second
    """

    def __init__(self, hour: int, minute: int, second: int):
        self.hour = hour
        self.minute = minute
        self.second = second

    def __str__(self) -> str:
        return f'{self.hour:0>2}:{self.minute:0>2}:{self.second:0>2}'

    def __repr__(self) -> str:
        return f'{self.hour:0>2}:{self.minute:0>2}:{self.second:0>2}'

    def __gt__(self, t2) -> bool:
        total_seconds_self = (
            (self.hour * 60 * 60) + (self.minute * 60) + (self.second)
        )
        total_seconds_t2 = (t2.hour * 60 * 60) + (t2.minute * 60) + (t2.second)
        return total_seconds_self > total_seconds_t2

    def __lt__(self, t2) -> bool:
        total_seconds_self = (
            (self.hour * 60 * 60) + (self.minute * 60) + (self.second)
        )
        total_seconds_t2 = (t2.hour * 60 * 60) + (t2.minute * 60) + (t2.second)
        return total_seconds_self < total_seconds_t2

    def is_after(self, other_time):
        self.total_seconds = (
            (self.hour * 60 * 60) + (self.minute * 60) + self.second
        )

        other_total_seconds = (
            (other_time.hour * 60 * 60)
            + (other_time.minute * 60)
            + other_time.second
        )

        if self.total_seconds > other_total_seconds:
            return True
        return False

    def __add__(self, t2):
        sec = self.add_time(t2)
        resultado = self.convert_seconds(sec)
        return resultado

    def __sub__(self, t2):
        sec = self.sub_time(t2)
        resultado = self.convert_seconds(sec)
        return resultado

    def __mul__(self, t2):
        sec = self.multiplic_time(t2)
        resultado = self.convert_seconds(sec)
        return resultado

    def add_time(self, t2):
        total_seconds_self = (
            (self.hour * 60 * 60) + (self.minute * 60) + (self.second)
        )
        total_seconds_t2 = (t2.hour * 60 * 60) + (t2.minute * 60) + (t2.second)
        total_seconds = total_seconds_self + total_seconds_t2
        return total_seconds

    def sub_time(self, t2):
        total_seconds_self = (
            (self.hour * 60 * 60) + (self.minute * 60) + (self.second)
        )
        total_seconds_t2 = (t2.hour * 60 * 60) + (t2.minute * 60) + (t2.second)
        total_seconds = total_seconds_self - total_seconds_t2
        return total_seconds

    def multiplic_time(self, t2):
        total_seconds_self = (
            (self.hour * 60 * 60) + (self.minute * 60) + (self.second)
        )
        total_seconds_t2 = (t2.hour * 60 * 60) + (t2.minute * 60) + (t2.second)
        total_seconds = total_seconds_self * total_seconds_t2
        return total_seconds

    def convert_seconds(self, seconds):
        _, seconds = divmod(seconds, 86400)
        hours, seconds = divmod(seconds, 3600)
        minutes, seconds = divmod(seconds, 60)
        return hours, minutes, seconds

    def segundos_desde_meia_noite(self):
        total_segundos = (
            (self.hour * 60 * 60) + (self.minute * 60) + (self.second)
        )
        return print(
            f'Passaram-se {total_segundos} segundos desde a meia noite'
        )


agora = Time(4, 0, 0)
duas_horas = Time(8, 0, 0)
agora.segundos_desde_meia_noite()
resultado = agora > duas_horas
print(resultado)

class Clock:

    def __init__(self, hour, minute):
        mod, self.minute = divmod(minute, 60)
        rm, self.hour = divmod(hour + mod, 24)

    def __repr__(self):
        return f"{self.hour:02d}:{self.minute:02d}"

    def __eq__(self, other):
        return repr(self) == other

    def __add__(self, minutes):
        return Clock(self.hour, self.minute + minutes)

    def __sub__(self, minutes):
        return self.__add__(- minutes)

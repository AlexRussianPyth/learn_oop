class IgnitionSystem:
    @staticmethod
    def produce_spark():
        return True


class Engine:
    def __init__(self):
        self.revs_per_minute = 0

    def turn_on(self):
        self.revs_per_minute = 2000

    def turn_off(self):
        self.revs_per_minute = 0


class FuelTank(object):
    def __init__(self, level=30):
        self._level = level

    @property
    def level(self):
        return self._level

    @level.setter
    def level(self, level: int):
        self._level = level


class DashBoardLight:
    def __init__(self, is_on=False):
        self._is_on = is_on

    def __str__(self):
        return self.__class__.__name__

    @property
    def is_on(self):
        return self._is_on

    @is_on.setter
    def is_on(self, status: bool):
        self._is_on = status

    def status_check(self):
        if self._is_on:
            print("{}: ON".format(str(self)))
        else:
            print("{}: OFF".format(str(self)))


class HandBrakeLight(DashBoardLight):
    pass


class FogLampLight(DashBoardLight):
    pass


class Dashboard:
    def __init__(self):
        self.lights = {"handbreak": HandBrakeLight(), "fog": FogLampLight()}

    def show(self):
        for light in self.lights.values():
            light.status_check()

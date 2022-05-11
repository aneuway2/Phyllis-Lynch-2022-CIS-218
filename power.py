"""
CIS-218 Final Lab 5-8-22 Phyllis Lynch
"""


class Power:
    """create class"""

    def __init__(self, name, megawatts, age, lifespan=60):
        self.name = name
        self.megawatts = megawatts
        self.age = age
        self.lifespan = lifespan

    def capacity(self):
        """capacity of plant"""
        return round(abs(self.megawatts / self.lifespan * self.age) - self.megawatts)

    def available(self):
        """avail capacity"""
        if (self.capacity()) >= 1:
            return True

    def __str__(self):
        """string for Power"""
        return "Power plant " + self.name + "(" + str(self.capacity()) + ")"

    def __repr__(self):
        """repr for power"""
        return (
            "name "
            + str(self.name)
            + " megawatts "
            + str(self.megawatts)
            + " age "
            + str(self.age)
            + " lifespan "
            + str(self.lifespan)
        )


class Wind(Power):
    """subclass of power"""

    def __init__(self, name, megawatts, age, lifespan=25):
        super().__init__(name, megawatts, age)
        self.lifespan = 25


class Nuclear(Power):
    """subclass of power"""

    def __init__(self, name, megawatts, age, cooling_towers, lifespan=60):
        super().__init__(name, megawatts, age, lifespan)
        self.__cooling_towers = cooling_towers

    def available(self):
        if (self.capacity()) == round(self.__cooling_towers * 100):
            return true


def test_wind():
    """test wind"""
    albert = test_wind()
    assert albert.capacity == 25
    assert albert.available is true


def test_nuclear():
    """test nuke"""
    yip = Nuclear("nuke", 600, 10, 10)
    assert yip.capacity == 500
    assert yip.available is False


def test_power():
    """test print in power"""
    zing = Power("test", 100, 0)
    assert print(zing)


if __name__ == "__main__":
    test_power()
if __name__ == "__main__":
    power_plants = [
        Wind(name="Alta Wind Energy", megawatts=1320, age=12),
        Wind(name="Roscoe Wind Farm", megawatts=781, age=10),
        Wind(name="Shepherds Flat Wind Farm", megawatts=845, age=13),
        Nuclear(name="Palo Verde", megawatts=3942, age=36, cooling_towers=3),
        Nuclear(name="Browns Ferry", megawatts=3300, age=48, cooling_towers=6),
        Nuclear(name="South Texas", megawatts=2560, age=34, cooling_towers=0),
    ]
    available = [_ for _ in power_plants if _.available()]
    order = sorted(available, reverse=True, key=lambda plant: plant.capacity())
    named_list = [str(_) for _ in order]
    print(named_list)

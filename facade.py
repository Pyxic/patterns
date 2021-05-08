class Power:

    def on(self):
        print("power on")

    def off(self):
        print("power off")


class DVDRom:

    _data = False

    @property
    def data(self):
        return self._data

    @data.setter
    def data(self, value):
        self._data = value

    def load(self):
        self._data = True

    def unload(self):
        self.data = False


class HDD:

    def copy_from_dvd(self, dvd_rom: DVDRom):
        if dvd_rom.data:
            print("copy from dvd to hdd")
        else:
            print("data is empty")


class Computer:

    hdd = HDD()
    dvd_rom = DVDRom()
    power = Power()

    def copy(self):
        self.power.on()
        self.dvd_rom.load()
        self.hdd.copy_from_dvd(self.dvd_rom)


computer = Computer()
computer.copy()


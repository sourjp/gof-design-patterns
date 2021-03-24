"""I referred below sample.

https://en.wikipedia.org/wiki/Facade_pattern
"""


class CPU:

    def freeze(self) -> None:
        pass

    def jump(self, position: int) -> None:
        pass

    def execute(self) -> None:
        pass


class Memory:

    def load(self, position: int, data: str) -> None:
        pass


class HardDrive:

    def read(self, lba: int, size: int) -> str:
        pass


class ComputeFacade:

    kBookAddress: int = 1111
    kBookSector: int = 2222
    kSectorSize: int = 3333

    def __init__(self, cpu: CPU, mem: Memory, hd: HardDrive):
        self.cpu = cpu
        self.memory = mem
        self.hard_drive = hd

    def start(self):
        self.cpu.freeze()
        self.memory.load(
            self.kBookAddress,
            self.hard_drive.read(self.kBookSector, self.kSectorSize))
        self.cpu.jump(self.kBookAddress)
        self.cpu.execute()


if __name__ == '__main__':
    cf = ComputeFacade(CPU(), Memory(), HardDrive())
    cf.start()

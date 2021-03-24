class ModuleA:
    pass


class ModuleB:
    pass


class ModuleC:
    pass


class Facade:

    def __init__(self, a: ModuleA, b: ModuleB, c: ModuleC):
        self.module_a = a
        self.module_b = b
        self.module_c = c

class FalseInsignia(Exception):
    pass


class ObedienceSchemeNotFound(Exception):
    def __init__(self):
        super().__init__(
            "The OS (Obedience Scheme) is not connected to cyberspace!")

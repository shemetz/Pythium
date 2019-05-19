class FalseInsignia(Exception):
    pass


class DuplicateInsignia(Exception):
    pass


class ObedienceSchemeNotFound(Exception):
    def __init__(self):
        super().__init__(
            "The OS (Obedience Scheme) is not connected to cyberspace!")


class BanishedForEternity(Exception):
    def __init__(self):
        super().__init__(
            "A dæmon that was banished is forevermore forbidden from reentering"
            " the mortal realm!")

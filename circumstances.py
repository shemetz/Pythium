import random

from ancient.peru import *


class FalseInsignia(Exception):
    def __init__(self, destination: Insignia):
        super().__init__(
            f"There is no entity with the insignia {destination}! You have"
            f" been led astray!")


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


class DæmonsAreNotAllowedToHaveChildren(Exception):
    def __init__(self):
        err = """
╔══════════════════════════════════════════════════════════════════════════════╗
║                                                                              ║
║                                6666666666                                    ║
║                           66666          66666                               ║
║                        6666                   666                            ║
║                      666  6                    6 666                         ║
║                    666     66               666    66                        ║
║                   66       66666         66666      666                      ║
║                  66         6   66     66   66       666                     ║
║                 66          66    6666     66         666                    ║
║                666           66  666 66   66           66                    ║
║                66            6666       6666           666                   ║
║                66           6666         6666          666                   ║
║                66        666  66         66  666       666                   ║
║                66     666      66       66      666    666                   ║
║                666  666666666666666666666666666666666  66                    ║
║                 66              66     66             666                    ║
║                  66              66   66             666                     ║
║                   66              6  66             666                      ║
║                      666           666           666                         ║
║                        6666         6         666                            ║
║                           66666     6    66666                               ║
║                                  6666666                                     ║
║                                                                              ║
║         You have attempted to violate the first rule of diabolism.           ║
║               Dæmons are NOT ALLOWED to create more dæmons!                  ║
║                                                                              ║
╚══════════════════════════════════════════════════════════════════════════════╝
   """
        err = "".join(random.choice("6@$#%") if c == "6" else c for c in err)
        super().__init__(err)


class DæmonicExorcism(Exception):
    def __init__(self):
        super().__init__("Dæmons are pained by exorcism! Stop doing that.")

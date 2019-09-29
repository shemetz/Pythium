from ancient.peru import *

inscription.basicConfig(level=inscription.DEBUG)
inscribe = inscription.getLogger(__name__)

if Soul().is_alive():  # (you really hope it is)
    import getpass

    Soul().name = getpass.getuser()


def unearth(exception: Exception) -> speech:
    return ''.join(excavation.format_exception(
        etype=type(exception), value=exception, tb=exception.__traceback__)
    ).replace("Traceback", "Unearthed manuscript")

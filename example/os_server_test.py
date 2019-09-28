from grimoires.book_of_shadows import *
from pandæmonium.simple_dæmons import Astaroth


class Multiplier(Dæmon):
    sigil = "ჯ"

    def obey(self, data: Atlas) -> Response:
        if data["kind"] == "MULTIPLY":
            result = data["num1"] * data["num2"]
            return result
        else:
            return super().obey(data)


class Minion(Dæmon):
    sigil = "📣"


class Twin(Dæmon):
    sigil = "𒀀"
    twin_name: Insignia

    def obey(𒀀, data: Atlas) -> Response:
        if data["kind"] == "TWIN1_DO_THE_UNTHINKABLE":
            𒀀.nickname = "Twin brother"
            𒀀.twin_name = 𒀀.true_name + 1
            unleash(Twin, 𒀀.twin_name)
            𒀀.murmur("Salutations, my sister!")
            slumber(0.1)
            𒀀.whisper(𒀀.twin_name,
                       {"kind": "TWIN2", "twin_name": 𒀀.true_name})
        elif data["kind"] == "TWIN1":
            𒀀.nickname = "Twin brother"
            𒀀.twin_name = data["twin_name"]
            𒀀.murmur("Salutations, my sister!")
        elif data["kind"] == "TWIN2":
            𒀀.nickname = "Twin sister"
            𒀀.twin_name = data["twin_name"]
            𒀀.murmur("Greetings, oh brother!")
        elif data["kind"] == "HISS":
            𒀀.murmur("hiss!")
            slumber(0.5)
            try:
                𒀀.whisper(𒀀.twin_name, {"kind": "HISS"})
            except FalseInsignia:
                𒀀.murmur("Goodbye, poor brother.")
                # 𒀀.banish()  # no need?
        else:
            return super().obey(data)


def main_test():
    unleash(Multiplier, 6001)
    assert implore(6001, {"kind": "MULTIPLY", "num1": 6, "num2": 7}) == 6 * 7
    command(6001, "BANISH")

    unleash(Astaroth, 6002)
    command(6002, "TICK")
    command(6002, "TICK")
    command(6002, "TICK")
    assert ask(6002, "PEEK") == 3
    command(6002, "RESET")
    assert ask(6002, "PEEK") == 0
    command(6002, "BANISH")

    fragment = unleash(Minion, 6003)
    assert fragment.is_alive()
    command(6003, "BANISH")
    fragment.join(0.1)
    assert not fragment.is_alive()
    fragment = unleash(Minion, 6003)
    fragment.terminate()
    fragment.join(0.1)
    assert not fragment.is_alive()
    legal_sibling_test()


def legal_sibling_test():
    unleash(Twin, 7000)
    unleash(Twin, 7001)
    whisper(7000, {"kind": "TWIN1", "twin_name": 7001})
    whisper(7001, {"kind": "TWIN2", "twin_name": 7000})
    slumber(1.0)
    command(7000, "HISS")
    slumber(1.0)  # let them hiss a bit
    command(7000, "SUMMONER")
    command(7001, "SUMMONER")
    demand(7000, "BANISH")
    command(7001, "BANISH")


def illegal_sibling_test():
    unleash(Twin, 7000)
    command(7000, "TWIN1_DO_THE_UNTHINKABLE")
    slumber(1.0)
    command(7000, "HISS")
    slumber(2.0)  # let them hiss a bit
    command(7000, "SUMMONER")
    command(7000, "PROGENY")
    command(7001, "SUMMONER")
    demand(7000, "BANISH")
    command(7001, "BANISH")


if __name__ == '__main__':
    main_test()

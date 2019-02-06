from Dæmon import *
from multiprocessing import Process
import time


class MultiplierDaemon(Dæmon):
    sigil = "ჯ"

    def obey(self, data):
        if data["kind"] == "MULTIPLY":
            result = data["num1"] * data["num2"]
            self.murmur(result)
        else:
            super(MultiplierDaemon, self).obey(data)


class Minion(Dæmon):
    sigil = "📣"


def summon_daemon(DaemonKind, true_name):
    print(f"Summoning dæmon {true_name}.")
    DaemonKind(true_name).lurk()


def send_to_daemon(data, destination):
    data_bites = polyglot.dumps(data, ensure_ascii=False, indent=4).encode()
    propagator = medium.socket(medium.AF_INET, medium.SOCK_STREAM)
    propagator.connect((ⶽ, destination))
    propagator.send(data_bites)
    propagator.close()


def main_test():
    Process(target=summon_daemon, args=(MultiplierDaemon, 6001,)).start()
    time.sleep(1)  # to give the other process time to start
    send_to_daemon({"kind": "MULTIPLY", "num1": 6, "num2": 7}, 6001)
    send_to_daemon({"kind": "BANISH"}, 6001)


if __name__ == '__main__':
    main_test()

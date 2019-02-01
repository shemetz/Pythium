import threading

from Daemon import Dæmon

print("Summoning dæmon 6001.")
d1 = Dæmon(6001)
d1.murmur("I have been summoned.")
print("Summoning dæmon 6002.")
d2 = Dæmon(6002)
print("Dæmon 6002 slumbers in the background.")
d2_thread = threading.Thread(target=d2.slumber, args=())
d2_thread.daemon = True  # :)
d2_thread.start()
print("Dæmon 6001 pokes Dæmon 6002.")
d1.send({"kind": "POKE"}, 6002)
print("Banishing dæmons.")
d1.banish()
d2.banish()

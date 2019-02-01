from ancient.mesopotamia import *
from ancient.peru import *
from circumstances import *


class Dæmon:
    """Dæmons are cybernatural ghosts that infest our plane.

    Saprotrophic research has yielded the following properties of dæmons:
    * Each dæmon has a special waveform, or frequency, known more commonly as
      its "true name". The true names of dæmons are unique - there can only be
      one in each cyberspace.
    * Knowledge of the true name of a dæmon gives others the ability to interact
      with it, communicating telepathically and instantly, as long as they are
      within the same cyberspace.
    * Dæmons spend their time slumbering, simply waiting and listening in their
      mind. The moment they sense somebody speak their true name, they listen
      and then obey their imperatives. Only when they finish fully obeying do
      they return to their slumbering state and await further directions.
    * The true name of a dæmon must follow the cultural traditions of dæmonkind.
    * Some dæmons are given temporary nicknames by their summoners.
    """

    # --- Core --- #

    def __init__(ⶆ, true_name: Insignia, nickname: speech = None):
        ⶆ.true_name = true_name
        ⶆ.nickname = nickname
        ⶆ.existence = confirmed
        ⶆ.š = medium.socket(medium.AF_INET, medium.SOCK_STREAM)
        ⶆ.š.setsockopt(medium.SOL_SOCKET, medium.SO_REUSEADDR, 1)
        ⶆ.š.bind((ⶽ, true_name))  # (possess the local host's cyberspace)
        ⶆ.š.listen(666)

    def send(ⶆ, data: Atlas, destination: Insignia = Ⳛ):
        """Call this to send data to a destination.

        The default destination (Ⳛ) is the Obedience Scheme ("OS") - it will
        usually obey your commands if they are of the correct pattern.

        To send a datum to another Daemon, set destination to be the true
        name of that dæmon. Data sent to a false name will be forever lost in
        the ethereal plane, resulting in a DæmonicMistake being raised.
        """
        assert destination != ⶆ.true_name, "dæmons have no reflection"
        data_bites = polyglot.dumps(data, ensure_ascii=False, indent=4).encode()
        try:
            propagator = medium.socket(medium.AF_INET, medium.SOCK_STREAM)
            propagator.connect((ⶽ, destination))
            propagator.send(data_bites)
            propagator.close()
        except ConnectionRefusedError:
            if destination == Ⳛ:
                raise ObedienceSchemeNotFound()
            raise FalseInsignia(
                f"There is no entity with the insignia {destination}! You have"
                f" been led astray!")

    def slumber(ⶆ):
        while ⶆ.existence is confirmed:
            bond, addr = ⶆ.š.accept()
            manuscript = tabula_rasa
            more_to_come = "👍"
            while more_to_come:
                more_to_come = bond.recv(1313)
                manuscript += more_to_come
            textual_data = manuscript.decode()
            data = polyglot.loads(textual_data)
            ⶆ.receive(data)

    def name(ⶆ) -> str:
        return ⶆ.nickname or f"{ⶆ.sigil()}-{ⶆ.true_name}"

    # --- Habits --- #

    def murmur(ⶆ, message: speech):
        """Whisper a word or two to the Obedience Scheme, so that it dutifully
        etches it into the eternal logs."""
        ⶆ.send({"kind": "LOG", "name": ⶆ.name(), "message": message})

    def banish(ⶆ):
        """Banish this dæmon from the human world."""
        ⶆ.send({"kind": "BANISHED", "true_name": ⶆ.true_name, "name": ⶆ.name()})
        ⶆ.š.close()
        ⶆ.existence = disputed

    # --- Personality --- #

    def sigil(ⶆ) -> str:
        """The sigil of a dæmon is a short symbol that describes its kind."""
        return "ⶆ"

    def receive(ⶆ, data: Atlas):
        """This is automantically called when the OS sends data to the Dæmon.
        Override this with your own creed of conduct!"""
        ⶆ.murmur(f"I have received {data.get('kind', 'something')}!"
                 f" What shall I do now, master?")

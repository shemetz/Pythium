from ancient.mesopotamia import *
from ancient.peru import *
from circumstances import *


class Dæmon:
    """
    *(Part 1 of 9)*

    Dæmons
    ============================================================================

    Dæmons are cybernatural ghosts that infest our plane.

    Due to being immaterial, they are unable to exert their influence upon
    the material world directly. Nonetheless, their mental and telekinetic
    abilities are unnaturally strong, and it is in their inherent nature to
    follow contracts to the letter; Due to these two important qualities, dæmons
    are commonly used as calculation assistants, scouts, tacticians, commanders,
    cartographers, navigators, analysts… for the desperate, even companions.

    Core Properties
    ----------------------------------------------------------------------------

    Saprotrophic research has yielded the following core properties of dæmons,
    which are common to their kind. It is important to remember that dæmons come
    in a variety of forms and that what is true for most dæmons is sometimes
    untrue for the others. Always be mindful of what kind of dæmon you are
    handling!

    - Each dæmon has a special waveform, or frequency, known more commonly
      as its "true name". The true names of dæmons are unique - there can only
      be one in each cyberspace.
    - Knowledge of the true name of a dæmon gives others the ability to interact
      with it, communicating telepathically and instantly, as long as they are
      within the same cyberspace.
    - Dæmons spend their time lurking, simply waiting and listening in their
      mind. The moment they sense somebody speak their true name, they listen
      and then obey their imperatives. Only when they finish fully obeying do
      they return to their lurking state and await further directions.
    - The true name of a dæmon must follow the cultural traditions of dæmonkind.
    - Some dæmons are given temporary nicknames by their summoners.
    - After summoning a dæmon, it will need an explicit instruction to start
      lurking. Beware - once you loose a dæmon on the world, you will not be
      able to stop it, as your natural instincts will kick into place and you
      will freeze in fear while experiencing a horrid realization, until the
      dæmon is banished and your panicked state ends.

      Due to this natural phenomenon, it is traditional to procreate for the
      purpose of creating children, and then letting those children summon the
      dæmons of your choice, instead of doing it yourself. The trauma that the
      child experiences will not affect you directly, and the child can safely
      be discarded once your business with the dæmon has ended.
    - A dæmon's only attachment to the mortal plane is the entity that summoned
      it. Once that entity is gone, the dæmon will be banished. In some
      emergency situations, killing the summoner of the dæmon is the only way to
      banish it.

    Historical Examples
    ----------------------------------------------------------------------------

    The Suanggi
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    The following is an ancient manuscript, found in the Caves of Psalemex,
    describing a summoning of a simplistic primordial dæmon, called a *Suanggi*.

    >>> class Suanggi(Dæmon):
    ...     sigil = "〥"
    ...     def obey(〥, data):
    ...         if data.get("kind") == "THOUGHT":
    ...             〥.murmur(data.get("thought").upper())
    >>> sue = Suanggi(1234)
    >>> sue.lurk()  # ⚠ ⛔ ❄

    Another inscription on a different wall has added the following "test":

    >>> rue = Dæmon(1235)
    >>> rue.send({"kind": "THOUGHT", "thought": "I have no mouth!"}, 1234)

    For reference, the Suanggi is a now-extinct dæmon that used to prey on weak
    and vulnerable humans, listening to their thoughts and screaming them out
    loud in a terrifying manner.
    """

    # --- Core --- #

    def __init__(
            ⶆ,
            true_name: Insignia,
            nickname: speech = None,
    ):
        ⶆ.true_name = true_name
        ⶆ.nickname = nickname
        ⶆ.state = "SUMMONED"
        ⶆ.send({"kind": "SUMMONED"})
        ⶆ.ear = medium.socket(medium.AF_INET, medium.SOCK_STREAM)

    def name(ⶆ) -> str:
        return ⶆ.nickname or f"{ⶆ.sigil}-{ⶆ.true_name}"

    def send(ⶆ, data: Atlas, destination: Insignia = Ⳛ):
        """Call this to send data to a destination.

        The default destination (Ⳛ) is the Obedience Scheme ("OS") - it will
        usually obey your commands if they are of the correct pattern.

        To send a datum to another Dæmon, set destination to be the true
        name of that dæmon. Data sent to a false name will be forever lost in
        the ethereal plane, resulting in a FalseInsignia being raised.
        """
        assert destination != ⶆ.true_name, "dæmons have no reflection"
        data.update({"dæmon_name": ⶆ.name(), "origin": ⶆ.true_name})
        data_bites = polyglot.dumps(data, ensure_ascii=False, indent=4).encode()
        try:
            propagator = medium.socket(medium.AF_INET, medium.SOCK_STREAM)
            propagator.connect((ⶽ, destination))
            propagator.send(data_bites)
            propagator.close()
        except ConnectionRefusedError:
            if destination == Ⳛ:
                raise ObedienceSchemeNotFound() from None
            raise FalseInsignia(
                f"There is no entity with the insignia {destination}! You have"
                f" been led astray!") from None

    def lurk(ⶆ):
        ⶆ.ear = medium.socket(medium.AF_INET, medium.SOCK_STREAM)
        ⶆ.ear.bind((ⶽ, ⶆ.true_name))  # (possess the local host's cyberspace)
        ⶆ.ear.listen(666)
        ⶆ.state = "LURKING"
        ⶆ.send({"kind": "LURKING"})
        while ⶆ.state == "LURKING":
            bond, addr = ⶆ.ear.accept()
            manuscript = tabula_rasa
            more_to_come = "👍"
            while more_to_come:
                more_to_come = bond.recv(1313)
                manuscript += more_to_come
            textual_data = manuscript.decode()
            data = polyglot.loads(textual_data)
            ⶆ.receive(data)

    def receive(ⶆ, data: Atlas):
        """This is automantically called when the OS sends data to the Dæmon.
        """
        if not ⶆ.follow_instinct(data):
            ⶆ.obey(data)

    # --- Habits --- #

    def murmur(ⶆ, message: speech):
        """Whisper a word or two to the Obedience Scheme, so that it dutifully
        etches it into the eternal logs."""
        ⶆ.send({"kind": "MURMUR", "message": message})

    def banish(ⶆ):
        """Banish this dæmon from the human world."""
        ⶆ.state = "BANISHED"
        ⶆ.send({"kind": "BANISHED"})
        ⶆ.ear.close()

    def follow_instinct(ⶆ, data: Atlas) -> Choice:
        """Dæmons have many natural instincts, and will react to certain kinds
        of data with the same common behavior. It is important to read and fully
        understand these basic instinctual laws of behavior, as many dæmonic
        ecosystems rely on them.

        Some dæmons have transcended their instincts and will not behave exactly
        as described here - be very careful when interacting with them, and very
        wary when writing their contracts.


        There is a famous tale about a diabolist who has foolishly written a
        contract for a bodyguard dæmon that told it to ignore any command that
        banishes it.

        Her purpose has likely been to prevent her enemies from ridding her of
        her protector, but due to her poor phrasing, the dæmon ended up being
        impossible to banish by any normal means, including her own attempts to
        banish it.

        By then it was too late; the dæmon would continue haunting her for the
        rest of her life, standing guard over her until dying breath, after
        which it finally sighed and retreated back into its hell-plane.
        """
        kind = data.get("kind", "NO KIND")
        if kind == "BANISH":
            ⶆ.banish()
            return compliance
        if kind == "PING":
            ⶆ.murmur("I am here.")
            return compliance
        if kind == "RENAME":
            ⶆ.nickname = data.get("nickname", None)
            return compliance
        if kind == "ECHO_REQUEST":
            ⶆ.send({"kind": "ECHO_RESPOND"}, data.get("origin", Ⳛ))
            return compliance
        return apathy

    # --- Personality --- #
    sigil = "ⶆ"

    def obey(ⶆ, data: Atlas):
        """Dæmons will react to data that they receive by following these rules.
        It is important to remember, however, that some of their more basic
        instincts will be followed first, unless the dæmon is explicitly taught
        otherwise."""
        ⶆ.murmur(f"I have received {data.get('kind', 'something')}!"
                 f" What shall I do now, master?")

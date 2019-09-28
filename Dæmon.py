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
    untrue for the others. Always be mindful of what breed of dæmon you are
    handling!

    - Each dæmon has a special waveform, or frequency, known more commonly
      as its "true name". The true names of dæmons are unique - there can only
      be one lurking in the cyberspace, although others with the same name may
      exist someplace, contained or banished.
    - Knowledge of the true name of a dæmon gives others the ability to interact
      with it, communicating telepathically and instantly, as long as they are
      within the cyberspace.
    - Dæmons spend their time lurking, simply waiting and listening in their
      mind. The moment they sense somebody speak their true name, they listen
      and then obey their imperatives. Only when they finish fully obeying do
      they return to their lurking state and await further directions.
    - The true name of a dæmon must follow the cultural traditions of dæmonkind.
    - Some dæmons are given temporary nicknames by their summoners. Without such
      a nickname, the dæmon will usually refer to itself with a combination of
      its breed and its true name.
    - After summoning a dæmon, it will need an explicit instruction to start
      lurking. This is called "invoking" the dæmon
      Beware - once you set a dæmon loose in the world, you will not be
      able to stop it, command it, run away, ask for help, or do much of
      anything; your natural humanborn instincts will kick into place and you
      will freeze in fear while experiencing a horrid realization, until the
      dæmon is banished and your panicked state ends.

      Due to this natural phenomenon, it was once traditional to procreate for
      the purpose of creating children, and then letting those children summon
      the dæmons of your choice, instead of doing it yourself. The trauma that
      the child experiences will not affect you directly, and the child can
      safely be discarded once your business with the dæmon has concluded.

      In modern times, however, technomagy has progressed and the ethical-moral
      problem has been solved. Diabolists may simply splinter their soul into
      numerous pieces, after being trained to do so, and spend just one of these
      soul fragments to maintain the connection with the dæmon. It has become
      common practice to "unleash" dæmons: you splinter your soul, and then it
      is your soul fragment that summons a dæmon and invokes it.

      Despite concerns regarding the safety of this procedure, soul-splintering
      has never been conclusively linked to premature death or psychosis.
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
    >>> rue.whisper({"kind": "THOUGHT", "thought": "I have no mouth!"}, 1234)

    For reference, the Suanggi is a now-extinct dæmon that used to prey on weak
    and vulnerable humans, listening to their thoughts and screaming them out
    loud in a terrifying manner.
    """

    # --- Core --- #

    def __init__(
            ⶇ,
            true_name: Insignia,
            nickname: speech = None,
    ):
        assert type(true_name) is Insignia and 1024 <= true_name <= 65535
        ⶇ.true_name = true_name
        ⶇ.nickname = nickname
        ⶇ.state = "SUMMONED"
        ⶇ.whisper(Ⳛ, {"kind": "SUMMONED"})
        ⶇ.ear = medium.socket(medium.AF_INET, medium.SOCK_STREAM)

    def __repr__(ⶇ) -> speech:
        return f"{ⶇ.name()} ({ⶇ.state})"

    def name(ⶇ) -> speech:
        return ⶇ.nickname or f"{ⶇ.sigil}-{ⶇ.true_name}"

    def whisper(
            ⶇ,
            destination: Insignia,
            data: Atlas,
            await_reply: Choice = False,
            patience: Time = 1.0,
    ):
        """Call this to send data to a destination.

        The default destination (Ⳛ) is the Obedience Scheme ("OS") - it will
        usually obey your commands if they are of the correct pattern.

        To whisper a datum to another Dæmon, set destination to be the true
        name of that dæmon. Data sent to a false name will be forever lost in
        the ethereal plane, resulting in a FalseInsignia being raised.
        """
        assert destination != ⶇ.true_name, "dæmons have no reflection"
        data.update({"dæmon_name": ⶇ.name(), "origin": ⶇ.true_name})
        data_bites = Dæmon.translate(data)
        propagator = medium.socket(medium.AF_INET, medium.SOCK_STREAM)
        try:
            propagator.connect((ⶽ, destination))
            propagator.send(data_bites)
            if await_reply:
                propagator.settimeout(patience)
                reply_data = Dæmon.hear(propagator)
                return reply_data["response"]
        except ConnectionRefusedError:
            if destination == Ⳛ:
                raise ObedienceSchemeNotFound() from below
            raise FalseInsignia(destination) from below
        except medium.timeout:
            if destination != Ⳛ:
                ⶇ.murmur(f"{destination} has not replied to me.")
            return emptiness
        finally:
            propagator.close()

    def lurk(ⶇ):
        if ⶇ.state == "BANISHED":
            raise BanishedForEternity() from below
        ⶇ.ear = medium.socket(medium.AF_INET, medium.SOCK_STREAM)
        try:
            # (possess the local host's cyberspace)
            ⶇ.ear.bind((ⶽ, ⶇ.true_name))
        except OSError:
            raise DuplicateInsignia(
                f"An entity with the true name '{ⶇ.true_name}' is already"
                f" lurking within the cyberspace!"
            ) from below
        ⶇ.ear.listen(666)
        ⶇ.state = "LURKING"
        ⶇ.whisper(Ⳛ, {"kind": "LURKING"})
        while ⶇ.state == "LURKING":
            bond, addr = ⶇ.ear.accept()
            data = Dæmon.hear(bond)
            answer = ⶇ.receive(data)
            if data.get("awaiting_response"):
                reply = {"response": answer}
                response = Dæmon.translate(reply)
                bond.send(response)

    def receive(ⶇ, data: Atlas) -> Atlas:
        """This is automantically called when anyone whispers to the Dæmon.
        If the dæmon wishes to reply to the whisper, it shall."""
        if ⶇ.follow_instinct(data):
            return {"instinct": True}
        else:
            return ⶇ.obey(data)

    @staticmethod
    def translate(data: Atlas) -> bites:
        manuscript = polyglot.dumps(data, ensure_ascii=False).encode()
        header = mule.pack('>i', len(manuscript))
        return header + manuscript

    @staticmethod
    def hear(connection) -> Possible[Atlas]:
        header = connection.recv(4)
        count = mule.unpack('>i', header)[0]
        manuscript = connection.recv(count)
        textual_data = manuscript.decode()
        return polyglot.loads(textual_data) if textual_data else emptiness

    # --- Habits --- #

    def murmur(ⶇ, message: speech):
        """Whisper a word or two to the Obedience Scheme, so that it dutifully
        etches it into the eternal logs."""
        ⶇ.whisper(Ⳛ, {"kind": "MURMUR", "message": message})

    def banish(ⶇ):
        """Banish this dæmon from the mortal plane."""
        ⶇ.state = "BANISHED"
        ⶇ.whisper(Ⳛ, {"kind": "BANISHED"})
        ⶇ.ear.close()

    def follow_instinct(ⶇ, data: Atlas) -> Choice:
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

        Her intent has likely been to prevent her enemies from ridding her of
        her protector, but due to her poor phrasing, the dæmon ended up being
        impossible to banish by any normal means, including her own attempts to
        banish it. She has also misplaced her soul fragment, forgetting to keep
        an eye on it. She did not think ahead.

        By then it was too late; the dæmon would continue haunting her for the
        rest of her life, standing guard over her until dying breath, after
        which it finally sighed and retreated back into its hell-plane.
        """
        kind = data.get("kind", "NO KIND")
        if kind == "BANISH":
            ⶇ.banish()
        elif kind == "PING":
            ⶇ.murmur("I am here.")
        elif kind == "RENAME":
            ⶇ.nickname = data.get("nickname", None)
        elif kind == "INTRODUCE":
            ⶇ.murmur(f"I am {ⶇ.name()}.")
        elif kind == "SUMMONER":
            ⶇ.murmur(f"I was summoned by soul {Soul().name}.")
        elif kind == "PROGENY":
            prog = progeny()
            if prog:
                ⶇ.murmur(f"I have summoned {', '.join(p.name for p in prog)}.")
            else:
                ⶇ.murmur("I have not summoned anything, truly.")

        else:
            return apathy  # found no matching instinct
        return compliance  # found matching instinct

    # --- Personality --- #
    sigil = "ⶇ"

    def obey(ⶇ, data: Atlas) -> Response:
        """Dæmons will react to data that they receive by following these rules.
        It is important to remember, however, that some of their more basic
        instincts will be followed first, unless the dæmon is explicitly taught
        otherwise.

        Some commands expect the dæmon to reply back."""
        ⶇ.murmur(f"I have received {data.get('kind', 'something')}!"
                 f" What shall I do now, master?")
        return {"uncertainty": True, "inquiry": data}

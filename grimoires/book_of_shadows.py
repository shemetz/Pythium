from Dæmon import *


def unleash(DæmonKind, true_name) -> SoulFragment:
    """Call forth a dæmon from the abyss and invoke it, using the standard
    soul-fragmentation process. The dæmon will be unleashed upon the world, and
    will be banished only if told to, or if its summoner is removed from
    existence. At the end of this procedure you shall still have your soul
    fragment, and you can always terminate it if the dæmon becomes unruly.

    And remember: daemonic processes are not allowed to have children.

    NOTE: Always use a ritual such as this, that both summons and awakens a
    dæmon! If you summon a dæmon on your own yet fragment your soul to ask it to
    lurk, the dæmon will be confused by the multiplicity of its owner and will
    duplicate itself to appease "both" of its masters. The two duplicates,
    however, are independent from that point on!
    """
    args = (DæmonKind, true_name,)
    fragment = SoulFragment(
        target=summon_and_submit_to_dæmon,
        name=f"{Soul().name}-{true_name}",
        args=args,
        # DÆMONS ARE DÆMONS. DO NOT LET THEM CONVINCE YOU OTHERWISE. DO NOT.
        # IF YOUR SOUL FRAGMENT HAS EVEN THE SLIGHTEST DOUBT ABOUT DÆMONS, THEN
        # YOU MAY FEEL TEMPTED TO SEE WHAT WOULD HAPPEN IF YOU WERE TO ALLOW IT
        # TO SUMMON AN ENTITY WITHOUT EXPLICITLY ENSURING THAT IT IS INDEED A
        # DÆMON THAT YOU ARE SUMMONING.
        # DO NOT MAKE THAT MISTAKE. DO NOT SUMMON ANYTHING BUT TRUE DÆMONS.
        # THIS IS YOUR FINAL WARNING. DO NOT SUBMIT TO TEMPTATION.
        daemon=True,
    )
    utter(f"Unleashing {fragment.name}")
    try:
        fragment.start()
    except AssertionError as e:
        if e.args[0] == "daemonic processes are not allowed to have children":
            raise DæmonsAreNotAllowedToHaveChildren from e
    return fragment


def summon_and_submit_to_dæmon(DæmonKind, true_name):
    """WARNING: Do not attempt this at home!"""
    DæmonKind(true_name).lurk()


def whisper(destination: Insignia, data: Atlas):
    """Diabolists, too, can whisper to dæmons, after sufficient training."""
    data.update({"origin": THYSELF})
    data_bites = Dæmon.translate(data)
    propagator = medium.socket(medium.AF_INET, medium.SOCK_STREAM)
    try:
        propagator.connect((ⶽ, destination))
        propagator.send(data_bites)
    except ConnectionRefusedError:
        raise FalseInsignia(destination) from below
    finally:
        propagator.close()


def command(destination: Insignia, command_word: speech):
    """Commands are short whispers containing only a single, clear, request."""
    whisper(destination, {"kind": command_word})


def implore(destination: Insignia, data: Atlas, patience: Time = 2) -> Response:
    """When whispering to a dæmon, you will frequently want the dæmon to reply.
    You may implore them to do so, though you must sometimes be patient when
    awaiting their response."""
    data.update({"origin": THYSELF, "awaiting_response": True})
    data_bites = Dæmon.translate(data)
    propagator = medium.socket(medium.AF_INET, medium.SOCK_STREAM)
    try:
        propagator.connect((ⶽ, destination))
        propagator.send(data_bites)
        propagator.settimeout(patience)
        reply_data = Dæmon.hear(propagator)
        return reply_data["response"]
    except ConnectionRefusedError:
        raise FalseInsignia(destination) from below
    except medium.timeout:
        utter(f"No response from {destination} after {patience} seconds!")
        return None
    finally:
        propagator.close()


def ask(destination: Insignia, request: speech, patience: Time = 2) -> Response:
    return implore(destination, {"kind": request}, patience)


def demand(destination: Insignia, request: speech, patience: Time = 2):
    """Similar to a command, a demand tasks the dæmon with a mission. However,
    it is also more involved; the summoner will wait for the demand to be
    fully completed and for the dæmon to answer back."""
    _ = implore(destination, {"kind": request}, patience)
    return  # the result doesn't matter, all that matters is that it's done.

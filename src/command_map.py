import queue

from commands import hello_world, play, set_prefix, leave, queue, get_perm, skip, voteskip, set_reactions_voteskip, \
    set_timer_voteskip, showqueue, soundcloud, help, set_perm, set_permu, resume, pause


command_map = {
    "hello": hello_world.HelloWorld(),
    "play": play.Play(),
    "setprefix": set_prefix.SetPrefix(),
    "leave": leave.Leave(),
    'queue': queue.Queue(),
    'getperms': get_perm.GetPerm(),
    'skip': skip.Skip(),
    'voteskip': voteskip.VoteSkip(),
    "setreactions": set_reactions_voteskip.SetReactions(),
    "votetimer": set_timer_voteskip.SetTimer(),
    "showqueue": showqueue.ShowQueue(),
    'soundcloud': soundcloud.Soundcloud(),
    'setpermr': set_perm.SetPerm(),
    'setpermu': set_permu.SetPermu(),
    'help': help.Help(),
    'resume': resume.Resume(),
    'pause': pause.Pause()
}
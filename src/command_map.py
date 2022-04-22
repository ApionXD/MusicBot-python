import queue

<<<<<<< Updated upstream
from commands import hello_world, play, set_prefix, leave, queue, get_perm, help, set_perm, set_permu, resume, pause
=======
from commands import hello_world, play, set_prefix, leave, queue, get_perm, skip, help, set_perm, set_permu, resume, pause
>>>>>>> Stashed changes

command_map = {
    "hello": hello_world.HelloWorld(),
    "play": play.Play(),
    "setprefix": set_prefix.SetPrefix(),
    "leave": leave.Leave(),
    'queue': queue.Queue(),
    'getperms': get_perm.GetPerm(),
<<<<<<< Updated upstream
=======
    'skip': skip.Skip()
>>>>>>> Stashed changes
    'setpermr': set_perm.SetPerm(),
    'setpermu': set_permu.SetPermu(),
    'help': help.Help(),
    'resume': resume.Resume(),
    'pause': pause.Pause()
}
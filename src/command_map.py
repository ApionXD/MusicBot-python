import queue

from commands import hello_world, play, set_prefix, leave, queue, get_perm, help, set_perm, resume, pause

command_map = {
    "hello": hello_world.HelloWorld(),
    "play": play.Play(),
    "setprefix": set_prefix.SetPrefix(),
    "leave": leave.Leave(),
    'queue': queue.Queue(),
    'getperms': get_perm.GetPerm(),
    'setperm': set_perm.SetPerm(),
    'help': help.Help(),
    'resume': resume.Resume(),
    'pause': pause.Pause()
}
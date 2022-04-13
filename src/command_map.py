from commands import hello_world, play, set_prefix

command_map = {
    "hello": hello_world.HelloWorld(),
    "play": play.Play(),
    "setprefix": set_prefix.SetPrefix()
}
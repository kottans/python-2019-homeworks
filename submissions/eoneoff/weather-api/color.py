def _print_color(string, code): return f'\033[38;5;{code}m{string}\033[37m'

def y(string): return _print_color(string, 3)
def c(string): return _print_color(string, 6)
def g(string): return _print_color(string, 8)
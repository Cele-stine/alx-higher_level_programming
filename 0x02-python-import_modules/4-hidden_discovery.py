#!/usr/bin/python3
import hidden_4
if __name__ == "__main__":
    def user_defined(obj):
        return not (obj.__name__ in dir(__builtins__))
    def print_names(hidden_4):
        def_names = dir(hidden_4)
        filt_names = sorted(name for name in def_names if not name.startswith('__') and user_defined(getattr(hidden_4, name)))
        for name in filt_names:
            print(name)

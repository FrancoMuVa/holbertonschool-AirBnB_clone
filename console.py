#!/usr/bin/python3
"""
    Console program that provides a simple interactive command-line interface.
"""
import cmd


class HBNBCommand(cmd.Cmd):
    """
        HBNBCommand class represents the command-line
        interface for the program.
    """
    prompt = "(hbnb) "

    def do_quit(self, arg):
        """ Quit mathod that exit the program """
        return True

    def do_EOF(self, arg):
        """ EOF method thet exit the program """
        return True


if __name__ == "__main__":
    HBNBCommand().cmdloop()

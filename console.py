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
        """ Quit command to exit the program\n"""
        return True

    def do_EOF(self, arg):
        """ EOF command to exit the program\n"""
        return True
    
    def emptyline(self):
        pass


if __name__ == "__main__":
    HBNBCommand().cmdloop()

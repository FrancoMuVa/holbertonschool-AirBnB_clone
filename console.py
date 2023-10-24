#!/usr/bin/python3
"""
    Console program that provides a simple interactive command-line interface.
"""
import cmd
from models.base_model import BaseModel


class HBNBCommand(cmd.Cmd):
    """
        HBNBCommand class represents the command-line
        interface for the program.
    """
    prompt = "(hbnb) "
    classes = ["BaseModel", "User", "Place",
               "State", "Review", "City", "Amenity"]

    def do_quit(self, arg):
        """ Quit command to exit the program\n"""
        return True

    def do_EOF(self, arg):
        """ EOF command to exit the program\n"""
        return True

    def emptyline(self):
        pass

    def do_create(self, arg):
        if not arg:
            print("** class name missing **")
        elif arg not in self.classes:
            print("** class doesn't exist **")
        else:
            instance = eval(arg)()
            print(instance.id)
            """ save in storage """

    def do_show(self, arg):
        arg = arg.split()
        if not arg:
            print("** class name missing **")
        elif arg[0] not in self.classes:
            print("** class doesn't exist **")
        elif len(arg) == 1:
            print("** instance id missing **")
    """ else:
            search instance in storage and print,
            handle error if it doesnt exist"""

    def do_destroy(self, arg):
        if not arg:
            print("** class name missing **")
        elif arg not in self.classes:
            print("** class doesn't exist **")
        elif len(arg) == 1:
            print("** instance id missing **")
    """ else:
            search instance in storage and delete it,
            handle error if it doesnt exist and
            save change in storage"""

    def do_all(self, arg):
        arg = arg.split()
        """ if not arg:
            search in storage all instances and print them as str """
        if arg not in self.classes:
            print("** class doesn't exist **")
    """ else:
            search instances of specified class and print them as str"""

    def do_update(self, arg):
        arg = arg.split()
        if not arg:
            print("** class name missing **")
        elif arg[0] not in self.classes:
            print("** class doesn't exist **")
        elif len(arg) == 1:
            print("** instance id missing **")
        elif len(arg) == 2:
            print("** attribute name missing **")
        elif len(arg) == 3:
            print("** value missing **")
    """ search for specified instance in storage, set attributes if it exists,
    handle error if it doesnt and save in storage """


if __name__ == "__main__":
    HBNBCommand().cmdloop()

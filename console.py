#!/usr/bin/python3
"""
    Console program that provides a simple interactive command-line interface.
"""
import cmd
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models import storage


class HBNBCommand(cmd.Cmd):
    """
        HBNBCommand class represents the command-line
        interface for the program.
    """
    prompt = "(hbnb) "
    classes = {
        "BaseModel": BaseModel,
        "User": User,
        "Place": Place,
        "State": State,
        "Review": Review,
        "City": City,
        "Amenity": Amenity
        }

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
            instance = self.classes[arg]()
            instance.save()
            print(instance.id)

    def do_show(self, arg):
        arg = arg.split()
        key_obj = None
        if not arg:
            print("** class name missing **")
        elif arg[0] not in self.classes:
            print("** class doesn't exist **")
        elif len(arg) == 1:
            print("** instance id missing **")
        else:
            for key, value in storage.all().items():
                key_obj = key.split(".")
                if key_obj[0] == arg[0] and key_obj[1] == arg[1]:
                    print(value)
                    break
            if key_obj is None or (key_obj[0] != arg[0]
                                   and key_obj[1] != arg[1]):
                print("** no instance found **")

    def do_destroy(self, arg):
        arg = arg.split()
        if not arg:
            print("** class name missing **")
        elif arg[0] not in self.classes:
            print("** class doesn't exist **")
        elif len(arg) == 1:
            print("** instance id missing **")
        else:
            a = arg[0] + "." + arg[1]
            if a in storage.all():
                storage.all().pop(a)
                storage.save()
            else:
                print("** no instance found **")

    def do_all(self, arg):
        if not arg:
            mylist = []
            for key, value in storage.all().items():
                mylist.append(value.__str__())
            print(mylist)
        else:
            mylist = []
            for key, value in storage.all().items():
                a = key.split(".")
                if a[0] == arg:
                    mylist.append(value.__str__())
            if mylist == []:
                print("** class doesn't exist **")
                return
            else:
                print(mylist)

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
        else:
            a = arg[0] + "." + arg[1]
            if a not in storage.all():
                print("** no instance found **")
            else:
                instance = storage.all()[a]
                setattr(instance, arg[2], arg[3].strip('"\''))
                instance.save()


if __name__ == "__main__":
    HBNBCommand().cmdloop()

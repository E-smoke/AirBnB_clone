#!/bin/python3
"""HBNB console"""

import cmd
import datetime
import copy
from models.base_model import BaseModel
from models import storage


class HBNBCommand(cmd.Cmd):
    """console class"""
    BaseModel_Subcls = {"BaseModel": BaseModel}
    prompt = "(hbnb)"

    def do_quit(self, arg):
        """use to quit the console"""
        return True

    def do_EOF(self, arg):
        """handles ctrl+D or EOF"""
        return True

    def emptyline(self):
        """Do nothing when an empty line is entered"""
        pass

    def do_create(self, cls):
        """create an obj of cls"""
        if not cls:
            print("** class name missing **")
        elif cls not in self.BaseModel_Subcls:
            print("** class doesn't exist **")
        else:
            cls = self.BaseModel_Subcls[cls]
            obj = cls()
            storage.save()
            print(obj.id)

    def do_show(self, line):
        """Prints the string representation of an
        instance based on the class name and id"""
        args = line.split()
        if len(args) < 1:
            print("** class name missing **")
        elif args[0] not in self.BaseModel_Subcls:
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        elif args[0] + "." + args[1] not in storage.all():
            print("** no instance found **")
        else:
            key = args[0] + "." + args[1]
            d = copy.deepcopy(storage.all()[key])
            d["created_at"] = datetime.datetime.fromisoformat(d["created_at"])
            d["updated_at"] = datetime.datetime.fromisoformat(d["updated_at"])
            cls = self.BaseModel_Subcls[args[0]]
            obj = cls(d)
            print(obj)

    def do_destroy(self, line):
        """deletes an instance"""
        args = line.split()
        if len(args) < 1:
            print("** class name missing **")
        elif args[0] not in self.BaseModel_Subcls:
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        elif args[0] + "." + args[1] not in storage.all():
            print("** no instance found **")
        else:
            key = args[0] + "." + args[1]
            d = storage.all()
            del d[key]
            storage.save()


if __name__ == "__main__":
    HBNBCommand().cmdloop()

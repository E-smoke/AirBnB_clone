#!/bin/python3
"""HBNB console"""

import cmd
import datetime
import copy
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models import storage


class HBNBCommand(cmd.Cmd):
    """console class"""
    BaseModel_Subcls = {
            "BaseModel": BaseModel,
            "User": User,
            "State": State,
            "City": City,
            "Amenity": Amenity,
            "Place": Place,
            "Review": Review
            }
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
            cls = self.BaseModel_Subcls[args[0]]
            obj = cls(**d)
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

    def do_all(self, line):
        """ Prints all string representation of all instances
        based or not on the class name. Ex: $all BaseModel or $ all."""
        list_cls = []
        if line:
            if line not in self.BaseModel_Subcls:
                print("** class doesn't exist **")
            else:
                cls = self.BaseModel_Subcls[line]
                d = copy.deepcopy(storage.all())
                for key in d:
                    cls_cmp = d[key]["__class__"]
                    cls_cmp = self.BaseModel_Subcls[cls_cmp]
                    if issubclass(cls_cmp, cls):
                        obj = cls_cmp(**d[key])
                        string = str(obj)
                        list_cls.append(string)
        else:
            d = copy.deepcopy(storage.all())
            for key in d:
                cls = d[key]["__class__"]
                cls = self.BaseModel_Subcls[cls]
                obj = cls(**d[key])
                string = str(obj)
                list_cls.append(string)
        print(list_cls)

    def do_update(self, line):
        """ Updates an instance based on the class name
            and id by adding or updating attribute
            (save the change into the JSON file).
            Ex: $ update BaseModel 1234-1234-1234 email 'aibnb@mail.com'.
            Usage:update <class name> <id> <attribute name> '<attribute value>'
            """
        args = line.split()
        if len(args) < 1:
            print("** class name missing **")
        elif args[0] not in self.BaseModel_Subcls:
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        elif args[0] + "." + args[1] not in storage.all():
            print("** no instance found **")
        elif len(args) < 3:
            print("** attribute name missing **")
        elif len(args) < 4:
            key = args[0] + "." + args[1]
            d = storage.all()[key]
            value = eval(args[2])
            d.update(value)
        else:
            key = args[0] + "." + args[1]
            d = storage.all()[key]
            cls = self.BaseModel_Subcls[args[0]]
            value = eval(args[3])
            d[args[2]] = value
            obj = cls(**copy.deepcopy(d))
            obj.save()

    def default(self, line):
        cls, rest = line.split('.')
        funct, rest = rest.split('(')
        rest = rest.replace(',', '')
        rest = rest.replace(')', '')
        args = cls
        if rest:
            args = cls + ' ' + rest
        funct = 'do_' + funct
        funct = getattr(self, funct)
        funct(args)

    def do_count(self, line):
        count = 0
        d = copy.deepcopy(storage.all())
        for key in d:
            if d[key]["__class__"] == line:
                count += 1
        print(count)


if __name__ == "__main__":
    HBNBCommand().cmdloop()

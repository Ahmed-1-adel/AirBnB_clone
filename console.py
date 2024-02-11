#!/usr/bin/python3
""" Command Interpreter Module """

import cmd
import shlex
import models
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review

class HBNBCommand(cmd.Cmd):
    """Command interpreter class

    Attributes:
        prompt (str): The command prompt.
    """
    prompt = "(hbnb) "  
    __classes = {
        "BaseModel",
        "User",
        "State",
        "City",
        "Place",
        "Amenity",
        "Review"
    }
    def do_quit(self, line):
        """Quit command to exit the program"""
        return True
    
    def do_EOF(self, line):
        """Handles End of File"""
        print()
        return True

    def emptyline(self):
        """Called when an empty line is entered"""
        pass
    
    def do_create(self, line):
        """Creates a new instance of BaseModel"""
        args = shlex.split(line)
        if not args:
            print("** class name missing **")
            return
        try:
            new_instance = eval(args[0])()
            new_instance.save()
            print(new_instance.id)
        except Exception:
            print("** class doesn't exist **")

    def do_show(self, line):
        """Prints the string representation of an instance"""
        args = shlex.split(line)
        if not args:
            print("** class name missing **")
            return
        try:
            if args[0] not in models.classes:
                print("** class doesn't exist **")
                return
            if len(args) < 2:
                print("** instance id missing **")
                return
            key = args[0] + "." + args[1]
            obj = models.storage.all()
            if key not in obj:
                print("** no instance found **")
                return
            print(obj[key])
        except Exception:
            print("** class doesn't exist **")

    def do_destroy(self, line):
        """Deletes an instance based on the class name and id"""
        args = shlex.split(line)
        if not args:
            print("** class name missing **")
            return
        try:
            if args[0] not in models.classes:
                print("** class doesn't exist **")
                return
            if len(args) < 2:
                print("** instance id missing **")
                return
            key = args[0] + "." + args[1]
            obj = models.storage.all()
            if key not in obj:
                print("** no instance found **")
                return
            del obj[key]
            models.storage.save()
        except Exception:
            print("** class doesn't exist **")

    def do_all(self, line):
        """Prints all string representation of all instances"""
        args = shlex.split(line)
        obj = models.storage.all()
        if not args:
            print([str(obj[k]) for k in obj])
            return
        try:
            if args[0] not in models.classes:
                print("** class doesn't exist **")
                return
            print([str(obj[k]) for k in obj if args[0] in k])
        except Exception:
            print("** class doesn't exist **")

    def do_update(self, line):
        """Updates an instance based on the class name and id"""
        args = shlex.split(line)
        if not args:
            print("** class name missing **")
            return
        try:
            if args[0] not in models.classes:
                print("** class doesn't exist **")
                return
            if len(args) < 2:
                print("** instance id missing **")
                return
            key = args[0] + "." + args[1]
            obj = models.storage.all()
            if key not in obj:
                print("** no instance found **")
                return
            if len(args) < 3:
                print("** attribute name missing **")
                return
            if len(args) < 4:
                print("** value missing **")
                return
            setattr(obj[key], args[2], args[3].replace('"', ''))
            obj[key].save()
        except Exception as e:
            print(e.__doc__)

if __name__ == "__main__":
    HBNBCommand().cmdloop()
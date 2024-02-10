#!/usr/bin/python3
""" Command Interpreter Module """

import cmd
import shlex
import models


class HBNBCommand(cmd.Cmd):
    """Command interpreter class"""

    prompt = "(hbnb) "

    def do_quit(self, arg):
        """Quit Command to exit the program."""
        return True
    
    def do_EOF(self, arg):
        """EOF signal to exit the program."""
        print("")
        return True

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


if __name__ == "__main__":
    HBNBCommand().cmdloop()



import cmd
from models.user import User
from models.engine.file_storage import FileStorage

class HBNBCommand(cmd.Cmd):
    """Simple command processor example."""
    prompt = '(hbnb) '

    def do_create(self, arg):
        """Create a new instance of a BaseModel"""
        if arg:
            args = arg.split()
            if args[0] == 'User':
                new_user = User()
                for a in args[1:]:
                    key, value = a.split('=')
                    setattr(new_user, key, value)
                new_user.save()
                print(new_user.id)
            else:
                print("** class doesn't exist **")
        else:
            print("** class name missing **")

    def do_show(self, arg):
        """Prints the string representation of an instance"""
        if arg:
            args = arg.split()
            if args[0] == 'User':
                if len(args) < 2:
                    print("** instance id missing **")
                    return
                key = "{}.{}".format(args[0], args[1])
                objects = FileStorage().all()
                if key in objects:
                    print(objects[key])
                else:
                    print("** no instance found **")
            else:
                print("** class doesn't exist **")
        else:
            print("** class name missing **")

    def do_destroy(self, arg):
        """Deletes an instance"""
        if arg:
            args = arg.split()
            if args[0] == 'User':
                if len(args) < 2:
                    print("** instance id missing **")
                    return
                key = "{}.{}".format(args[0], args[1])
                objects = FileStorage().all()
                if key in objects:
                    del objects[key]
                    FileStorage().save()
                else:
                    print("** no instance found **")
            else:
                print("** class doesn't exist **")
        else:
            print("** class name missing **")

    def do_update(self, arg):
        """Updates an instance"""
        if arg:
            args = arg.split()
            if args[0] == 'User':
                if len(args) < 2:
                    print("** instance id missing **")
                    return
                key = "{}.{}".format(args[0], args[1])
                objects = FileStorage().all()
                if key in objects:
                    if len(args) < 3:
                        print("** attribute name missing **")
                        return
                    if len(args) < 4:
                        print("** value missing **")
                        return
                    setattr(objects[key], args[2], args[3])
                    objects[key].save()
                else:
                    print("** no instance found **")
            else:
                print("** class doesn't exist **")
        else:
            print("** class name missing **")

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, line):
        """End of File"""
        return True

if __name__ == '__main__':
    HBNBCommand().cmdloop()

#!/usr/bin/python3
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

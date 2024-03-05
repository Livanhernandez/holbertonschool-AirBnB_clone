#!/usr/bin/python3
"""Entry point of the commamd interpreter"""

import cmd
import json

from models import FileStorage, storage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review


class HBNBCommand(cmd.Cmd):
    """Command Interpreter class"""

    prompt = "(hbnb) "

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, arg):
        """EOF command to exit the program"""
        print()
        return True

    def emptyline(self):
        """Do nothing on empty line"""
        pass

    def do_create(self, arg):
        """Create a new instance of BaseModel"""
        if not arg:
            print('** class name missing **')
            return
        try:
            new_obj = eval(arg)()
            new_obj.save()
            print(new_obj.id)
        except Exception:
            print('** class doesn\'t exist **')

    def do_show(self, arg):
        """Prints the string representation of an
        instance based on the class name and id"""
        if not arg:
            print("** class name missing **")
            return
        list_arg = arg.split()
        try:
            class_name = eval(list_arg[0]).__name__
        except Exception:
            print("** class doesn't exist **")
            return
        if len(list_arg) == 1:
            print("** instance id missing **")
            return
        try:
            class_name = f"{list_arg[0]}.{list_arg[1]}"
            print(storage.all()[class_name])
        except Exception:
            print("** no instance found **")

    def do_destroy(self, arg):
        """Deletes an instance based on the class name and id"""
        if not arg:
            print("** class name missing **")
            return
        list_arg = arg.split()
        try:
            class_name = eval(list_arg[0]).__name__
        except Exception:
            print("** class doesn't exist **")
            return
        if len(list_arg) == 1:
            print("** instance id missing **")
            return
        try:
            class_name = f"{list_arg[0]}.{list_arg[1]}"
            object = storage.all().get(class_name)
            del (object)
            storage.save()
        except Exception:
            print("** class doesn't exist **")

    def do_all(self, arg):
        """
        Prints all string representation of all
        instances based or not on the class name.
        """
        if arg:
            try:
                arg == eval(arg).__name__
            except Exception:
                print("** class doesn't exist **")
                return
        if not arg:
            all_object_list = []
            for obj in storage.all().values():
                all_object_list.append(str(obj))
        else:
            all_object_list = []
            for obj in storage.all().values():
                if arg == obj.__class__.__name__:
                    all_object_list.append(str(obj))
        print(all_object_list)

    def do_update(self, arg):
        """
        update the object insatance by adding a
        new atribute and saving it to json
        """
        if not arg:
            print("** class name missing **")
            return
        arguments = arg.split()
        if arg:
            try:
                arguments[0] == eval(arguments[0]).__name__
            except Exception:
                print("** class doesn't exist **")
                return
        if len(arguments) == 0:
            print("** instance id missing **")
            return
        try:
            class_name = f"{arguments[0]}.{arguments[1]}"
            obj_instance = storage.all()[class_name]
        except Exception:
            print("** no instance found **")
            return
        if len(arguments) == 1:
            print("** attribute name missing **")
            return
        if len(arguments) == 2:
            print("** value missing **")
            return
        else:
            new_atribute = {str(arguments[2]): arguments[3]}
            obj_instance.__dict__.update(new_atribute)
            obj_instance.save()
            return


if __name__ == '__main__':
    HBNBCommand().cmdloop()
#!/usr/bin/python3
"""Defines the HBnB console"""
import cmd
import json
from models import storage
from models.base_model import BaseModel

class HBNBCommand(cmd.Cmd):
    """HBnB command interpreter."""

    prompt = '(hbnb) '

    # ... previous commands (quit, EOF, emptyline) ...

    def do_create(self, arg):
        """Creates a new instance of a model."""
        args = arg.split()
        if not args:
            print("** class name missing **")
            return

        class_name = args[0]
        try:
            model_class = getattr(models, class_name)
            new_instance = model_class()
            storage.save()  # Save all instances for persistence
            print(new_instance.id)
        except AttributeError:
            print(f"** class doesn't exist **: {class_name}")

    def do_show(self, arg):
        """Shows an instance based on class name and id."""
        args = arg.split()
        if not args:
            print("** class name missing **")
            return

        class_name = args[0]
        try:
            model_class = getattr(models, class_name)
            if len(args) < 2:
                print("** instance id missing **")
                return

            obj_id = args[1]
            instance = storage.get(model_class, obj_id)
            if instance:
                print(instance)
            else:
                print(f"** no instance found **: {class_name} {obj_id}")
        except AttributeError:
            print(f"** class doesn't exist **: {class_name}")

    def do_destroy(self, arg):
        """Destroys an instance based on class name and id."""
        args = arg.split()
        if not args:
            print("** class name missing **")
            return

        class_name = args[0]
        try:
            model_class = getattr(models, class_name)
            if len(args) < 2:
                print("** instance id missing **")
                return

            obj_id = args[1]
            instance = storage.get(model_class, obj_id)
            if instance:
                storage.delete(instance)
                storage.save()  # Save changes
            else:
                print(f"** no instance found **: {class_name} {obj_id}")
        except AttributeError:
            print(f"** class doesn't exist **: {class_name}")

    def do_all(self, arg):
        """Shows all instances of a class or all classes."""
        args = arg.split()
        if args:
            class_name = args[0]
            try:
                model_class = getattr(models, class_name)
                instances = storage.all(model_class)
            except AttributeError:
                print(f"** class doesn't exist **: {class_name}")
                return
        else:
            instances = storage.all()

        for instance in instances:
            print(instance)

    def do_update(self, arg):
        """Updates an instance based on class name, id, and attribute."""
        args = arg.split()
        if not args:
            print("** class name missing **")
            return

        class_name = args[0]
        try:
            model_class = getattr(models, class_name)
            if len(args) < 3:
                print("** instance id missing **")
                return

            obj_id = args[1]
            instance = storage.get(model_class, obj_id)
            if not instance:
                print(f"** no instance found **: {class_name} {obj_id}")
                return

            if len(args) < 4:
                print("** attribute name missing **")
                return

            attribute_name = args[2]
            value = args[3] if len(args) == 4 else None
            if not value:
                print("** value missing **")
                return

            setattr(instance, attribute_name, value)

#!/usr/bin/python3
"""Defines the HBnB console"""
import cmd

class HBNBCommand(cmd.Cmd):
    """HBnB command interpreter."""

    prompt = '(hbnb) '

    def do_quit(self, arg):
        """Quit the command interpreter."""
        return True

    def do_EOF(self, arg):
        """Exit on end-of-file."""
        return True

    # Override empty line behavior to do nothing
    def emptyline(self):
        """Do nothing on empty input lines."""
        pass

if __name__ == '__main__':
    HBNBCommand().cmdloop()

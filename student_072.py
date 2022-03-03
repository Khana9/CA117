#!/usr/bin/env python3

class Student():
    def __init__(self, sid, name, modlist=None):
        self.sid = sid
        self.name = name
        self.modlist = [] if modlist is None else modlist

    def add_module(self, mod):
        self.modlist.append(mod)

    def del_module(self, mod):
        self.modlist.remove(mod)

    def __str__(self):
        s = []
        s.append(f'ID: {self.sid}')
        s.append(f'Name: {self.name}')
        s.append(f'Modules: {", ".join(self.modlist)}')
        return "\n".join(s)

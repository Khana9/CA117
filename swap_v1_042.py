#!/usr/bin/env python3

def swap_keys_values(s):
    new_dict = dict([(value, key) for key, value in s.items()])
    return new_dict

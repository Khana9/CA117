#!/usr/bin/env python3

def swap_unique_keys_values(s):
    result = {}
    for key, value in s.items():
        duplicates = []
        if value not in result and value not in duplicates:
            result[value] = key
            duplicates.append(value)
        else:
            del result[value]
    return result

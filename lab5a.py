#!/usr/bin/env python3
# Author ID: skarki28

def read_file_string(file_name):
    try:
        with open(file_name, 'r') as f:
            return f.read()
    except FileNotFoundError:
        return 'Error: File not found'

def read_file_list(file_name):
    try:
        with open(file_name, 'r') as f:
            return f.read().splitlines()
    except FileNotFoundError:
        return ['Error: File not found']

if __name__ == '__main__':
    file_name = 'data.txt'
    print(read_file_string(file_name))
    print(read_file_list(file_name))


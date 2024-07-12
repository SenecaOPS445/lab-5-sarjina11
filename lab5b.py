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

def append_file_string(file_name, string_of_lines):
    try:
        with open(file_name, 'a') as f:
            f.write(string_of_lines)
    except FileNotFoundError:
        print('Error: File not found')

def write_file_list(file_name, list_of_lines):
    try:
        with open(file_name, 'w') as f:
            for line in list_of_lines:
                f.write(line + '\n')
    except FileNotFoundError:
        print('Error: File not found')

def copy_file_add_line_numbers(file_name_read, file_name_write):
    try:
        with open(file_name_read, 'r') as f_read, open(file_name_write, 'w') as f_write:
            lines = f_read.readlines()
            for i, line in enumerate(lines):
                f_write.write(f"{i+1}:{line}")
    except FileNotFoundError:
        print('Error: File not found')

if __name__ == '__main__':
    file1 = 'seneca1.txt'
    file2 = 'seneca2.txt'
    file3 = 'seneca3.txt'
    string1 = 'First Line\nSecond Line\nThird Line\n'
    list1 = ['Line 1\n', 'Line 2\n', 'Line 3\n']

    append_file_string(file1, string1)
    print(read_file_string(file1))

    write_file_list(file2, list1)
    print(read_file_string(file2))

    copy_file_add_line_numbers(file2, file3)
    print(read_file_string(file3))


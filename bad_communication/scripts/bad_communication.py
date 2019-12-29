#!/bin/usr/env python3
# -*- coding: utf-8 -*-
from os import system, path, makedirs

def format2double_space(data):
    formatted_data = ''
    double_space = ' '*2
    counter = 0

    for data_n in data:
        for string in data_n:
            if '\n' in string or ' ' in string or len(string) < 1:
                if ' ' in string or len(string) < 1:
                    pass
                formatted_data += string
            else:
                formatted_data += string+double_space
                counter += 1

    formatted_data += '\n\n[{}]'.format(counter)

    return formatted_data

def import_files(filename):
    output = []
    with open(filename, 'r') as input_file:
        file_data = input_file.readlines()
        for data in file_data:
            output.append(data.split(' '))
        print(output)
        output = format2double_space(output)
        print(output)
        _filename = ''
        for i in filename:
            _filename += i
            if i == '/':
                _filename = ''

        return output, _filename

if __name__ == '__main__':
    file_path = input('input file to format: ')
    data, filename = import_files(file_path)
    path.abspath('./')
    makedirs('outputs', exist_ok=True)
    with open(f'outputs/{filename}', 'w') as output_file:
        output_file.write(data)

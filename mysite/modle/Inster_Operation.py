#!/usr/bin/env python
# -*- coding:utf-8 -*-

def insert_operation(char_join,file_name):
    fp = file(file_name)
    lines = []
    for line in fp:
        lines.append(line.strip('\n'))
    fp.close()
    lines.insert(-1,char_join)
    s = '\n'.join(lines)
    fp = file(file_name, 'w')
    fp.write(s)
    fp.close()
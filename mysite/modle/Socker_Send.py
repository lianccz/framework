#!/usr/bin/env python
# -*- coding:utf-8 -*-
import socket
import os
import sys
import struct
def socket_client(distributed,file_path):
    if distributed == "y":
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect(('118.31.184.85',8448))
        except socket.error:
            sys.exit(1)
        while True:
            if os.path.isfile(file_path):
                fileinfo_size = struct.calcsize('128sl')
                # 定义文件头信息，包含文件名和文件大小
                fhead = struct.pack('128sl', os.path.basename(file_path),os.stat(file_path).st_size)
                s.send(fhead)
                fp = open(file_path, 'rb')
                while 1:
                    data = fp.read(1024)
                    if not data:
                        break
                    s.send(data)
            s.close()
            break
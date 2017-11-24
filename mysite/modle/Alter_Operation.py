#!/usr/bin/env python
# -*- coding:utf-8 -*-
def alter_content(request_dict,file_name):
    with open(file_name,'r') as f:
        lines = f.readlines()
    with open(file_name, 'w') as f_w:
        for line in lines:
            if str(request_dict["SerAreaUid"]) in line:
                new_str = '    <SerAreaData SerAreaUid="%s" SerAreaGroupName="%s" SerAreaFormName="%s" SerAreaUpName="%s" SerAreaIp="%s" SerAreaPort="%s" SerAreaPriority="%s"/>\n' \
                      %(request_dict["SerAreaUid"],request_dict["SerAreaGroupName"],request_dict["SerAreaFormName"],request_dict["SerAreaFormName"],request_dict["SerAreaIp"],request_dict["SerAreaPort"],request_dict["SerAreaPriority"])
                line = line.replace(line,new_str)
            f_w.write(line)
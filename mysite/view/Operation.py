#!/usr/bin/env python
# -*- coding:utf-8 -*-

import xml.etree.ElementTree as ET
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from mysite.modle.Add_Form import Add_Form
from mysite.modle.Alter_Form import Alter_Form, Select_Form
from mysite.modle.Paging_Show import paging_info
from mysite.modle.Alter_Operation import alter_content
from mysite.modle.Inster_Operation import insert_operation
from mysite.modle.Socker_Send import socket_client
from account.decorators import login_exempt
import json
import sys
reload(sys)
sys.setdefaultencoding('utf8')

Android_name = "/data/xml_file/SerAreaConfig_Android.xml"
IOS_name = "/data/xml_file/SerAreaConfig_IOS.xml"
test_name = "/data/xml_file/SerAreaConfig_test.xml"
# 获取xml所有值

@csrf_exempt
def show_all_content(request):
    a = []
    baseurl = '/t/serverlist/yqzj/index/?p1='
    global file_name
    if request.method == 'POST':
        request_form = Select_Form(request.POST)
        if request_form.is_valid():
            request_dict = request_form.clean()
            if request_dict['Server_type'] == 1:
                file_name = Android_name
            elif request_dict['Server_type'] == 2:
                file_name = IOS_name
            elif request_dict['Server_type'] == 3:
                file_name = test_name
    else:
        request_form = Select_Form()
    try:
        tree = ET.parse(file_name)
    except NameError,e:
        file_name = Android_name
        tree = ET.parse(file_name)
    show_num = int(request.GET.get('p1', 1))
    distributed = request.GET.get('distributed', 'n')
    socket_client(distributed,file_name)
    root = tree.getroot()
    for i in root:
        a.append(i.attrib)
    content_num = len(a)
    total = divmod(content_num, 10)
    if total[1] == 0:
        totalpage = total[0]
    else:
        totalpage = total[0] + 1
    result = paging_info(baseurl, show_num, totalpage)
    b = a[(show_num - 1) * 10:(show_num) * 10]
    return render_to_response('html/show_paging.html',
                              {'data': b, 'result': result, 'show_num': show_num, 'form': request_form})

def add_operation(request):
    ret = {'status': False, 'data': '', 'error': ''}
    server_stat = {1: '新服', 2: '推荐', 3: '爆满'}
    if request.method == 'POST':
        request_form = Add_Form(request.POST)
        if request_form.is_valid():
            request_dict = request_form.clean()
            ret['status'] = True
            char_join = '    <SerAreaData SerAreaUid="%s" SerAreaGroupName="%s" SerAreaFormName="%s(%s)" SerAreaUpName="%s(%s)" SerAreaIp="%s" SerAreaPort="%s" SerAreaPriority="%s"/>' \
                        % (
                        request_dict["SerAreaUid"], request_dict["SerAreaGroupName"], request_dict["SerAreaFormName"],
                        server_stat[request_dict["Server_type"]], request_dict["SerAreaFormName"],
                        server_stat[request_dict["Server_type"]], request_dict["SerAreaIp"],
                        request_dict["SerAreaPort"], request_dict["SerAreaPriority"])
            insert_operation(char_join,file_name)
            return HttpResponseRedirect('/t/serverlist/yqzj/index')
        else:
            error_msg = request_form.errors.as_json()
            ret['error'] = json.loads(error_msg)
            return render_to_response('html/add_content.html', {'form': request_form}, ret)
    else:
        request_form = Add_Form()
        return render_to_response('html/add_content.html', {'form': request_form})

def add_show(request):
    SerAreaUid = request.GET.get('SerAreaUid', "-001")
    tree = ET.parse(file_name)
    root = tree.getroot()
    for i in root.findall('SerAreaData'):
        rank = i.get("SerAreaUid")
        if rank == SerAreaUid:
            SerAreaGroupName = i.get('SerAreaGroupName')
            SerAreaFormName = i.get('SerAreaFormName')
            SerAreaIp = i.get('SerAreaIp')
            SerAreaPort = i.get('SerAreaPort')
            SerAreaPriority = i.get('SerAreaPriority')
            print SerAreaGroupName
            print SerAreaFormName
            print SerAreaIp
            print SerAreaPort
            print SerAreaPriority

def del_operation(request):
    get_uid = int(request.GET.get('uid', "-001"))
    page = int(request.GET.get('page', 1))
    with open(file_name, 'r') as f:
        lines = f.readlines()
    with open(file_name, 'w') as f_w:
        for line in lines:
            if str(get_uid) in line:
                continue
            f_w.write(line)
    return HttpResponseRedirect('/t/serverlist/yqzj/index/?p1=%s' % page)

def alter_operation(request):
    ret = {'status': False, 'data': '', 'error': ''}
    get_all_dict = {}
    SerAreaUid = request.GET.get('SerAreaUid', "-001")
    page = int(request.GET.get('page', 1))
    get_all_dict['SerAreaUid'] = SerAreaUid
    tree = ET.parse(file_name)
    root = tree.getroot()
    for i in root.findall('SerAreaData'):
        rank = i.get("SerAreaUid")
        if rank == SerAreaUid:
            get_all_dict['SerAreaGroupName'] = i.get('SerAreaGroupName')
            get_all_dict['SerAreaFormName'] = i.get('SerAreaFormName')
            get_all_dict['SerAreaIp'] = i.get('SerAreaIp')
            get_all_dict['SerAreaPort'] = i.get('SerAreaPort')
            get_all_dict['SerAreaPriority'] = i.get('SerAreaPriority')

    if request.method == 'POST':
        request_form = Alter_Form(request.POST)
        if request_form.is_valid():
            request_dict = request_form.clean()
            ret['status'] = True
            alter_content(request_dict,file_name)
            return HttpResponseRedirect('/t/serverlist/yqzj/index?p1=%s' % page)
        else:
            error_msg = request_form.errors.as_json()
            ret['error'] = json.loads(error_msg)
            return render_to_response('html/alter_content.html', {'form': request_form}, ret, get_all_dict)
    else:
        request_form = Alter_Form()
        return render_to_response('html/alter_content.html', {'form': request_form, 'get_all_dict': get_all_dict})


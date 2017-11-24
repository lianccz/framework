#!/usr/bin/env python
# -*- coding:utf-8 -*-
from django import forms
from django.forms import widgets
class Add_Form(forms.Form):
    Server_type_all = (
        (1,u'新服'),
        (2,u'推荐'),
        (3,u'火爆'),
    )
    SerAreaUid = forms.IntegerField(widget=widgets.NumberInput(attrs={"style":"width:220px;"}),error_messages={'required': u'id不能为空',
                                          'invalid': '必须输入数字'})
    SerAreaGroupName = forms.CharField(widget=widgets.TextInput(attrs={"style":"width:220px;"}),error_messages={'required': u'SerAreaGroupName不能为空'})
    SerAreaFormName = forms.CharField(widget=widgets.TextInput(attrs={"style":"width:220px;"}),error_messages={'required': u'SerAreaFormName不能为空'})
    Server_type = forms.IntegerField(widget=forms.widgets.Select(attrs={"style":"width:100px;"},choices=Server_type_all))
    SerAreaIp = forms.CharField(widget=widgets.TextInput(attrs={"style":"width:220px;"}),error_messages={'required': u'SerAreaIp不能为空'})
    SerAreaPort = forms.IntegerField(widget=widgets.NumberInput(attrs={"style":"width:220px;"}),error_messages={'required': u'SerAreaPort不能为空',
                                                     'invalid': '必须输入数字'})
    SerAreaPriority = forms.IntegerField(widget=widgets.NumberInput(attrs={"style":"width:220px;"}),error_messages={'required': u'SerAreaPriority不能为空',
                                                         'invalid': '必须输入数字'})
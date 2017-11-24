#!/usr/bin/env python
# -*- coding:utf-8 -*-
import re
from django import forms
from django.forms import widgets
class Alter_Form(forms.Form):
    SerAreaUid = forms.IntegerField(widget=widgets.NumberInput(attrs={"style":"width:220px;","readonly":"readonly",'placeholder':'{{get_all_dict.SerAreaUid}}'}),error_messages={'required': u'id不能为空',
                                          'invalid': '必须输入数字'})
    SerAreaGroupName = forms.CharField(widget=widgets.TextInput(attrs={"style":"width:220px;","placeholder":"{{get_all_dict.SerAreaGroupName}}"}),error_messages={'required': u'SerAreaGroupName不能为空'})
    SerAreaFormName = forms.CharField(widget=widgets.TextInput(attrs={"style":"width:220px;","placeholder":"{{get_all_dict.SerAreaFormName}}"}),error_messages={'required': u'SerAreaFormName不能为空'})
    SerAreaIp = forms.CharField(widget=widgets.TextInput(attrs={"style":"width:220px;","placeholder":"{{get_all_dict.SerAreaIp}}"}),error_messages={'required': u'SerAreaIp不能为空'})
    SerAreaPort = forms.IntegerField(widget=widgets.NumberInput(attrs={"style":"width:220px;","placeholder":"{{get_all_dict.SerAreaPort}}"}),error_messages={'required': u'SerAreaPort不能为空',
                                                     'invalid': '必须输入数字'})
    SerAreaPriority = forms.IntegerField(widget=widgets.NumberInput(attrs={"style":"width:220px;","placeholder":"{{get_all_dict.SerAreaPriority}}"}),error_messages={'required': u'SerAreaPriority不能为空',
                                                         'invalid': '必须输入数字'})

class Select_Form(forms.Form):
    file_type_all = (
        (1, u'Android'),
        (2, u'IOS'),
        (3, u'测试'),
    )
    Server_type = forms.IntegerField(
        widget=forms.widgets.Select(attrs={"style": "width:100px;"}, choices=file_type_all))
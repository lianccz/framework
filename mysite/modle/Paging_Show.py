#!/usr/bin/env python
# -*- coding:utf-8 -*-

from django.utils.safestring import mark_safe

def paging_info(baseurl,currentpage,totalpage):
    initial_page = 11
    if totalpage <= initial_page:
        begin = 0
        end = totalpage
    else:
        if currentpage > initial_page/2:
            begin = currentpage - initial_page/2
            end = currentpage + initial_page/2
            if end > totalpage:
                end = totalpage
        else:
            begin = 0
            end = totalpage

    paging_list = []
    if currentpage <= 1:
        paging_first = '<a href="" class="page-button">首页</a>'
    else:
        paging_first = '<a href="%s%d" class="page-button">首页</a>' %(baseurl,1)
    paging_first = mark_safe(paging_first)
    paging_list.append(paging_first)

    for i in range(begin+1,end+1):
        if i == currentpage:
            paging_all = '<a href="%s%d" class="page-button" style="color:#1E90FF">%d</a>' % (baseurl,i,i)
        else:
            paging_all = '<a href="%s%d" class="page-button">%d</a>' % (baseurl,i,i)
        paging_all = mark_safe(paging_all)
        paging_list.append(paging_all)

    if currentpage >= totalpage:
        paging_end = '<a href="" class="page-button">尾页</a>'
    else:
        paging_end = '<a href="%s%d" class="page-button">尾页</a>' %(baseurl,totalpage)
    paging_end = mark_safe(paging_end)
    paging_list.append(paging_end)
    return paging_list










# -*- coding: utf-8 -*-

from common.mymako import render_mako_context


def demo(request):
    """
    首页
    """
    return render_mako_context(request, '/demo/demo.html')


def demo1(request):
    """
    开发指引
    """
    return render_mako_context(request, '/demo/demo1.html')

#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Views for Bookmarks app"""

from django.http import HttpResponse


def index(request):
    """Show the main page of Bookmarks"""
    if request.user.is_authenticated():
        pass

    return HttpResponse('It works!')

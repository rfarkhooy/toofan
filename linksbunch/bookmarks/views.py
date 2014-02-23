#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Views for Bookmarks app"""

from django.http import HttpResponse
from django.shortcuts import render_to_response


def index(request):
    """Show the main page of Bookmarks"""
    if request.user.is_authenticated():
        pass

    return render_to_response('bookmarks/index.html')

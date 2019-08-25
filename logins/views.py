# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.


def home(request):
    """
    :returns HTML home page
    :param request:
    """
    return render(request, 'login.html')


def login_user(request):
    """

    :param request:
    :return: JWT Authentication token
    """
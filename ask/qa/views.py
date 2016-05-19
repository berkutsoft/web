# -*- coding: utf-8 -*-
from django.http import HttpResponse, HttpRequest
from django.shortcuts import render_to_response, get_object_or_404
from models import *

from django.views.decorators.http import require_GET
@require_GET

def test(request, *args, **kwargs):
    return HttpResponse('OK')

def page(pg=1):
    pg = pg.GET.get('page')
    if pg is None: pg=''
    question = get_object_or_404(Question)
    return render_to_response('index.html', {
        'page': {
            'title':'TITLE',
            'header':u'Хеадер!'+pg,
            'question':question[0]
        }
    })

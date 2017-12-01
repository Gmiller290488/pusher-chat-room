# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from pusher import Pusher
from .models import *
from django.http import JsonResponse, HttpResponse

#instantiate pusher
pusher = Pusher(app_id=u'', key=u'', secret=u'', cluster=u'eu')
# Create your views here.
# add the login required decorator, so the method cannot be accessed without login

@login_required(login_url='admin/login/')
def chat(request):
   return render(request, "chat.html");

# use the csrf_exempt decorator to exempt this function from csrf checks
@csrf_exempt
def broadcast(request):
# trigger the message, channel and event to pusher
   pusher.trigger(u'a_channel', u'an_event', {u'name': request.user.username, u'message': request.POST['message']})
   return HttpResponse("done");


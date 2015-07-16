from django.http import HttpResponse, HttpResponseRedirect, HttpResponsePermanentRedirect
from django.shortcuts import redirect, render_to_response, render
from django.template import RequestContext
from django.db import connection, transaction
from django.core.urlresolvers import reverse
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.sites.models import Site
from django.utils import timezone
from datetime import datetime
from django.db.models import Max
from django.utils.dateformat import format
from django.contrib.auth import logout as auth_logout
from django.conf import settings

#from jumpchat.socketio_ns import V1Namespace
import ShareCamReg
import string
import random
import logging
#from .models import Room
from datetime import date
#import jumpchat.utils
import json
import os

def index(request):
    return render_to_response('index.html', locals(), RequestContext(request))

def toBool(val):
    if val in ["true","True"]:
        return True
    if val in ["false","False"]:
        return False
    if val:
        return True
    return False

@csrf_exempt
def reg_mapview(request):
    return render_to_response("mapview.html", locals(), RequestContext(request))

@csrf_exempt
def reg_remove(request):
    q = request.GET
    params = {'room': '', 'type': 'random', 'serverName': settings.JUMPCHAT_SERVER, 'apiKey': settings.API_KEY  }
    jsonStr = ShareCamReg.regRemove(request, params, q)
    return HttpResponse(jsonStr, content_type="application/json")

@csrf_exempt
def reg_connect(request):
    q = request.GET
    params = {'room': '', 'type': 'random', 'serverName': settings.JUMPCHAT_SERVER, 'apiKey': settings.API_KEY  }
    url = ShareCamReg.regConnect(request, params, q)
    return HttpResponseRedirect(url)

@csrf_exempt
def reg_query(request):
    q = request.GET
    params = {'room': '', 'type': 'random', 'serverName': settings.JUMPCHAT_SERVER, 'apiKey': settings.API_KEY  }
    jsonStr = ShareCamReg.regQuery(request, params, q)
    response = HttpResponse(jsonStr, content_type="application/json")
    response['Access-Control-Allow-Origin'] = '*'
    return response

@csrf_exempt
def reg_config(request):
    q = request.GET
    config = {'type': 'random', 'serverName': settings.JUMPCHAT_SERVER }
    if "name" in q:
        name = q['name']
        path = "registry/config/%s.json" % (name,)
        config['name'] = name
        try:
            cfg = json.loads(file(path).read())
            for key in cfg:
                config[key] = cfg[key]
            config['configPath'] = path
        except:
            pass
    jsonStr = json.dumps(config)
    return HttpResponse(jsonStr, content_type="application/json")

@csrf_exempt
def reg_becomeguide(request):
    return render_to_response("becomeguide.html", locals(), RequestContext(request))

@csrf_exempt
def reg_notification(request):
    return render_to_response("notification.html", locals(), RequestContext(request))

@csrf_exempt
def reg_getNotification(request):
    obj = {}
    q = request.GET
    if "name" in q:
        name = q['name']
        path = "notifications/records/%s.json" % (name,)
        obj['name'] = name
        obj['configPath'] = path
        try:
            cfg = json.loads(file(path).read())
            for key in cfg:
                obj[key] = cfg[key]
        except:
            obj['error'] = 'could not get values'
    else:
        obj['error'] = 'no name specified'
    jsonStr = json.dumps(obj)
    return HttpResponse(jsonStr, content_type="application/json")

@csrf_exempt
def reg_setNotification(request):
    obj = {}
    q = request.GET
    obj['pattern_tags'] = q.get("pattern_tags", "")
    obj['active'] = toBool(q.get("active", False))
    obj['notifyByEmail'] = toBool(q.get("notifyByEmail", False))
    obj['notifyBySMS'] = toBool(q.get("notifyBySMS", False))
    obj['email'] = q.get("email", "")
    obj['phone'] = q.get("phone", "")
    obj['sms_carrier'] = q.get("sms_carrier", "")
    if "name" in q:
        name = q['name']
        path = "notifications/records/%s.json" % (name,)
        obj['name'] = name
        obj['configPath'] = path
        try:
            json.dump(obj, file(path,"w"))
        except:
            obj['error'] = 'could not save values'
    else:
        obj['error'] = 'no name specified'
    jsonStr = json.dumps(obj)
    return HttpResponse(jsonStr, content_type="application/json")

@csrf_exempt
def reg_delNotification(request):
    obj = {}
    q = request.GET
    if "name" in q:
        name = q['name']
        path = "notifications/records/%s.json" % (name,)
        obj['name'] = name
        obj['configPath'] = path
        try:
            os.unlink(path)
        except:
            obj['error'] = 'could not delete notification'
    else:
        obj['error'] = 'no name specified'
    jsonStr = json.dumps(obj)
    return HttpResponse(jsonStr, content_type="application/json")


@csrf_exempt
def reg(request):
    params = {'room': '', 'type': 'random', 'serverName': settings.JUMPCHAT_SERVER, 'apiKey': settings.API_KEY  }
    jsonStr = ShareCamReg.reg(request, params)
    return HttpResponse(jsonStr, content_type="application/json")

# Post version of reg
@csrf_exempt
def regp(request):
    params = {'room': '', 'type': 'random', 'serverName': settings.JUMPCHAT_SERVER, 'apiKey': settings.API_KEY  }
    jsonStr = ShareCamReg.regp(request, params)
#    jsonStr = json.dumps({'return_code': 'failed'})
    return HttpResponse(jsonStr, content_type="application/json")

def login(request):
    return render_to_response('login.html', locals(), RequestContext(request))

def logout(request):
    auth_logout(request)
    return redirect('index')


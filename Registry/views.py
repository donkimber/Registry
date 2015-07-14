from django.http import HttpResponse, HttpResponseRedirect, HttpResponsePermanentRedirect
from django.shortcuts import redirect, render_to_response, render
from django.template import RequestContext
from django.db import connection, transaction
from django.core.urlresolvers import reverse
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.sites.models import Site
import json
from django.utils import timezone
from datetime import datetime
from django.db.models import Max
from django.utils.dateformat import format
from django.contrib.auth import logout as auth_logout

def index(request):
    return render_to_response('index.html', locals(), RequestContext(request))


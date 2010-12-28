"""myEWB CHAMP analytics

This file is part of myEWB
Copyright 2010 Engineers Without Borders Canada

@author Francis Kung
"""

import csv, copy
from datetime import date

from django.core.urlresolvers import reverse
from django.shortcuts import get_object_or_404, render_to_response
from django.contrib.contenttypes.models import ContentType
from django.http import HttpResponseNotFound, HttpResponseRedirect, HttpResponse, HttpResponseForbidden
from django.db.models import Q
from django.template import RequestContext
from django.template.loader import render_to_string

from base_groups.decorators import group_admin_required
from networks.decorators import chapter_president_required, chapter_exec_required
from networks.models import Network
from champ.models import *
from champ.forms import *
from siteutils import schoolyear
from siteutils.helpers import fix_encoding, copy_model_instance
from siteutils.http import JsonResponse

def default(request):
    if not request.GET.get('stage', None):
        return select_graph(request)
    else:
        return draw_graph(request)
        
def select_graph(request):
    metric = request.GET.get('metric', None)
    group = request.GET.get('group', None)
    
    return render_to_response('champ/champalytics/select.html',
                              {},
                              context_instance=RequestContext(request))

def draw_graph(request):
    return HttpResponse("graph")

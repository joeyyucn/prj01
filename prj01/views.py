import django.views
from django.http.response import HttpResponse
from django.template.response import get_template
from django.template.loader import render_to_string

def indexView(request):
    return HttpResponse(render_to_string('index.html', {'headline1':'this is headline1'}))
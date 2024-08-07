from django.shortcuts import render
from django.http.response import HttpResponse
# Create your views here.
from .models import Tag
from django.template import Context, loader

def homepage(request):
    tag_list = Tag.objects.all()
    template = loader.get_template('organizer/tag_list.html')
    context ={'tag_list': tag_list}
    return HttpResponse(template.render(context))
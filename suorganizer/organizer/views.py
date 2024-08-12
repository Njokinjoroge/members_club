from django.shortcuts import render
from django.http.response import HttpResponse
# Create your views here.
from .models import Tag
from django.shortcuts import get_object_or_404
from django.template import Context, loader


def homepage(request):
    return render(request,"organizer/tag_list.html",{"tag_list":Tag.objects.all()})



def tag_detail(request,slug):
    tag=get_object_or_404(Tag,slug__iexact=slug)
    template = loader.get_template("organizer/tag_details.html")
    context ={'tag': tag}
    return HttpResponse(template.render(context))




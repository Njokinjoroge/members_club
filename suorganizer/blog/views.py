from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse
from .models import Post
# Create your views here.
def post_list(request):
    return render(request,"post_list.html",{"post_list":Post.objects.all()})

def post_details(request,year,month,slug):
    post = get_object_or_404(Post,pub_date__year=year,
                             pub_date__month=month,
                             slug=slug)
    
    return render(request,"post_details.html",{"post":post})

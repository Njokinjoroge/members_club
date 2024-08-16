from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse
from .models import Post
from django.views.generic import View
# Create your view
class Postlist(View):
    def get(self,request,parent_template=None):
        return render(request,"post_list.html",{"post_list":Post.objects.all(),'parent_template':parent_template})

def post_details(request,year,month,slug,parent_template=None):
    post = get_object_or_404(Post,pub_date__year=year,
                             pub_date__month=month,
                             slug=slug)
    
    return render(request,"post_details.html",{"post":post,'parent_template': parent_template})

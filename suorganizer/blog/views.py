from django.shortcuts import render,get_object_or_404,redirect
from django.http import HttpResponse
from .models import Post
from django.views.generic import View
from .forms import PostForm
# Create your view
class Postlist(View):
    def get(self,request,parent_template=None):
        return render(request,"post_list.html",{"post_list":Post.objects.all(),'parent_template':parent_template})

def post_details(request,year,month,slug,parent_template=None):
    post = get_object_or_404(Post,pub_date__year=year,
                             pub_date__month=month,
                             slug=slug)
    
    return render(request,"post_details.html",{"post":post,'parent_template': parent_template})

class PostCreate(View):
    form_class=PostForm
    template_name='blog/post_form.html'
    def get(self,request):
        return render(request,self.template_name,{'form':self.form_class()})   
    def post(self,request):
        form=self.form_class(request.POST)
        if form.is_valid:
            new_post=form.save()
            return redirect(new_post)    
        else:
            return render(request,self.template_name,{'form':form})

class PostUpdate(View):
  form_calss=PostForm
  model=Post
  template_name="post_form.html"
  def get_object(self,year,month,slug):
      return get_object_or_404(self.model,pub_date__year=year,pub_date__month=month,slug=slug)
  
  def get(self,request,year,month,slug):
      post=self.get_object(year,month,slug)
      context={
          'form':self.form_calss(instance=post),
          'post':post
      }
      return render(request,self.template_name,context)
  
  def post(self,request,year,slug,month):
      post=self.get_object(year,slug,month)
      bound_form= self.form_calss(request.post,instance=post)
      if bound_form.is_valid():
          new_post=bound_form.save()
          return redirect(new_post)
      else:
          context={
              "form":bound_form,"post":post
          }
          return render(request,self.template_name,context)


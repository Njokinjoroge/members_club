from django.http.response import HttpResponse
from .models import Tag,Startup
from django.views.generic import View
from django.shortcuts import get_object_or_404,redirect,render
from django.template import Context, loader
from.forms import TagForm


def tag_list(request):
    return render(request,"organizer/tag_list.html",{"tag_list":Tag.objects.all()})



def tag_detail(request,slug):
    tag=get_object_or_404(Tag,slug__iexact=slug)
    template = loader.get_template("organizer/tag_details.html")
    context ={'tag': tag}
    return HttpResponse(template.render(context))


def startup_list(request):
    return render(request,"organizer/startup_list.html",{'startup_list':Startup.objects.all()})

def startup_details(request,slug):
    startup=get_object_or_404(Startup,slug__iexact=slug)
    return render(request,"organizer/startup_detail.html",{'startup':startup})
    

# def tag_create(request):
#     if request.method == 'POST':
#         form=TagForm(request.POST)
#         if form.is_valid():
#             new_tag=form.save()
#             return redirect(new_tag)
        
#     else:
#         form =TagForm()
#         return render(request,"organizer/tag_form.html",{'form':form})
class TagCreate:
    form_class=TagForm
    template_name='organizer/tag_form.html'
    def get(self,request):
        return render(request,"organizer/tag_form.html",{'form':self.form_class()})
    def post(self,request):
        form=self.form_class(request.POST)
        if form.is_valid():
            new_tag=form.save()
            return redirect(new_tag)
        else:
            return render(request,self.template_name,{'form':form})


        
